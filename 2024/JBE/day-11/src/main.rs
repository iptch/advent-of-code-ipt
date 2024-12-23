use std::collections::HashMap;
use std::fs;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-11/input.txt")?;
    let nums = parse(&content)?;
    let res_1 = part_1(&nums)?;
    let res_2 = part_2(&nums)?;
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(stones: &[usize]) -> Result<usize> {
    let mut cache = HashMap::new();
    stones
        .iter()
        .map(|stone| split(*stone, 0, &mut cache, 25))
        .sum()
}

fn part_2(stones: &[usize]) -> Result<usize> {
    let mut cache = HashMap::new();
    stones
        .iter()
        .map(|stone| split(*stone, 0, &mut cache, 75))
        .sum()
}

fn split(
    num: usize,
    level: usize,
    cache: &mut HashMap<usize, HashMap<usize, usize>>,
    stop: usize,
) -> Result<usize> {
    if level == stop {
        return Ok(1);
    }
    if let Some(num_cache) = cache.get(&num) {
        if let Some(val) = num_cache.get(&level) {
            return Ok(*val);
        }
    }
    let string = num.to_string();
    let res = match string.as_str() {
        "0" => split(1, level + 1, cache, stop)?,
        x if x.len() % 2 == 0 => {
            let (first, second) = string.split_at(string.len() / 2);
            split(first.parse()?, level + 1, cache, stop)?
                + split(second.parse()?, level + 1, cache, stop)?
        }
        _ => split(num * 2024, level + 1, cache, stop)?,
    };
    let num_cache = cache.entry(num).or_insert_with(|| HashMap::new());
    num_cache.insert(level, res);
    Ok(res)
}

fn parse(content: &str) -> ::std::result::Result<Vec<usize>, ::std::num::ParseIntError> {
    content.trim().split(" ").map(|e| e.parse()).collect()
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let lines = parse(&content)?;
        let res = part_1(&lines)?;
        assert_eq!(55312, res);
        Ok(())
    }
}
