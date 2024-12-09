use std::cmp::Ordering;
use std::collections::HashMap;
use std::str::FromStr;

struct Input {
    partial_order: HashMap<(i32, i32), bool>,
    updates: Vec<Vec<i32>>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut lines = s.lines();

        let mut partial_order = HashMap::new();
        lines
            .by_ref()
            .take_while(|l| !l.is_empty())
            .for_each(|line| {
                let (before, after) = line.split_once("|").unwrap();
                let (Ok(before), Ok(after)) = (before.parse::<i32>(), after.parse()) else {
                    panic!("Invalid input");
                };
                partial_order.insert((before, after), true);
                partial_order.insert((after, before), false);
            });

        let updates: Vec<Vec<i32>> = lines
            .map(|line| line.split(",").map(|i| i.parse().unwrap()).collect())
            .collect();

        Ok(Input {
            partial_order,
            updates,
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
    input
        .updates
        .iter()
        .filter(|update| is_ordered(&input, update))
        .map(|update| update[update.len() / 2])
        .sum()
}

fn is_ordered(input: &Input, update: &Vec<i32>) -> bool {
    update.is_sorted_by(|lhs, rhs| *input.partial_order.get(&(*lhs, *rhs)).unwrap())
}

fn puzzle_2(input: Input) -> i32 {
    input
        .updates
        .clone()
        .into_iter()
        .filter(|update| !is_ordered(&input, update))
        .map(|update| select_nth(&input, update))
        .sum()
}

fn select_nth(input: &Input, mut update: Vec<i32>) -> i32 {
    let len = update.len();
    *update
        .select_nth_unstable_by(len / 2, |lhs, rhs| partial_ordering(&input, lhs, rhs))
        .1
}

fn partial_ordering(input: &Input, lhs: &i32, rhs: &i32) -> Ordering {
    match *input.partial_order.get(&(*lhs, *rhs)).unwrap() {
        true => Ordering::Less,
        false => Ordering::Greater,
    }
}

#[cfg(test)]
mod test_day_05 {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 143);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 123);
    }
}
