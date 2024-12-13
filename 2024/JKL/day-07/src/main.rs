use std::str::FromStr;

struct Input {
    equations: Vec<(u64, Vec<u64>)>
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            equations: raw_input.lines()
                .map(|line| line.split_once(":").unwrap())
                .map(|(value, numbers)| (
                    value.parse().unwrap(),
                    numbers.split_whitespace()
                        .map(|number| number.parse().unwrap())
                        .collect()))
                .collect()
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

fn check_possibilities(value: &u64, numbers: &[u64], current: u64) -> bool {
    match numbers {
        [] => current == *value,
        [head, tail @ ..] => {
            check_possibilities(value, tail, current + head)
                || check_possibilities(value, tail, current * head)
        },
    }
}

fn puzzle_1(input: Input) -> u64 {
    input.equations.iter()
        .filter(|(value, numbers)| check_possibilities(value, numbers, 0))
        .map(|(value, _)| value)
        .sum()
}

fn concat(lhs: &u64, rhs: &u64) -> u64 {
    if *rhs > 0 {
        lhs * 10u64.pow(rhs.ilog10() + 1) + rhs
    } else {
        *rhs
    }
}
fn check_concat(value: &u64, numbers: &[u64], current: u64) -> bool {
    match numbers {
        [] => current == *value,
        [head, tail @ ..] => {
            check_concat(value, tail, current + head)
                || check_concat(value, tail, current * head)
                || check_concat(value, tail, concat(&current, head))
        },
    }
}

fn puzzle_2(input: Input) -> u64 {
    input.equations.iter()
        .filter(|(value, numbers)| check_concat(value, numbers, 0))
        .map(|(value, _)| value)
        .sum()
}

#[cfg(test)]
mod test_day_07 {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 3749);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 11387);
    }
}
