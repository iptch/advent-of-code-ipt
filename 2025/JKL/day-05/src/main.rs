use std::{cmp::Ordering, str::FromStr};

#[derive(Debug)]
struct Input {
    ranges: Vec<(i64, i64)>,
    products: Vec<i64>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        let (ranges, products) = raw_input.split_once("\n\n").unwrap();

        Ok(Input {
            ranges: ranges
                .lines()
                .map(|line| line.split_once("-").unwrap())
                .map(|(i, j)| (i.parse().unwrap(), j.parse().unwrap()))
                .collect(),
            products: products.lines().map(|line| line.parse().unwrap()).collect(),
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
    let ranges = sort_and_compact(input.ranges);

    input
        .products
        .into_iter()
        .filter(|product| in_range(&ranges, *product))
        .count() as i64
}

fn in_range(ranges: &Vec<(i64, i64)>, product: i64) -> bool {
    ranges
        .binary_search_by(|(lower, upper)| match product {
            p if p < *lower => Ordering::Greater,
            p if p > *upper => Ordering::Less,
            _ => Ordering::Equal,
        })
        .is_ok()
}

fn puzzle_2(input: Input) -> i64 {
    let ranges = sort_and_compact(input.ranges);

    ranges
        .into_iter()
        .flat_map(|(lower, upper)| lower..=upper)
        .count() as i64
}

fn sort_and_compact(mut ranges: Vec<(i64, i64)>) -> Vec<(i64, i64)> {
    ranges.sort_by_key(|(x, _)| *x);

    ranges.into_iter().fold(vec![], compact)
}

fn compact(mut accumulator: Vec<(i64, i64)>, value: (i64, i64)) -> Vec<(i64, i64)> {
    if let Some(last) = accumulator.last()
        && last.1 >= value.0
    {
        let last_idx = accumulator.len() - 1;
        accumulator[last_idx] = (last.0, i64::max(value.1, last.1));
    } else {
        accumulator.push(value);
    }

    accumulator
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 3);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 14);
    }
}
