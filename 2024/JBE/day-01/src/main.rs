use std::collections::HashMap;
use std::fs;

use std::str::FromStr;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-01/input.txt")?;
    let lines = parse(&content)?;
    let res_1 = part_1(&lines)?;
    let res_2 = part_2(&lines)?;
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(lines: &[Line]) -> Result<u32> {
    let mut first = Vec::new();
    let mut second = Vec::new();
    for line in lines {
        first.push(line.first);
        second.push(line.second);
    }
    first.sort();
    second.sort();
    let distance = first
        .iter()
        .zip(second.iter())
        .fold(0, |acc, (f, s)| acc + f.abs_diff(*s));
    Ok(distance)
}

fn part_2(lines: &[Line]) -> Result<u32> {
    let mut first = Vec::new();
    let mut second = HashMap::new();
    for line in lines {
        first.push(line.first);
        if let Some(x) = second.get_mut(&line.second) {
            *x = *x + 1;
        } else {
            second.insert(&line.second, 1);
        }
    }
    Ok(first
        .iter()
        .fold(0, |acc, e| acc + e * second.get(&e).unwrap_or(&0)))
}

fn parse(content: &str) -> Result<Vec<Line>> {
    content.lines().map(|l| l.parse()).collect()
}

#[derive(Debug)]
struct Line {
    first: u32,
    second: u32,
}

impl FromStr for Line {
    type Err = Box<dyn ::std::error::Error>;

    fn from_str(s: &str) -> Result<Line> {
        let mut parts = s.split("   ");
        Ok(Line {
            first: parts
                .next()
                .ok_or("failed to find first element")?
                .parse()?,
            second: parts
                .next()
                .ok_or("failed to find second element")?
                .parse()?,
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
        let res = part_1(&lines)?;
        assert_eq!(11, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let lines = parse(&content)?;
        let res = part_2(&lines)?;
        assert_eq!(31, res);
        Ok(())
    }
}
