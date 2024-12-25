#[macro_use]
extern crate lazy_static;
extern crate regex;

use std::collections::{HashMap, HashSet};
use std::fs;

use regex::Regex;

const X_MAX: isize = 101;
const Y_MAX: isize = 103;
const ITERATION_LIMIT: usize = 10_000;
const LINE_LENGTH: usize = 15;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-14/input.txt")?;
    let robots: Vec<Robot> = parse(&content, X_MAX, Y_MAX).collect();
    let res_1 = part_1(&robots);
    let res_2 = part_2(&robots);
    println!("Part 1: {}", res_1);
    println!(
        "Part 2: {}",
        res_2.expect("limit reached without finding anything")
    );
    Ok(())
}

fn part_1(robots: &Vec<Robot>) -> usize {
    let mut quartals: HashMap<usize, usize> = HashMap::new();
    let mut robs = robots.clone();
    robs.iter_mut().for_each(|r| r.estimate(100));
    for r in robs {
        if let Some(q) = r.p.quartal() {
            let count = quartals.entry(q).or_default();
            *count += 1;
        }
    }
    quartals
        .into_values()
        .reduce(|acc, e| acc * e)
        .unwrap_or_default()
}

fn part_2(robots: &Vec<Robot>) -> Option<usize> {
    let mut robs = robots.clone();
    for idx in 1..ITERATION_LIMIT {
        robs.iter_mut().for_each(|r| r.reposition());
        if check_vertical_line(&robs) {
            return Some(idx);
        }
    }
    None
}

fn check_vertical_line(robots: &[Robot]) -> bool {
    let mut grid: HashMap<isize, HashSet<isize>> = HashMap::new();
    for robot in robots {
        let row = grid.entry(robot.p.x).or_default();
        row.insert(robot.p.y);
    }
    let mut contiguous = 0;
    for row in grid.values() {
        for idx in 0..robots[0].p.y_max {
            if row.contains(&idx) {
                contiguous += 1;
            } else {
                contiguous = 0;
            }
            if contiguous > LINE_LENGTH {
                return true;
            }
        }
    }
    false
}

fn parse(content: &str, x_max: isize, y_max: isize) -> impl Iterator<Item = Robot> + '_ {
    lazy_static! {
        static ref RE: Regex = Regex::new(
            r"(?x)
            p=
            (?P<px>[0-9]+),(?P<py>[0-9]+)
            \s
            v=
            (?P<vx>\-?[0-9]+),(?P<vy>\-?[0-9]+)
            "
        )
        .unwrap();
    }
    RE.captures_iter(content).map(move |e| Robot {
        p: Vector {
            x: e["px"].parse().unwrap(),
            y: e["py"].parse().unwrap(),
            x_max,
            y_max,
        },
        v: Vector {
            x: e["vx"].parse().unwrap(),
            y: e["vy"].parse().unwrap(),
            x_max,
            y_max,
        },
    })
}

#[derive(Debug, Clone)]
struct Vector {
    x: isize,
    y: isize,
    x_max: isize,
    y_max: isize,
}

impl ::std::ops::Add<&Vector> for &Vector {
    type Output = Vector;

    fn add(self, rhs: &Vector) -> Self::Output {
        let mut x = self.x + rhs.x;
        if x >= self.x_max || x < 0 {
            x = x.rem_euclid(self.x_max);
        }
        let mut y = self.y + rhs.y;
        if y >= self.y_max || y < 0 {
            y = y.rem_euclid(self.y_max);
        }
        Self::Output {
            x,
            y,
            x_max: self.x_max,
            y_max: self.y_max,
        }
    }
}

impl Vector {
    fn quartal(&self) -> Option<usize> {
        let x_half = self.x_max / 2;
        let y_half = self.y_max / 2;
        match (self.x, self.y) {
            (x, y) if x < x_half && y < y_half => Some(1),
            (x, y) if x > x_half && y < y_half => Some(2),
            (x, y) if x > x_half && y > y_half => Some(3),
            (x, y) if x < x_half && y > y_half => Some(4),
            _ => None,
        }
    }
}

#[derive(Debug, Clone)]
struct Robot {
    p: Vector,
    v: Vector,
}

impl Robot {
    fn reposition(&mut self) {
        self.p = &self.p + &self.v;
    }

    fn estimate(&mut self, time: usize) {
        for _ in 0..time {
            self.reposition()
        }
    }
}

#[cfg(test)]
mod test {
    use crate::*;

    const X_MAX_TEST: isize = 11;
    const Y_MAX_TEST: isize = 7;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let robots: Vec<Robot> = parse(&content, X_MAX_TEST, Y_MAX_TEST).collect();
        let res = part_1(&robots);
        assert_eq!(12, res);
        Ok(())
    }
}
