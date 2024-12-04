#[macro_use]
extern crate lazy_static;
extern crate regex;

use std::fs;

use regex::Regex;
use std::str::FromStr;

const DO: &str = "do()";
const DONT: &str = "don't()";

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-03/input.txt")?;
    let lines = parse(&content)?;
    let res_1 = part_1(&lines)?;
    let res_2 = part_2(&content)?;
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(lines: &[Line]) -> Result<i32> {
    let sum = lines
        .iter()
        .map(|e| &e.values)
        .flatten()
        .fold(0, |acc, (f, s)| acc + f * s);
    Ok(sum)
}

fn part_2(content: &str) -> Result<i32> {
    let input = preprocess_input(content);
    let lines = parse(&input)?;
    part_1(&lines)
}

fn preprocess_input(input: &str) -> String {
    let do_len = DO.len();
    let dont_len = DONT.len();
    let mut haystack = input;
    let mut output = String::new();
    while haystack.len() > 0 {
        if let Some(stop) = haystack.find(DONT) {
            output.push_str(&haystack[..stop]);
            haystack = &haystack[stop + dont_len..];
            if let Some(start) = haystack.find(DO) {
                haystack = &haystack[start + do_len..];
            } else {
                return output;
            }
        } else {
            output.push_str(&haystack);
            return output;
        }
    }
    output
}

fn parse(content: &str) -> Result<Vec<Line>> {
    content.lines().map(|l| l.parse()).collect()
}

#[derive(Debug)]
struct Line {
    values: Vec<(i32, i32)>,
}

impl FromStr for Line {
    type Err = Box<dyn ::std::error::Error>;

    fn from_str(s: &str) -> Result<Line> {
        lazy_static! {
            static ref RE: Regex = Regex::new(
                r"(?x)
                mul\(
                (?P<first>[0-9]{1,3})
                ,
                (?P<second>[0-9]{1,3})
                \)"
            )
            .unwrap();
        }

        Ok(Line {
            values: RE
                .captures_iter(s)
                .map(|e| (e["first"].parse().unwrap(), e["second"].parse().unwrap()))
                .collect(),
        })
    }
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example-1.txt")?;
        let lines = parse(&content)?;
        let res = part_1(&lines)?;
        assert_eq!(161, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example-2.txt")?;
        let res = part_2(&content)?;
        assert_eq!(48, res);
        Ok(())
    }
}
