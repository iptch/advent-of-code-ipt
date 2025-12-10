use std::{collections::HashSet, str::FromStr};

use microlp::{ComparisonOp, OptimizationDirection, Problem};
use petgraph::{
    algo::dijkstra,
    graph::{UnGraph, node_index},
};

#[derive(Debug)]
struct Input {
    configs: Vec<Config>,
}

#[derive(Debug)]
struct Config {
    target_state: Vec<bool>,
    buttons: Vec<Vec<i64>>,
    joltage: Vec<i64>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            configs: raw_input
                .lines()
                .map(|line| line.parse().unwrap())
                .collect(),
        })
    }
}

impl FromStr for Config {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        let bracket = raw_input.find("]").unwrap();
        let curley = raw_input.find("{").unwrap();

        let target_state = &raw_input[1..bracket];
        let buttons = &raw_input[(bracket + 2)..(curley - 1)];
        let joltage = &raw_input[(curley + 1)..(raw_input.len() - 1)];

        Ok(Config {
            target_state: target_state.chars().map(|c| c == '#').collect(),
            buttons: buttons
                .split(" ")
                .map(|button| {
                    button[1..(button.len() - 1)]
                        .split(",")
                        .map(|b| b.parse().unwrap())
                        .collect()
                })
                .collect(),
            joltage: joltage.split(",").map(|j| j.parse().unwrap()).collect(),
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
    input.configs.into_iter().map(sub_puzzle_1).sum()
}

fn sub_puzzle_1(config: Config) -> i64 {
    let switches: Vec<u32> = config
        .buttons
        .iter()
        .map(|b| b.iter().map(|w| 1_u32 << w).sum())
        .collect();

    let bits = config.target_state.len() as u32;
    let max_node = 2_u32.pow(bits);

    let mut g = UnGraph::<String, String>::default();

    let mut edges: HashSet<(u32, u32, String)> = HashSet::default();
    for u in 0..max_node {
        g.add_node(format!("{u} {u:0bits$b}", bits = (bits as usize)));
        for (idx, switch) in switches.iter().enumerate() {
            let v = u ^ switch;
            edges.insert((u.min(v), u.max(v), format!("{:?}", config.buttons[idx])));
        }
    }

    g.extend_with_edges(edges);

    let target = config
        .target_state
        .iter()
        .rfold(0_usize, |acc, b| (acc << 1) + *b as usize);

    let start = node_index(0);
    let goal = node_index(target);

    let distance = dijkstra(&g, start, Some(goal), |_| 1);

    distance[&goal] as i64
}

fn puzzle_2(input: Input) -> i64 {
    input.configs.into_iter().map(sub_puzzle_2).sum()
}

fn sub_puzzle_2(config: Config) -> i64 {
    let num_vars = config.buttons.len();
    let num_constraints = config.joltage.len();

    let mut problem = Problem::new(OptimizationDirection::Minimize);

    let x: Vec<_> = (0..config.buttons.len())
        .map(|_| problem.add_integer_var(1.0, (0, i32::MAX)))
        .collect();

    let mut matrix = vec![vec![false; num_vars]; num_constraints];

    for (j, button) in config.buttons.into_iter().enumerate() {
        for i in button {
            matrix[i as usize][j] = true;
        }
    }

    for (row, jolt) in matrix.into_iter().zip(config.joltage.into_iter()) {
        problem.add_constraint(
            row.into_iter()
                .zip(x.iter())
                .filter(|(a, _)| *a)
                .map(|(_, &x)| (x, 1.0)),
            ComparisonOp::Eq,
            jolt as f64,
        );
    }

    let solution = problem.solve().unwrap();

    solution.objective().round() as i64
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT: &str = include_str!("../example.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT.parse().unwrap());
        assert_eq!(answer, 7);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT.parse().unwrap());
        assert_eq!(answer, 33);
    }
}
