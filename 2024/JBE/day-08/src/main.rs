use std::collections::{HashMap, HashSet};
use std::fs;

use itertools::Itertools;
use std::str::FromStr;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-08/input.txt")?;
    let res_1 = part_1(&content)?;
    let res_2 = part_2(&content)?;
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(input: &str) -> Result<isize> {
    reduce_for_antennas(input, |p1, p2, grid, locs| {
        let diff = p1 - p2;
        for interference in [p1 + &diff, p2 - &diff] {
            if interference.contained(grid) {
                locs.insert(interference);
            }
        }
    })
}

fn part_2(input: &str) -> Result<isize> {
    reduce_for_antennas(input, |p1, p2, grid, locs| {
        locs.insert(*p1);
        for delta in [p1 - p2, p2 - p1] {
            let mut point = p1 + &delta;
            while point.contained(grid) {
                locs.insert(point);
                point = &point + &delta;
            }
        }
    })
}

fn reduce_for_antennas<F>(input: &str, func: F) -> Result<isize>
where
    F: Fn(&Point, &Point, &Grid, &mut HashSet<Point>),
{
    let grid: Grid = input.parse()?;
    let mut res = HashSet::new();
    for (_, points) in grid.antennas.iter() {
        for comb in points.iter().combinations(2) {
            let [p1, p2] = comb[..] else {
                return Err("too many elements in combination".into());
            };
            func(p1, p2, &grid, &mut res);
        }
    }
    res.len()
        .try_into()
        .or(Err("failed to convert usize to isize".into()))
}

#[derive(Debug, Clone, Copy, Hash, PartialEq, Eq)]
struct Point {
    x: isize,
    y: isize,
}

impl Point {
    fn contained(&self, grid: &Grid) -> bool {
        self.x >= grid.x_min && self.x <= grid.x_max && self.y >= grid.y_min && self.y <= grid.y_max
    }
}

impl ::std::ops::Add<&Point> for &Point {
    type Output = Point;

    fn add(self, rhs: &Point) -> Self::Output {
        Self::Output {
            x: self.x + rhs.x,
            y: self.y + rhs.y,
        }
    }
}

impl ::std::ops::Sub<&Point> for &Point {
    type Output = Point;

    fn sub(self, rhs: &Point) -> Self::Output {
        Self::Output {
            x: self.x - rhs.x,
            y: self.y - rhs.y,
        }
    }
}

#[derive(Debug, Clone)]
struct Grid {
    antennas: HashMap<char, HashSet<Point>>,
    x_min: isize,
    x_max: isize,
    y_min: isize,
    y_max: isize,
}

impl Grid {}

impl FromStr for Grid {
    type Err = Box<dyn ::std::error::Error>;

    fn from_str(s: &str) -> Result<Grid> {
        let mut antennas = HashMap::new();
        let lines: Vec<&str> = s.lines().collect();
        for (y, line) in lines.iter().enumerate() {
            for (x, val) in line.chars().enumerate() {
                if val != '.' {
                    let point = Point {
                        x: x.try_into()?,
                        y: y.try_into()?,
                    };
                    antennas
                        .entry(val)
                        .and_modify(|entry: &mut HashSet<Point>| {
                            entry.insert(point);
                        })
                        .or_insert(HashSet::from([point]));
                }
            }
        }
        Ok(Grid {
            x_min: 0,
            x_max: lines[0].len() as isize - 1,
            y_min: 0,
            y_max: lines.len() as isize - 1,
            antennas,
        })
    }
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let res = part_1(&content)?;
        assert_eq!(14, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let res = part_2(&content)?;
        assert_eq!(34, res);
        Ok(())
    }
}
