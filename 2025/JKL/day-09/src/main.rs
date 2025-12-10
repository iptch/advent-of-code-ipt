use std::str::FromStr;

#[derive(Debug)]
struct Input {
    red_tiles: Vec<(i64, i64)>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            red_tiles: raw_input
                .lines()
                .map(|line| line.split_once(",").unwrap())
                .map(|(x, y)| (x.parse().unwrap(), y.parse().unwrap()))
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

fn puzzle_1(input: Input) -> i64 {
    let mut max = 0;
    for tile1 in input.red_tiles.iter() {
        for tile2 in input.red_tiles.iter() {
            max = i64::max(max, area(&tile1, &tile2));
        }
    }
    max
}

fn area(tile1: &(i64, i64), tile2: &(i64, i64)) -> i64 {
    let (x1, y1) = tile1;
    let (x2, y2) = tile2;
    ((x1.abs_diff(*x2) + 1) * (y1.abs_diff(*y2) + 1)) as i64
}

fn puzzle_2(input: Input) -> i64 {
    let tiles = input.red_tiles;
    let mut max = 0;
    for tile1 in tiles.iter() {
        for tile2 in tiles.iter() {
            let mut last = &tiles[tiles.len() - 1];
            let mut intersects = false;
            for i in 0..tiles.len() {
                let current = &tiles[i];
                if rectancle_intersects_line(tile1, tile2, current, last) {
                    intersects = true;
                    break;
                }
                last = current;
            }
            if !intersects {
                max = i64::max(max, area(&tile1, &tile2));
            }
        }
    }
    max
}

fn rectancle_intersects_line(
    x1: &(i64, i64),
    x2: &(i64, i64),
    l1: &(i64, i64),
    l2: &(i64, i64),
) -> bool {
    let (x1, y1) = x1;
    let (x2, y2) = x2;
    let x_min = i64::min(*x1, *x2);
    let x_max = i64::max(*x1, *x2);
    let y_min = i64::min(*y1, *y2);
    let y_max = i64::max(*y1, *y2);

    if l1.0 == l2.0 && x_min < l1.0 && l1.0 < x_max {
        return !((l1.1 <= y_min && l2.1 <= y_min) || (l1.1 >= y_max && l2.1 >= y_max));
    } else if l1.1 == l2.1 && y_min < l1.1 && l1.1 < y_max {
        return !((l1.0 <= x_min && l2.0 <= x_min) || (l1.0 >= x_max && l2.0 >= x_max));
    }
    false
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 50);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 24);
    }
}
