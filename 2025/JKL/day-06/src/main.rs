use std::str::FromStr;

#[derive(Debug)]
struct Input {
    columns: Vec<(Vec<i64>, String)>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        let num_columns = raw_input.lines().next().unwrap().split_whitespace().count();

        let lines: Vec<&str> = raw_input.lines().collect();
        let numbers = &lines[0..lines.len() - 1];
        let signs: Vec<String> = lines
            .last()
            .unwrap()
            .split_whitespace()
            .map(|sign| sign.to_string())
            .collect();

        let mut columns: Vec<Vec<i64>> = vec![vec![]; num_columns];

        for line in numbers.into_iter() {
            for (idx, val) in line.split_whitespace().enumerate() {
                columns[idx].push(val.parse().unwrap())
            }
        }

        Ok(Input {
            columns: columns.into_iter().zip(signs).collect(),
        })
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let answer = puzzle_1(input.parse().unwrap());
    println!("The solution to part 1 is '{}'", answer);
    let answer = puzzle_2(input);
    println!("The solution to part 2 is '{}'", answer);
}

fn puzzle_1(input: Input) -> i64 {
    input
        .columns
        .into_iter()
        .map(|(numbers, sign)| match sign.as_str() {
            "+" => numbers.iter().sum::<i64>(),
            "*" => numbers.iter().product(),
            _ => panic!(),
        })
        .sum()
}

fn puzzle_2(raw_input: &str) -> i64 {
    let mut matrix: Vec<Vec<char>> = raw_input
        .lines()
        .map(|line| line.chars().collect::<Vec<_>>())
        .collect();
    let len = matrix[0].len();
    matrix.insert(matrix.len() - 1, vec![' '; len]);

    let matrix = transpose(matrix);
    let lines: Vec<String> = matrix
        .into_iter()
        .map(|row| row.into_iter().collect())
        .collect();

    let mut total = 0_i64;
    let mut current = 0_i64;

    let mut multiply = false;

    for line in lines {
        let mut line = line.split_whitespace();
        if let Some(num) = line.next() {
            let num = num.parse().unwrap();
            if let Some(sign) = line.next() {
                multiply = match sign {
                    "+" => false,
                    "*" => true,
                    _ => panic!(),
                };
                total += current;
                current = num;
            } else {
                match multiply {
                    false => current += num,
                    true => current *= num,
                }
            }
        }
    }
    total += current;

    total
}

fn transpose(v: Vec<Vec<char>>) -> Vec<Vec<char>> {
    let len = v[0].len();
    let mut iters: Vec<_> = v.into_iter().map(|n| n.into_iter()).collect();
    (0..len)
        .map(|_| {
            iters
                .iter_mut()
                .map(|n| n.next().unwrap())
                .collect::<Vec<char>>()
        })
        .collect()
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 4277556);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT);
        assert_eq!(answer, 3263827);
    }
}
