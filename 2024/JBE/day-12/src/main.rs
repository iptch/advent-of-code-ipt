use std::collections::{BTreeSet, HashMap};
use std::fs;

use itertools::Itertools;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

type Grid = Vec<Vec<char>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-12/input.txt")?;
    let grid = parse(&content);
    let res_1 = part_1(&grid);
    let res_2 = part_2(&grid);
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(grid: &Grid) -> usize {
    let mut cache: HashMap<BTreeSet<(usize, usize)>, usize> = HashMap::new();
    let mut sum = 0;
    for position in positions(grid) {
        if let Some(area) = cache.keys().find(|area| area.contains(&position)) {
            sum += cache[area];
        } else {
            let area = area(grid, &position);
            let perimeter = area.iter().map(|pos| fence_perimiter(grid, pos)).sum();
            cache.insert(area, perimeter);
            sum += perimeter;
        }
    }
    sum
}

fn part_2(grid: &Grid) -> usize {
    let mut cache: HashMap<BTreeSet<(usize, usize)>, usize> = HashMap::new();
    let mut sum = 0;
    for position in positions(grid) {
        if let Some(area) = cache.keys().find(|area| area.contains(&position)) {
            sum += cache[area];
        } else {
            let area = area(grid, &position);
            let corners = area.iter().map(|pos| fence_corner_count(grid, pos)).sum();
            cache.insert(area, corners);
            sum += corners;
        }
    }
    sum
}

fn area(grid: &Grid, pos: &(usize, usize)) -> BTreeSet<(usize, usize)> {
    let mut area = BTreeSet::new();
    let val = grid[pos.0][pos.1];
    area.insert(*pos);

    fn inner(g: &Grid, p: &(usize, usize), val: char, a: &mut BTreeSet<(usize, usize)>) {
        for position in surrounding(p).filter(|p| contained(g, p) && g[p.0][p.1] == val) {
            if !a.contains(&position) {
                a.insert(position);
                inner(g, &position, val, a);
            }
        }
    }

    inner(grid, pos, val, &mut area);
    area
}

fn fence_perimiter(grid: &Grid, pos: &(usize, usize)) -> usize {
    let val = grid[pos.0][pos.1];
    surrounding(pos)
        .filter(|p| !contained(grid, p) || grid[p.0][p.1] != val)
        .count()
}

fn fence_corner_count(grid: &Grid, pos: &(usize, usize)) -> usize {
    let val = grid[pos.0][pos.1];
    let mut res = corners(pos)
        .filter(|(p1, p2)| {
            (!contained(grid, p1) || grid[p1.0][p1.1] != val)
                && (!contained(grid, p2) || grid[p2.0][p2.1] != val)
        })
        .count();
    res += outer_corners(pos)
        .filter(|(p1, p2, p3)| {
            (contained(grid, p1) && grid[p1.0][p1.1] == val)
                && (!contained(grid, p2) || grid[p2.0][p2.1] != val)
                && (contained(grid, p3) && grid[p3.0][p3.1] == val)
        })
        .count();
    res
}

fn positions(grid: &Grid) -> impl Iterator<Item = (usize, usize)> {
    (0..grid.len()).cartesian_product(0..grid[0].len())
}

fn surrounding(pos: &(usize, usize)) -> impl Iterator<Item = (usize, usize)> {
    let &(x, y) = pos;
    [
        (x.wrapping_sub(1), y),
        (x + 1, y),
        (x, y.wrapping_sub(1)),
        (x, y + 1),
    ]
    .into_iter()
}

fn corners(pos: &(usize, usize)) -> impl Iterator<Item = ((usize, usize), (usize, usize))> {
    let &(x, y) = pos;
    [
        ((x.wrapping_sub(1), y), (x, y + 1)),
        ((x.wrapping_sub(1), y), (x, y.wrapping_sub(1))),
        ((x + 1, y), (x, y + 1)),
        ((x + 1, y), (x, y.wrapping_sub(1))),
    ]
    .into_iter()
}

fn outer_corners(
    pos: &(usize, usize),
) -> impl Iterator<Item = ((usize, usize), (usize, usize), (usize, usize))> {
    let &(x, y) = pos;
    [
        (
            (x.wrapping_sub(1), y),
            (x.wrapping_sub(1), y + 1),
            (x, y + 1),
        ),
        (
            (x.wrapping_sub(1), y),
            (x.wrapping_sub(1), y.wrapping_sub(1)),
            (x, y.wrapping_sub(1)),
        ),
        ((x + 1, y), (x + 1, y + 1), (x, y + 1)),
        (
            (x + 1, y),
            (x + 1, y.wrapping_sub(1)),
            (x, y.wrapping_sub(1)),
        ),
    ]
    .into_iter()
}

fn contained(grid: &Grid, pos: &(usize, usize)) -> bool {
    let &(x, y) = pos;
    x < grid.len() && y < grid[x].len()
}

fn parse(content: &str) -> Grid {
    content.lines().map(|l| l.chars().collect()).collect()
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let grid = parse(&content);
        let res = part_1(&grid);
        assert_eq!(1930, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let grid = parse(&content);
        let res = part_2(&grid);
        assert_eq!(1206, res);
        Ok(())
    }
}
