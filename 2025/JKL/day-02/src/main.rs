use std::{ops::RangeInclusive, str::FromStr};

struct Input {
    ranges: Vec<RangeInclusive<i64>>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            ranges: raw_input
                .lines()
                .next()
                .unwrap()
                .split(',')
                .map(|range| range.split_once('-').unwrap())
                .map(|(left, right)| (left.parse().unwrap(), right.parse().unwrap()))
                .map(|(left, right)| left..=right)
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

fn puzzle_1(input: Input) -> i64 {
    input
        .ranges
        .iter()
        .flat_map(|range| range.clone().into_iter())
        .filter(|number| is_repeated_twice(number))
        .sum()
}

fn is_repeated_twice(number: &i64) -> bool {
    let number = number.to_string();
    if number.len() % 2 == 0 {
        let (left, right) = number.split_at(number.len() / 2);
        return left == right;
    }
    false
}

fn puzzle_2(input: Input) -> i64 {
    input
        .ranges
        .iter()
        .flat_map(|range| range.clone().into_iter())
        .filter(|number| is_repeated(number))
        .sum()
}

fn is_repeated(number: &i64) -> bool {
    let number = number.to_string();
    for i in 2..=number.len() {
        if number.len() % i != 0 {
            continue;
        }
        let split = number.len() / i;
        let first = &number[0..split];
        let mut matches = true;
        for j in 1..i {
            let start = j * split;
            let part = &number[start..start+split];
            if first != part {
                matches = false;
                break;
            }
        }
        if matches {
            return true;
        }
    }

    false
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 1227775554);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 4174379265);
    }
}
