use std::fs;

use std::collections::HashSet;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

type Grid = Vec<Vec<u32>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-10/input.txt")?;
    let grid = parse(&content);
    let res_1 = part_1(&grid);
    let res_2 = part_2(&grid);
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(grid: &Grid) -> usize {
    let trailheads = find_starting_positions(grid);
    trailheads.iter().fold(0, |acc, pos| {
        let mut found = HashSet::new();
        search_endpoints(grid, pos, &mut found);
        acc + found.len()
    })
}

fn part_2(grid: &Grid) -> usize {
    let trailheads = find_starting_positions(grid);
    trailheads
        .iter()
        .fold(0, |acc, pos| acc + search_paths(grid, pos))
}

fn search_paths(grid: &Grid, pos: &(usize, usize)) -> usize {
    if grid[pos.0][pos.1] == 9 {
        return 1;
    }

    surrounding(grid, pos).fold(0, |acc, pos| acc + search_paths(grid, &pos))
}

fn search_endpoints(grid: &Grid, pos: &(usize, usize), found: &mut HashSet<(usize, usize)>) {
    if grid[pos.0][pos.1] == 9 {
        found.insert(*pos);
    }

    surrounding(grid, pos).for_each(|pos| search_endpoints(grid, &pos, found));
}

fn surrounding<'a>(
    grid: &'a Grid,
    pos: &(usize, usize),
) -> impl Iterator<Item = (usize, usize)> + 'a {
    let &(x, y) = pos;
    let val = grid[x][y];
    [
        (x.wrapping_sub(1), y),
        (x + 1, y),
        (x, y.wrapping_sub(1)),
        (x, y + 1),
    ]
    .into_iter()
    .filter(move |&(sx, sy)| contained(grid, &(sx, sy)) && grid[sx][sy] == val + 1)
}

fn contained(grid: &Grid, pos: &(usize, usize)) -> bool {
    let &(x, y) = pos;
    x < grid.len() && y < grid[x].len()
}

fn find_starting_positions(grid: &Grid) -> HashSet<(usize, usize)> {
    let mut res = HashSet::new();
    for x in 0..grid.len() {
        for y in 0..grid[x].len() {
            if grid[x][y] == 0 {
                res.insert((x, y));
            }
        }
    }
    res
}

fn parse(content: &str) -> Grid {
    content
        .lines()
        .map(|l| {
            l.chars()
                .map(|e| e.to_digit(10).expect("a digit"))
                .collect()
        })
        .collect()
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let grid = parse(&content);
        let res = part_1(&grid);
        assert_eq!(36, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let grid = parse(&content);
        let res = part_2(&grid);
        assert_eq!(81, res);
        Ok(())
    }
}
