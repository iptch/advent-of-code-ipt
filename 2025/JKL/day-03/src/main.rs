use std::str::FromStr;

#[derive(Debug)]
struct Input {
    banks: Vec<Vec<u32>>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            banks: raw_input
                .lines()
                .map(|line| line.chars().map(|c| c.to_digit(10).unwrap()).collect())
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

fn puzzle_1(input: Input) -> u64 {
    input
        .banks
        .iter()
        .map(|bank| find_max_in_bank(bank, 2))
        .sum()
}

fn puzzle_2(input: Input) -> u64 {
    input
        .banks
        .iter()
        .map(|bank| find_max_in_bank(bank, 12))
        .sum()
}

/// Computes the largest number that can be build from the digits in `bank` using `digits` many digits.
///
/// The solution works using dynamic programming, where `dp[i][j]` represents the largest number
/// that can be build using `i` digits using the digits in `bank[0..j]`.
///
/// `dp[i][j]` is computed as the max of:
/// - `dp[i][j - 1]`: not using the current digit, thus the result is the same as the previous
///   result
/// - `dp[i - 1][j - 1] * 10 + bank[j - 1]`: using the digit, thus appending the maximum for
///   `bank[0..j-1]` with the current digit
fn find_max_in_bank(bank: &Vec<u32>, digits: usize) -> u64 {
    let mut dp = vec![vec![0_u64; bank.len() + 1]; digits + 1];

    for i in 1..=digits {
        for j in 1..=bank.len() {
            dp[i][j] = u64::max(dp[i][j - 1], dp[i - 1][j - 1] * 10 + bank[j - 1] as u64)
        }
    }

    dp[digits][bank.len()]
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 357);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 3121910778619);
    }
}
