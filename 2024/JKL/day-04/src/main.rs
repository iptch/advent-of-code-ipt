use itertools::Itertools;
use std::str::FromStr;

#[derive(Debug)]
struct Input {
    matrix: Vec<Vec<char>>,
}

static XMAS: [char; 4] = ['X', 'M', 'A', 'S'];
static SAMX: [char; 4] = ['S', 'A', 'M', 'X'];

static STENCILS: [[(usize, usize, char); 5]; 4] = [
    [
        (0, 0, 'M'),
        (2, 0, 'M'),
        (1, 1, 'A'),
        (0, 2, 'S'),
        (2, 2, 'S'),
    ],
    [
        (0, 0, 'M'),
        (2, 0, 'S'),
        (1, 1, 'A'),
        (0, 2, 'M'),
        (2, 2, 'S'),
    ],
    [
        (0, 0, 'S'),
        (2, 0, 'M'),
        (1, 1, 'A'),
        (0, 2, 'S'),
        (2, 2, 'M'),
    ],
    [
        (0, 0, 'S'),
        (2, 0, 'S'),
        (1, 1, 'A'),
        (0, 2, 'M'),
        (2, 2, 'M'),
    ],
];

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            matrix: s.lines().map(|line| line.chars().collect()).collect(),
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
    let rows = input.matrix.len();
    let cols = input.matrix[0].len();

    let len = XMAS.len();

    let down: i32 = (0..=rows - len)
        .cartesian_product(0..cols)
        .map(|(row, col)| {
            (0..4).all(|idx| input.matrix[row + idx][col] == XMAS[idx]) as i32
                + (0..4).all(|idx| input.matrix[row + idx][col] == SAMX[idx]) as i32
        })
        .sum();
    let right: i32 = (0..rows)
        .cartesian_product(0..=cols - len)
        .map(|(row, col)| {
            (0..4).all(|idx| input.matrix[row][col + idx] == XMAS[idx]) as i32
                + (0..4).all(|idx| input.matrix[row][col + idx] == SAMX[idx]) as i32
        })
        .sum();
    let diag_down: i32 = (0..=rows - len)
        .cartesian_product(0..=cols - len)
        .map(|(row, col)| {
            (0..4).all(|idx| input.matrix[row + idx][col + idx] == XMAS[idx]) as i32
                + (0..4).all(|idx| input.matrix[row + idx][col + idx] == SAMX[idx]) as i32
        })
        .sum();
    let diag_up: i32 = (3..rows)
        .cartesian_product(0..=cols - len)
        .map(|(row, col)| {
            (0..4).all(|idx| input.matrix[row - idx][col + idx] == XMAS[idx]) as i32
                + (0..4).all(|idx| input.matrix[row - idx][col + idx] == SAMX[idx]) as i32
        })
        .sum();
    down + right + diag_down + diag_up
}

fn puzzle_2(input: Input) -> i32 {
    let rows = input.matrix.len();
    let cols = input.matrix[0].len();

    (0..=rows - 3)
        .cartesian_product(0..=cols - 3)
        .map(|(row, col)| {
            STENCILS
                .into_iter()
                .filter(|stencil| {
                    stencil
                        .into_iter()
                        .all(|(i, j, c)| input.matrix[row + i][col + j].eq(c))
                })
                .count() as i32
        })
        .sum()
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 18);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 9);
    }
}
