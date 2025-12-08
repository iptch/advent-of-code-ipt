use std::str::FromStr;

#[derive(Debug)]
struct Input {}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        todo!("modify Input struct and implement parsing logic")
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
    todo!("implement part 1 solution")
}

fn puzzle_2(input: Input) -> i64 {
    todo!("implement part 2 solution")
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, todo!("replace with part 1 example solution"));
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, todo!("replace with path 2 example solution"));
    }
}
