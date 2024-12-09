use std::cmp;
use std::iter::zip;
use std::str::FromStr;

struct Input {
    reports: Vec<Vec<i32>>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            reports: s
                .lines()
                .map(|line| {
                    line.split_whitespace()
                        .map(|val| val.parse().unwrap())
                        .collect()
                })
                .collect(),
        })
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let answer = puzzle_1(input.parse().unwrap());
    println!("The solution to part 1 is '{}'", answer);
    let answer = puzzle_2(input.parse().unwrap());
    println!("The solution to part 2 is '{}'", answer);
}

fn puzzle_1(input: Input) -> i32 {
    input.reports.into_iter().filter(is_safe).count() as i32
}

fn is_safe(report: &Vec<i32>) -> bool {
    let (min, max) = zip(report.iter(), report.iter().skip(1))
        .map(|(a, b)| a - b)
        .fold((i32::MAX, i32::MIN), |(min, max), x| {
            (cmp::min(min, x), cmp::max(max, x))
        });
    (min >= 1 && max <= 3) || (min >= -3 && max <= -1)
}

fn puzzle_2(input: Input) -> i32 {
    input
        .reports
        .into_iter()
        .filter(is_save_with_damper)
        .count() as i32
}

fn is_save_with_damper(report: &Vec<i32>) -> bool {
    (0..report.len())
        .into_iter()
        .map(|i| [&report[..i], &report[i + 1..]].concat().to_vec())
        .any(|report| is_safe(&report))
}

#[cfg(test)]
mod test_day_02 {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 2);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 4);
    }
}
