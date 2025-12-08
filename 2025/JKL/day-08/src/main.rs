use std::{collections::BinaryHeap, str::FromStr};

use disjoint::DisjointSet;
use itertools::Itertools;

#[derive(Debug)]
struct Input {
    boxes: Vec<Box>,
}

#[derive(Debug, PartialEq, Eq, Hash)]
struct Box {
    x: i32,
    y: i32,
    z: i32,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            boxes: raw_input
                .lines()
                .map(|line| line.parse().unwrap())
                .collect(),
        })
    }
}

#[derive(Debug, Eq, PartialEq)]
struct Edge(usize, usize, i64);

impl Ord for Edge {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.2.cmp(&other.2)
    }
}

impl PartialOrd for Edge {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        self.2.partial_cmp(&other.2)
    }
}

impl FromStr for Box {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        let mut coords = raw_input.split(",");
        Ok(Box {
            x: coords.next().unwrap().parse()?,
            y: coords.next().unwrap().parse()?,
            z: coords.next().unwrap().parse()?,
        })
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let answer = puzzle_1(input.parse().unwrap(), 1000);
    println!("The solution to part 1 is '{}'", answer);
    let answer = puzzle_2(input.parse().unwrap());
    println!("The solution to part 2 is '{}'", answer);
}

fn puzzle_1(input: Input, iterations: usize) -> i64 {
    let boxes = input.boxes;
    let n = boxes.len();

    let mut connections = compute_edges(&boxes, n);
    let mut sets = DisjointSet::with_len(n);

    for _ in 0..iterations {
        let Edge(i, j, _) = connections.pop().unwrap();
        if !sets.is_joined(i, j) {
            sets.join(i, j);
        }
    }

    sets.sets()
        .into_iter()
        .map(|set| set.len() as i64)
        .sorted()
        .rev()
        .take(3)
        .product()
}

fn dist(box1: &Box, box2: &Box) -> i64 {
    let dx = (box1.x - box2.x) as i64;
    let dy = (box1.y - box2.y) as i64;
    let dz = (box1.z - box2.z) as i64;

    dx * dx + dy * dy + dz * dz
}

fn puzzle_2(input: Input) -> i64 {
    let boxes = input.boxes;
    let n = boxes.len();

    let mut connections = compute_edges(&boxes, n);
    let mut sets = DisjointSet::with_len(n);

    let mut num_joins: usize = 0;
    loop {
        let Edge(i, j, _) = connections.pop().unwrap();
        if !sets.is_joined(i, j) {
            num_joins += sets.join(i, j) as usize;
        }
        if num_joins == boxes.len() - 1 {
            return (boxes[i].x as i64) * (boxes[j].x as i64);
        }
    }
}

fn compute_edges(boxes: &Vec<Box>, n: usize) -> BinaryHeap<Edge> {
    let mut connections = BinaryHeap::with_capacity(n * (n-1));
    for i in 0..n {
        for j in (i + 1)..n {
            // BinaryHeap is a max heap thus we invert the distance
            connections.push(Edge(i, j, -dist(&boxes[i], &boxes[j])))
        }
    }
    connections
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap(), 10);
        assert_eq!(answer, 40);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 25272);
    }
}
