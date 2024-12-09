use std::str::FromStr;

struct Input {}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(Input {})
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
    todo!()
}

fn puzzle_2(input: Input) -> i32 {
    todo!()
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, todo!());
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, todo!());
    }
}
