use std::{collections::{HashMap, HashSet}, str::FromStr};

#[derive(Debug)]
struct Input {
    start: usize,
    map: Vec<Vec<bool>>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            start: raw_input.lines().next().unwrap().find('S').unwrap(),
            map: raw_input
                .lines()
                .map(|line| line.chars().map(|c| c == '^').collect())
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

    let mut beams = HashSet::new();
    beams.insert(input.start);

    for line in input.map {
        let mut split_beams = vec![];
        for beam in beams.iter() {
            if line[*beam] {
                split_beams.push(*beam);
            }
        }
        count += split_beams.len() as i32;
        for beam in split_beams.iter() {
            beams.remove(beam);
            beams.insert(beam - 1);
            beams.insert(beam + 1);
        }
    }

    count
}

fn puzzle_2(input: Input) -> i64 {
    let mut beams: HashMap<usize, i64> = HashMap::new();
    beams.insert(input.start, 1);

    for line in input.map {
        let mut split_beams = vec![];
        for (beam, _) in beams.iter() {
            if line[*beam] {
                split_beams.push(*beam);
            }
        }
        for beam in split_beams.iter() {
            let multipliciy = beams.remove(beam).unwrap();

            *beams.entry(*beam - 1).or_insert(0) += multipliciy;
            *beams.entry(*beam + 1).or_insert(0) += multipliciy;
        }
    }

    beams.values().sum()
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 21);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 40);
    }
}
