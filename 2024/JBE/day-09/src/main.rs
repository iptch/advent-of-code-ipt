use std::collections::HashSet;
use std::fs;

use std::str::FromStr;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-09/input.txt")?;
    let lines = parse(&content)?;
    assert_eq!(1, lines.len());
    let res_1 = part_1(&lines[0]);
    let res_2 = part_2(&lines[0]);
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn score(pos: isize, file_id: isize, len: isize) -> isize {
    (0..len).fold(0, |acc, file_idx| acc + (pos + file_idx) * file_id)
}

// attempt solution that does not require more memory than the actual string being passed as input
fn part_1(line: &Line) -> isize {
    let mut consuming_file_idx = line.files.len() - 1;
    let mut consumed_file_len = 0;
    let mut position = 0;
    let mut sum = 0;
    for (idx, &(file_id, file_len, mut free_len)) in line.files.iter().enumerate() {
        // if overpassing files that have already been moved, stop
        if idx > consuming_file_idx {
            break;
        }
        // if viewing the remains of a file being moved, add score and finish
        if idx == consuming_file_idx {
            let length = file_len - consumed_file_len;
            sum = sum + score(position, file_id, length);
            break;
        }
        // add file hashsum
        sum = sum + score(position, file_id, file_len);
        position = position + file_len;
        // while there is free space, check end of fs to move files
        while free_len > 0 {
            let consuming_remaining_len = line.files[consuming_file_idx].1 - consumed_file_len;
            let file_id = line.files[consuming_file_idx].0;
            // remains of file fit into free space, move entire remains into free space and update
            // buffer pointers
            if consuming_remaining_len <= free_len {
                sum = sum + score(position, file_id, consuming_remaining_len);
                position = position + consuming_remaining_len;
                free_len = free_len - consuming_remaining_len;
                consumed_file_len = 0;
                consuming_file_idx = consuming_file_idx - 1;
                if consuming_file_idx == idx {
                    break;
                }
            } else {
                // else, add only part of the buffer and update pointers
                consumed_file_len = consumed_file_len + free_len;
                sum = sum + score(position, file_id, free_len);
                position = position + free_len;
                free_len = 0;
            }
        }
    }
    sum
}

fn part_2(line: &Line) -> isize {
    let mut seen = HashSet::new();
    let mut position = 0;
    let mut sum = 0;
    for &(file_id, file_len, mut free_len) in line.files.iter() {
        if !seen.contains(&file_id) {
            sum = sum + score(position, file_id, file_len);
            position = position + file_len;
            seen.insert(file_id);
        } else {
            position = position + file_len;
        }
        for &(file_id, file_len, _) in line.files.iter().rev() {
            if file_len <= free_len && !seen.contains(&file_id) {
                sum = sum + score(position, file_id, file_len);
                position = position + file_len;
                seen.insert(file_id);
                free_len = free_len - file_len;
            }
        }
        position = position + free_len;
    }
    sum
}

fn parse(content: &str) -> Result<Vec<Line>> {
    content.lines().map(|l| l.parse()).collect()
}

#[derive(Debug, Clone)]
struct Line {
    files: Vec<(isize, isize, isize)>,
}

impl FromStr for Line {
    type Err = Box<dyn ::std::error::Error>;

    fn from_str(s: &str) -> Result<Line> {
        let mut files = Vec::new();
        let chars: Vec<isize> = s.chars().map(|e| e.to_string().parse().unwrap()).collect();
        for chunk in chars.chunks(2).enumerate() {
            match chunk {
                (idx, &[first, second]) => files.push((idx as isize, first, second)),
                (idx, &[first]) => files.push((idx as isize, first, 0)),
                _ => {
                    return Err("chunk malformated".into());
                }
            }
        }
        Ok(Line { files })
    }
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let lines = parse(&content)?;
        let res = part_1(&lines[0]);
        assert_eq!(1928, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let lines = parse(&content)?;
        let res = part_2(&lines[0]);
        assert_eq!(2858, res);
        Ok(())
    }
}
