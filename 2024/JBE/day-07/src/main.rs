use std::fs;

use std::str::FromStr;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-07/input.txt")?;
    let lines = parse(&content)?;
    let res_1 = part_1(&lines);
    let res_2 = part_2(&lines);
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(lines: &[Line]) -> usize {
    lines
        .iter()
        .filter(|e| e.test(&[Op::Mul, Op::Add]))
        .map(|e| e.result)
        .reduce(|acc, e| acc + e)
        .unwrap_or_default()
}

fn part_2(lines: &[Line]) -> usize {
    lines
        .iter()
        .filter(|e| e.test(&[Op::Mul, Op::Add, Op::Concat]))
        .map(|e| e.result)
        .reduce(|acc, e| acc + e)
        .unwrap_or_default()
}

fn parse(content: &str) -> Result<Vec<Line>> {
    content.lines().map(|l| l.parse()).collect()
}

#[derive(Debug, Clone, Copy)]
enum Op {
    Mul,
    Add,
    Concat,
}

impl Op {
    fn apply(&self, a: usize, b: usize) -> usize {
        match self {
            Op::Add => a + b,
            Op::Mul => a * b,
            Op::Concat => {
                let val = format!("{}{}", a, b);
                val.parse().unwrap()
            }
        }
    }
}

#[derive(Debug)]
struct Line {
    result: usize,
    operands: Vec<usize>,
}

fn solve(line: &Line, tmp_result: usize, next_index: usize, ops: &[Op]) -> bool {
    if tmp_result == line.result && next_index == line.operands.len() {
        return true;
    }

    if tmp_result > line.result || next_index == line.operands.len() {
        return false;
    }

    let next_val = line.operands[next_index];
    ops.iter()
        .any(|op| solve(line, op.apply(tmp_result, next_val), next_index + 1, ops))
}

impl Line {
    fn test(&self, options: &[Op]) -> bool {
        solve(self, self.operands[0], 1, options)
    }
}

impl FromStr for Line {
    type Err = Box<dyn ::std::error::Error>;

    fn from_str(s: &str) -> Result<Line> {
        let mut parts = s.split(": ");
        Ok(Line {
            result: parts
                .next()
                .ok_or("failed to find first element")?
                .parse()?,
            operands: parts
                .next()
                .ok_or("failed to find second element")?
                .split(" ")
                .map(|e| e.parse())
                .collect::<::std::result::Result<Vec<usize>, ::std::num::ParseIntError>>()?,
        })
    }
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let lines = parse(&content)?;
        let res = part_1(&lines);
        assert_eq!(3749, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let lines = parse(&content)?;
        let res = part_2(&lines);
        assert_eq!(11387, res);
        Ok(())
    }
}
