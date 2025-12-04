use std::str::FromStr;

use itertools::Itertools;

#[derive(Debug)]
struct Input {
    map: Vec<Vec<bool>>,
    n: i32,
    m: i32,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        let map: Vec<Vec<bool>> = raw_input
            .lines()
            .map(|line| line.chars().map(|c| c == '@').collect())
            .collect();
        Ok(Input {
            n: map.len() as i32,
            m: map[0].len() as i32,
            map: map,
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
    get_accessible(&input).len() as i32
}

fn get_accessible(input: &Input) -> Vec<(i32, i32)> {
    (0..input.n)
        .cartesian_product(0..input.m)
        .filter(|(i, j)| input.map[*i as usize][*j as usize])
        .filter(|(i, j)| count_arount(*i, *j, &input) < 4)
        .collect()
}

fn count_arount(i: i32, j: i32, input: &Input) -> i32 {
    (i - 1..=i + 1)
        .cartesian_product(j - 1..=j + 1)
        .filter(|(x, y)| *x != i || *y != j)
        .filter(|(x, y)| *x >= 0 && *y >= 0)
        .filter(|(x, y)| *x < input.n as i32 && *y < input.m)
        .filter(|(x, y)| input.map[*x as usize][*y as usize])
        .count() as i32
}

fn puzzle_2(mut input: Input) -> i32 {
    let mut count: i32 = 0;
    loop {
        let accessible = get_accessible(&input);
        if accessible.len() == 0 {
            return count;
        }
        count += accessible.len() as i32;
        remove(&mut input, accessible);
    }
}

fn remove(input: &mut Input, list: Vec<(i32, i32)>) {
    list.iter()
        .for_each(|(i, j)| input.map[*i as usize][*j as usize] = false);
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 13);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 43);
    }
}
