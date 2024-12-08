use std::collections::HashMap;
use std::iter;
use std::str::FromStr;

struct Input(Vec<i32>, Vec<i32>);

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let strings: (Vec<&str>, Vec<&str>) = s.lines()
            .map(|l| l.split_whitespace())
            .map(|mut w| (w.next().unwrap(), w.next().unwrap()))
            .unzip();
        let left: Vec<i32> = strings.0.into_iter()
            .map(|l| l.parse().expect(&format!("Could not parse '{}'", l)))
            .collect();
        let right: Vec<i32> = strings.1.into_iter()
            .map(|l| l.parse().expect(&format!("Could not parse '{}'", l)))
            .collect();
        Ok(Input(left, right))
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let answer = puzzle_1(input.parse().unwrap());
    println!("The solution to part 1 is '{}'", answer);
    let answer = puzzle_2(input.parse().unwrap());
    println!("The solution to part 2 is '{}'", answer);
}

fn puzzle_1(mut input: Input) -> i32 {
    input.0.sort();
    input.1.sort();

    iter::zip(&input.0, &input.1)
        .map(|(l, r)| (l - r).abs())
        .sum()
}

fn puzzle_2(input: Input) -> i32 {
    let mut map: HashMap<i32, i32> = HashMap::new();
    input.1.into_iter().for_each(|x| {
        map.entry(x).and_modify(|e| *e += 1).or_insert(1);
    });
    input.0.into_iter()
        .map(|x| *map.entry(x).or_insert(0) * x)
        .sum()
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 11);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 31);
    }
}
