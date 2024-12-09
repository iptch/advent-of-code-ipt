use regex::Regex;
use std::str::FromStr;

#[derive(Debug)]
struct Input {
    instructions: Vec<Instruction>,
}

#[derive(Debug)]
enum Instruction {
    Mul(i32, i32),
    Do(),
    Dont(),
}

trait Compute {
    fn compute(&self) -> i32;
}

impl Compute for Instruction {
    fn compute(&self) -> i32 {
        match self {
            Instruction::Mul(x, y) => x * y,
            _ => 0,
        }
    }
}

impl FromStr for Instruction {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match &s[..3] {
            "mul" => {
                let mut it = s
                    .strip_prefix("mul(")
                    .unwrap()
                    .strip_suffix(")")
                    .unwrap()
                    .split(",");
                let lhs = it.next().unwrap().parse::<i32>()?;
                let rhs = it.next().unwrap().parse::<i32>()?;
                Ok(Self::Mul(lhs, rhs))
            }
            "do(" => Ok(Self::Do()),
            "don" => Ok(Self::Dont()),
            _ => panic!("Unexpected instruction: {}", s),
        }
    }
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        let expression = Regex::new(r"mul\(\d+,\d+\)|do\(\)|don't\(\)").unwrap();
        Ok(Input {
            instructions: expression
                .find_iter(raw_input)
                .map(|instr| instr.as_str().parse().unwrap())
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
    input.instructions.iter().map(|inst| inst.compute()).sum()
}

fn puzzle_2(input: Input) -> i32 {
    input
        .instructions
        .iter()
        .fold((0, true), |acc, instr| match (instr, acc.1) {
            (Instruction::Do(), _) => (acc.0, true),
            (Instruction::Dont(), _) => (acc.0, false),
            (Instruction::Mul(_, _), true) => (acc.0 + instr.compute(), true),
            _ => acc,
        })
        .0
}

#[cfg(test)]
mod test_day_03 {
    use crate::{puzzle_1, puzzle_2};

    #[test]
    fn test_puzzle_1() {
        let input = include_str!("../example_1.txt");
        let answer = puzzle_1(input.parse().unwrap());
        assert_eq!(answer, 161);
    }

    #[test]
    fn test_puzzle_2() {
        let input = include_str!("../example_2.txt");
        let answer = puzzle_2(input.parse().unwrap());
        assert_eq!(answer, 48);
    }
}
