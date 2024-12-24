#[macro_use]
extern crate lazy_static;
extern crate regex;

use std::fs;

use regex::Regex;

const A_COST: isize = 3;
const B_COST: isize = 1;
const OFFSET: isize = 10000000000000;

type Result<T> = ::std::result::Result<T, Box<dyn ::std::error::Error>>;

fn main() -> Result<()> {
    let content = fs::read_to_string("day-13/input.txt")?;
    let machines: Vec<Machine> = parse(&content).collect();
    let res_1 = part_1(&machines);
    let res_2 = part_2(&machines);
    println!("Part 1: {}", res_1);
    println!("Part 2: {}", res_2);
    Ok(())
}

fn part_1(machines: &[Machine]) -> isize {
    machines.iter().filter_map(|m| m.solve()).sum()
}

fn part_2(machines: &[Machine]) -> isize {
    machines
        .iter()
        .filter_map(|m| {
            let mut machine = m.clone();
            machine.p.x += OFFSET;
            machine.p.y += OFFSET;
            machine.solve()
        })
        .sum()
}

fn parse(content: &str) -> impl Iterator<Item = Machine> + '_ {
    lazy_static! {
        static ref RE: Regex = Regex::new(
            r"(?x)
            Button\sA:\sX\+(?P<ax>[0-9]+),\sY\+(?P<ay>[0-9]+)\n
            Button\sB:\sX\+(?P<bx>[0-9]+),\sY\+(?P<by>[0-9]+)\n
            Prize:\sX=(?P<px>[0-9]+),\sY=(?P<py>[0-9]+)"
        )
        .unwrap();
    }
    RE.captures_iter(content).map(|e| Machine {
        a: Vector {
            x: e["ax"].parse().unwrap(),
            y: e["ay"].parse().unwrap(),
        },
        b: Vector {
            x: e["bx"].parse().unwrap(),
            y: e["by"].parse().unwrap(),
        },
        p: Vector {
            x: e["px"].parse().unwrap(),
            y: e["py"].parse().unwrap(),
        },
    })
}

#[derive(Debug, Clone)]
struct Vector {
    x: isize,
    y: isize,
}

#[derive(Debug, Clone)]
struct Machine {
    a: Vector,
    b: Vector,
    p: Vector,
}

impl Machine {
    fn solve(&self) -> Option<isize> {
        let b = (self.a.x * self.p.y - self.a.y * self.p.x)
            / (self.b.y * self.a.x - self.b.x * self.a.y);
        let a = (self.p.x - b * self.b.x) / self.a.x;

        if self.p.x != a * self.a.x + b * self.b.x || self.p.y != a * self.a.y + b * self.b.y {
            None
        } else {
            Some(a * A_COST + b * B_COST)
        }
    }
}

#[cfg(test)]
mod test {
    use crate::*;

    #[test]
    fn test_example_part_1() -> Result<()> {
        let content = fs::read_to_string("example.txt")?;
        let machines: Vec<Machine> = parse(&content).collect();
        let res = part_1(&machines);
        assert_eq!(480, res);
        Ok(())
    }
}
