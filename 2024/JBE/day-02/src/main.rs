use std::fs;

use std::str::FromStr;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-02/input.txt")?;
    let lines = parse(&content);
    let res_1 = part_1(&lines)?;
    let res_2 = part_2(&lines)?;
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(lines: &[Line]) -> Result<usize> {
    Ok(lines.iter().filter(|e| is_safe(&e.levels)).count())
}

fn is_safe(report: &[i32]) -> bool {
    let diffs = report.windows(2).map(|w| w[0] - w[1]);
    let positive = diffs.clone().filter(|e| *e > 0).count();
    if positive != 0 && positive != diffs.len() {
        return false;
    }
    diffs.map(|e| e.abs()).all(|e| e <= 3 && e >= 1)
}

fn part_2(lines: &[Line]) -> Result<usize> {
    Ok(lines
        .iter()
        .filter(|e| is_safe_with_dampener(&e.levels))
        .count())
}

fn is_safe_with_dampener(report: &[i32]) -> bool {
    for idx in 0..report.len() {
        let slice = [&report[..idx], &report[idx + 1..]].concat();
        if is_safe(&slice) {
            return true;
        }
    }
    false
}

fn parse(content: &str) -> Vec<Line> {
    content.lines().map(|l| l.parse().unwrap()).collect()
}

#[derive(Debug)]
struct Line {
    levels: Vec<i32>,
}

impl FromStr for Line {
    type Err = Box<dyn ::std::error::Error>;

    fn from_str(s: &str) -> Result<Line> {
        Ok(Line {
            levels: s.split(" ").map(|e| e.parse().unwrap()).collect(),
        })
    }
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let lines = parse(&content);
        let res = part_1(&lines)?;
        assert_eq!(2, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let lines = parse(&content);
        let res = part_2(&lines)?;
        assert_eq!(4, res);
        Ok(())
    }
}
