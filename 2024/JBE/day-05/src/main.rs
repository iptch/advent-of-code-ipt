use std::fs;

use std::str::FromStr;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-05/input.txt")?;
    let (rules, updates) = parse(&content)?;
    let res_1 = part_1(&rules, &updates);
    let res_2 = part_2(&rules, &updates);
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(rules: &[OrderingRule], updates: &[Update]) -> usize {
    updates
        .iter()
        .filter(|update| rules.iter().all(|r| update.respects(r)))
        .fold(0, |acc, update| acc + update.get_middle())
}

fn part_2(rules: &[OrderingRule], updates: &[Update]) -> usize {
    let mut bad_updates: Vec<Update> = updates
        .iter()
        .filter(|update| !rules.iter().all(|r| update.respects(r)))
        .map(|e| e.clone())
        .collect();
    while bad_updates
        .iter()
        .any(|update| !rules.iter().all(|r| update.respects(r)))
    {
        for update in bad_updates.iter_mut() {
            rules.iter().for_each(|r| update.reorder(r));
        }
    }
    bad_updates
        .iter()
        .fold(0, |acc, update| acc + update.get_middle())
}

fn parse(content: &str) -> Result<(Vec<OrderingRule>, Vec<Update>)> {
    let lines = content.lines();
    let rules = lines
        .clone()
        .take_while(|e| *e != "")
        .map(|l| l.parse())
        .collect::<::std::result::Result<Vec<OrderingRule>, Box<dyn ::std::error::Error>>>()?;
    let updates = lines
        .skip_while(|e| *e != "")
        .skip(1)
        .map(|l| l.parse())
        .collect::<::std::result::Result<Vec<Update>, Box<dyn ::std::error::Error>>>()?;
    Ok((rules, updates))
}

#[derive(Debug)]
struct OrderingRule {
    before: usize,
    after: usize,
}

impl FromStr for OrderingRule {
    type Err = Box<dyn ::std::error::Error>;

    fn from_str(s: &str) -> Result<OrderingRule> {
        let mut parts = s.split("|");
        Ok(OrderingRule {
            before: parts.next().ok_or("did not find first entry")?.parse()?,
            after: parts.next().ok_or("did not find second entry")?.parse()?,
        })
    }
}

#[derive(Debug, Clone)]
struct Update {
    pages: Vec<usize>,
}

impl Update {
    fn respects(&self, rule: &OrderingRule) -> bool {
        let first_idx = self.pages.iter().position(|e| *e == rule.before);
        let second_idx = self.pages.iter().position(|e| *e == rule.after);
        if first_idx.is_none() || second_idx.is_none() {
            return true;
        }
        first_idx.unwrap() < second_idx.unwrap()
    }

    fn reorder(&mut self, rule: &OrderingRule) {
        if let Some(first_idx) = self.pages.iter().position(|e| *e == rule.before) {
            if let Some(second_idx) = self.pages.iter().position(|e| *e == rule.after) {
                if first_idx > second_idx {
                    let value = self.pages.remove(second_idx);
                    self.pages.insert(first_idx, value);
                }
            }
        }
    }

    fn get_middle(&self) -> usize {
        let len = self.pages.len();
        let middle = len.div_ceil(2) - 1;
        self.pages[middle]
    }
}

impl FromStr for Update {
    type Err = Box<dyn ::std::error::Error>;

    fn from_str(s: &str) -> Result<Update> {
        Ok(Update {
            pages: s
                .split(",")
                .map(|e| e.parse())
                .collect::<::std::result::Result<Vec<usize>, ::std::num::ParseIntError>>()?,
        })
    }
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_parse() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let (rules, updates) = parse(&content)?;
        assert_eq!(21, rules.len());
        assert_eq!(6, updates.len());
        Ok(())
    }

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let (rules, updates) = parse(&content)?;
        let res = part_1(&rules, &updates);
        assert_eq!(143, res);
        Ok(())
    }

    #[test]
    fn test_example_part_2() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let (rules, updates) = parse(&content)?;
        let res = part_2(&rules, &updates);
        assert_eq!(123, res);
        Ok(())
    }
}
