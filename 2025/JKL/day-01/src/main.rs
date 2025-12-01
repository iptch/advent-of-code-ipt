use std::str::FromStr;

#[derive(Debug)]
enum Rotation {
    Left(i32),
    Right(i32),
}

impl FromStr for Rotation {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(match raw_input.split_at(1) {
            ("L", num) => Self::Left(num.parse()?),
            ("R", num) => Self::Right(num.parse()?),
            _ => panic!("Invalid input"),
        })
    }
}

struct Input {
    rotations: Vec<Rotation>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            rotations: raw_input
                .lines()
                .map(|line| line.parse().unwrap())
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
    let mut count: i32 = 0;
    let mut position: i32 = 50;
    for rotation in input.rotations {
        position = match rotation {
            Rotation::Left(diff) => position - diff,
            Rotation::Right(diff) => position + diff,
        }.rem_euclid(100);
        if position == 0 {
            count += 1;
        }
    }
    count
}

fn puzzle_2(input: Input) -> i32 {
    let mut count: i32 = 0;
    let mut position: i32 = 50;
    for rotation in input.rotations {
        let new_position = match rotation {
            Rotation::Left(diff) => position - diff,
            Rotation::Right(diff) => position + diff,
        };
        count += new_position.div_euclid(100).abs();

        // edge case: when we left rotate directly to a multiple of 0 we need to
        // count that 0 as well
        if let Rotation::Left(_) = rotation && new_position.rem_euclid(100) == 0 {
            count += 1;
        }

        // edge case: when we left rotate starting from 0 we need to subtract
        // one because the 0 was already counted in the previous iteration
        if let Rotation::Left(_) = rotation && position == 0 {
            count -= 1;
        }
        position = new_position.rem_euclid(100);
    }
    count
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
        assert_eq!(answer, 6);
    }
}
