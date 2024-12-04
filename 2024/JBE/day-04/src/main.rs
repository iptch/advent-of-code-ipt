use std::fs;

const XMAS_WINDOW_SIZE: usize = 4;
const MAS_WINDOW_SIZE: usize = 3;
const BUFFER_CHAR: char = 'O';

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-04/input.txt")?;
    let grid = parse(&content);
    let res_1 = part_1(&grid)?;
    let res_2 = part_2(&grid)?;
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(grid: &Vec<Vec<char>>) -> Result<usize> {
    let mut input = grid.clone();
    add_margins(&mut input);
    let mut count = 0;
    for i in 0..input.len() - XMAS_WINDOW_SIZE + 1 {
        for j in 0..input[i].len() - XMAS_WINDOW_SIZE + 1 {
            let window = get_window_at(&input, &(i, j), XMAS_WINDOW_SIZE);
            count = count + count_xmas_in_window(&window);
        }
    }
    Ok(count)
}

fn part_2(grid: &Vec<Vec<char>>) -> Result<usize> {
    let mut count = 0;
    for i in 0..grid.len() - MAS_WINDOW_SIZE + 1 {
        for j in 0..grid[i].len() - MAS_WINDOW_SIZE + 1 {
            let window = get_window_at(&grid, &(i, j), MAS_WINDOW_SIZE);
            if is_mas_in_window(&window) {
                count = count + 1;
            }
        }
    }
    Ok(count)
}

fn get_window_at(grid: &Vec<Vec<char>>, position: &(usize, usize), size: usize) -> Vec<Vec<char>> {
    let &(i, j) = position;
    (i..i + size)
        .map(|idx_i| (j..j + size).map(|idx_j| grid[idx_i][idx_j]).collect())
        .collect()
}

fn count_xmas_in_window(window: &Vec<Vec<char>>) -> usize {
    let potentials: Vec<String> = vec![
        (0..XMAS_WINDOW_SIZE).map(|i| window[i][i]).collect(),
        (0..XMAS_WINDOW_SIZE)
            .map(|i| window[XMAS_WINDOW_SIZE - i - 1][i])
            .collect(),
        (0..XMAS_WINDOW_SIZE).map(|i| window[1][i]).collect(),
        (0..XMAS_WINDOW_SIZE).map(|i| window[i][1]).collect(),
    ];
    potentials.iter().filter(|e| is_xmas(&e)).count()
}

fn is_mas_in_window(window: &Vec<Vec<char>>) -> bool {
    is_mas(
        &(0..MAS_WINDOW_SIZE)
            .map(|i| window[i][i])
            .collect::<String>(),
    ) && is_mas(
        &(0..MAS_WINDOW_SIZE)
            .map(|i| window[MAS_WINDOW_SIZE - i - 1][i])
            .collect::<String>(),
    )
}

fn is_xmas(candidate: &str) -> bool {
    candidate == "XMAS" || candidate == "SAMX"
}

fn is_mas(candidate: &str) -> bool {
    candidate == "MAS" || candidate == "SAM"
}

fn add_margins(grid: &mut Vec<Vec<char>>) {
    for row in grid.iter_mut() {
        row.insert(0, BUFFER_CHAR);
        row.push(BUFFER_CHAR);
        row.push(BUFFER_CHAR);
    }
    let length = grid[0].len();
    grid.insert(0, vec![BUFFER_CHAR; length]);
    grid.push(vec![BUFFER_CHAR; length]);
    grid.push(vec![BUFFER_CHAR; length]);
}

fn parse(content: &str) -> Vec<Vec<char>> {
    content.lines().map(|l| l.chars().collect()).collect()
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_count_in_window() -> Result<()> {
        let content = "XMAS\nXMAS\nXMAS\nXMAS";
        let grid = parse(&content);
        let res = count_xmas_in_window(&grid);
        assert_eq!(3, res);
        let content = "XM0S\nXM0S\nXMAS\nXM0S";
        let grid = parse(&content);
        let res = count_xmas_in_window(&grid);
        assert_eq!(1, res);
        let content = "XM0S\nSAMX\nXM0S\nXM0S";
        let grid = parse(&content);
        let res = count_xmas_in_window(&grid);
        assert_eq!(1, res);
        let content = "XM0S\nXM0S\nXMAS\nXM00";
        let grid = parse(&content);
        let res = count_xmas_in_window(&grid);
        assert_eq!(0, res);
        Ok(())
    }

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example-1.txt")?;
        let grid = parse(&content);
        let res = part_1(&grid)?;
        assert_eq!(18, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example-2.txt")?;
        let grid = parse(&content);
        let res = part_2(&grid)?;
        assert_eq!(9, res);
        Ok(())
    }
}
