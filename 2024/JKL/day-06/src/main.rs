use std::str::FromStr;

struct Input {
    map: Vec<Vec<bool>>,
    start: (usize, usize),
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let map = s
            .lines()
            .map(|line| line.chars().map(|c| c == '#').collect())
            .collect();
        let start = s
            .lines()
            .enumerate()
            .filter_map(|(i, line)| line.find('^').map(|j| (i, j)))
            .next()
            .unwrap();
        Ok(Input { map, start })
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let answer = puzzle_1(input.parse().unwrap());
    println!("The solution to part 1 is '{}'", answer);
    let answer = puzzle_2(input.parse().unwrap());
    println!("The solution to part 2 is '{}'", answer);
}

enum Direction {
    Up,
    Down,
    Left,
    Right,
}

impl Direction {
    fn move_from(&self, (x, y): (usize, usize)) -> (usize, usize) {
        match self {
            Direction::Up => (x - 1, y),
            Direction::Down => (x + 1, y),
            Direction::Left => (x, y - 1),
            Direction::Right => (x, y + 1),
        }
    }

    fn is_leaving(&self, (x, y): (usize, usize), map: &Vec<Vec<bool>>) -> bool {
        match self {
            Direction::Up => x == 0,
            Direction::Down => x == map.len() - 1,
            Direction::Left => y == 0,
            Direction::Right => y == map[0].len() - 1,
        }
    }

    fn rotate(&self) -> Self {
        match self {
            Direction::Up => Direction::Right,
            Direction::Right => Direction::Down,
            Direction::Down => Direction::Left,
            Direction::Left => Direction::Up,
        }
    }
}

fn puzzle_1(input: Input) -> i32 {
    let map = input.map;
    let mut marked: Vec<Vec<bool>> = vec![vec![false; map[0].len()]; map.len()];
    let mut pos = input.start;
    let mut dir = Direction::Up;

    loop {
        marked[pos.0][pos.1] = true;
        if dir.is_leaving(pos, &map) {
            break;
        }
        let new_pos = dir.move_from(pos);
        if map[new_pos.0][new_pos.1] {
            dir = dir.rotate();
        } else {
            pos = new_pos;
        }
    }

    marked.into_iter().flatten().filter(|&b| b).count() as i32
}

fn puzzle_2(input: Input) -> i32 {
    todo!()
}

#[cfg(test)]
mod test_day_06 {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 41);
    }

    // #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, todo!());
    }
}
