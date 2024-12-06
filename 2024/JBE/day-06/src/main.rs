use std::collections::HashSet;
use std::fs;

use std::str::FromStr;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-06/input.txt")?;
    let (grid, guard) = parse(&content);
    let res_1 = part_1(&grid, &guard);
    let res_2 = part_2(&grid, &guard);
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(grid: &Vec<Vec<Cell>>, guard: &(usize, usize)) -> usize {
    let mut grid = Grid::new(grid.clone(), guard);
    while grid.move_guard() {}
    grid.count_visited()
}

fn part_2(input: &Vec<Vec<Cell>>, guard: &(usize, usize)) -> usize {
    let mut grid = Grid::new(input.clone(), guard);
    while grid.move_guard() {}
    let mut count = 0;
    for i in 0..grid.inner.len() {
        for j in 0..grid.inner[i].len() {
            if grid.inner[i][j] == Cell::Visited && !(i == guard.0 && j == guard.1) {
                let mut new_grid = Grid::new(input.clone(), guard);
                new_grid.inner[i][j] = Cell::Obstacle;
                while new_grid.move_guard() {
                    if new_grid.is_in_loop() {
                        count = count + 1;
                        break;
                    }
                }
            }
        }
    }
    count
}

fn parse(content: &str) -> (Vec<Vec<Cell>>, (usize, usize)) {
    let mut guard = (0, 0);
    let result = content
        .lines()
        .enumerate()
        .map(|(i, l)| {
            l.chars()
                .enumerate()
                .map(|(j, e)| {
                    let cell = e.to_string().parse::<Cell>().unwrap();
                    if cell == Cell::Guard {
                        guard = (i, j);
                    }
                    cell
                })
                .collect()
        })
        .collect();
    (result, guard)
}

#[derive(Debug, Clone)]
struct Grid {
    inner: Vec<Vec<Cell>>,
    dir: Direction,
    position: (isize, isize),
    x_len: isize,
    y_len: isize,
    history: HashSet<(isize, isize, Direction)>,
}

impl Grid {
    fn new(grid: Vec<Vec<Cell>>, start: &(usize, usize)) -> Self {
        let x_len = grid.len().try_into().unwrap();
        let y_len = grid[0].len().try_into().unwrap();
        let &(i, j) = start;
        let position = (i.try_into().unwrap(), j.try_into().unwrap());
        Self {
            inner: grid,
            dir: Direction::Up,
            position,
            x_len,
            y_len,
            history: HashSet::new(),
        }
    }

    fn contains(&self, position: &(isize, isize)) -> bool {
        let &(x, y) = position;
        0 <= x && x < self.x_len && 0 <= y && y < self.y_len
    }

    fn count_visited(&self) -> usize {
        self.inner
            .iter()
            .flatten()
            .filter(|&e| *e == Cell::Visited || *e == Cell::Guard)
            .count()
    }

    fn is_in_loop(&self) -> bool {
        self.history
            .contains(&(self.position.0, self.position.1, self.dir))
    }

    fn move_guard(&mut self) -> bool {
        let next_pos = self.dir.from_position(&self.position);
        if !self.contains(&next_pos) {
            self.inner[self.position.0 as usize][self.position.1 as usize] = Cell::Visited;
            return false;
        }

        if self.inner[next_pos.0 as usize][next_pos.1 as usize] == Cell::Obstacle {
            self.dir = self.dir.turn_90();
            return true;
        }

        self.history
            .insert((self.position.0, self.position.1, self.dir));

        self.inner[self.position.0 as usize][self.position.1 as usize] = Cell::Visited;
        self.position = next_pos;
        true
    }
}

#[derive(Debug, Clone, Copy, Eq, PartialEq, Hash)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

impl Direction {
    fn turn_90(&self) -> Self {
        match self {
            Self::Up => Self::Right,
            Self::Right => Self::Down,
            Self::Down => Self::Left,
            Self::Left => Self::Up,
        }
    }

    fn from_position(&self, position: &(isize, isize)) -> (isize, isize) {
        let &(x, y) = position;
        match *self {
            Direction::Up => (x - 1, y),
            Direction::Down => (x + 1, y),
            Direction::Left => (x, y - 1),
            Direction::Right => (x, y + 1),
        }
    }
}

#[derive(Debug, PartialEq, Eq, Clone)]
enum Cell {
    Guard,
    Obstacle,
    Visited,
    Unvisited,
}

impl FromStr for Cell {
    type Err = Box<dyn ::std::error::Error>;

    fn from_str(s: &str) -> Result<Cell> {
        Ok(match s {
            "#" => Cell::Obstacle,
            "^" => Cell::Guard,
            "." => Cell::Unvisited,
            _ => Err("cannot parse cell")?,
        })
    }
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let (grid, guard) = parse(&content);
        let res = part_1(&grid, &guard);
        assert_eq!(41, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let (grid, guard) = parse(&content);
        let res = part_2(&grid, &guard);
        assert_eq!(6, res);
        Ok(())
    }
}
