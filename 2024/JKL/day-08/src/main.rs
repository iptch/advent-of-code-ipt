use itertools::Itertools;
use std::str::FromStr;

struct Input {
    antennas: Vec<(char, (i32, i32))>,
    height: i32,
    width: i32,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            antennas: raw_input
                .lines()
                .enumerate()
                .flat_map(|(i, line)| {
                    line.chars()
                        .enumerate()
                        .map(|(j, c)| (c, (i as i32, j as i32)))
                        .collect::<Vec<_>>()
                })
                .filter(|(c, _)| *c != '.')
                .collect(),
            height: raw_input.lines().count() as i32,
            width: raw_input.lines().next().unwrap().len() as i32,
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

fn antinodes(antennas: &Vec<(i32, i32)>) -> Vec<(i32, i32)> {
    antennas
        .iter()
        .permutations(2)
        .flat_map(|pair| match pair[..] {
            [(x, y), (a, b)] => {
                let d = (x - a, y - b);
                let p = (x + d.0, y + d.1);
                let q = (a - d.0, b - d.1);
                vec![p, q]
            }
            _ => unreachable!(),
        })
        .collect()
}

fn puzzle_1(input: Input) -> usize {
    let height = input.height;
    let width = input.width;

    input
        .antennas
        .into_iter()
        .into_group_map()
        .into_values()
        .flat_map(|antennas| antinodes(&antennas))
        .filter(|(x, y)| *x >= 0 && *x < height && *y >= 0 && *y < width)
        .unique()
        .count()
}

fn all_antinodes(antennas: &Vec<(i32, i32)>, height: i32, width: i32) -> Vec<(i32, i32)> {
    antennas
        .iter()
        .permutations(2)
        .flat_map(|pair| match pair[..] {
            [(x, y), (a, b)] => {
                let d = (x - a, y - b);
                let up: Vec<(i32, i32)> = (0..)
                    .map(|i| (x + i * d.0, y + i * d.1))
                    .take_while(|&(x, y)| x >= 0 && x < height && y >= 0 && y < width)
                    .collect();
                let down: Vec<(i32, i32)> = (0..)
                    .map(|i| (x - i * d.0, y - i * d.1))
                    .take_while(|&(x, y)| x >= 0 && x < height && y >= 0 && y < width)
                    .collect();
                vec![up, down].concat()
            }
            _ => unreachable!("we only have pairs coming in"),
        })
        .collect()
}

fn puzzle_2(input: Input) -> usize {
    let height = input.height;
    let width = input.width;

    input
        .antennas
        .into_iter()
        .into_group_map()
        .into_values()
        .flat_map(|antennas| all_antinodes(&antennas, height, width))
        .unique()
        .count()
}

#[cfg(test)]
mod test_day_08 {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 14);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 34);
    }
}
