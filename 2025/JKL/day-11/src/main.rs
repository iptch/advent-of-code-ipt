use std::{
    collections::{HashMap, HashSet},
    str::FromStr,
};

use petgraph::{algo::toposort, graph::DiGraph, Graph};

#[derive(Debug)]
struct Input {
    map: HashMap<String, Vec<String>>,
}

impl FromStr for Input {
    type Err = std::num::ParseIntError;
    fn from_str(raw_input: &str) -> Result<Self, Self::Err> {
        Ok(Input {
            map: raw_input
                .lines()
                .map(|l| l.split_once(":").unwrap())
                .map(|(from, to)| {
                    (
                        from.to_string(),
                        to[1..].split(" ").map(|s| s.to_string()).collect(),
                    )
                })
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
    num_paths(&input, "you".to_string(), "out".to_string())
}

fn num_paths(input: &Input, from: String, to: String) -> i64 {

    let mut g = DiGraph::<String, ()>::default();

    let mut nodes = HashMap::new();
    for node in input.map.keys() {
        nodes.insert(node.clone(), g.add_node(node.clone()));
    }
    for (u, vs) in &input.map {
        for v in vs {
            if !nodes.contains_key(v) {
                nodes.insert(v.clone(), g.add_node(v.clone()));
            }
            let u = nodes[u];
            let v = nodes[v];
            g.add_edge(u, v, ());
        }
    }

    let topo = toposort(&g, None).unwrap();

    let relevant_nodes: Vec<_> = topo.into_iter().skip_while(|node| *node != nodes[&from])
        .take_while(|node| *node != nodes[&to])
        .collect();

    let mut num_paths = HashMap::new();
    num_paths.insert(nodes[&from], 1_i64);

    for node in &relevant_nodes {
        let paths_to_node = num_paths.get(node).unwrap_or(&0).clone();
        for neighbor in g.neighbors(*node) {
            *num_paths.entry(neighbor).or_default() += paths_to_node;
        }
    }

    *num_paths.get(&nodes[&to]).unwrap_or(&0)
}


fn puzzle_2(input: Input) -> i64 {
    let dac_to_out = num_paths(&input, "dac".to_string(), "out".to_string());
    let fft_to_dac = num_paths(&input, "fft".to_string(), "dac".to_string());
    let svr_to_fft = num_paths(&input, "svr".to_string(), "fft".to_string());

    svr_to_fft * fft_to_dac * dac_to_out
}

#[cfg(test)]
mod test {
    use crate::{puzzle_1, puzzle_2};

    static INPUT1: &str = include_str!("../example.txt");
    static INPUT2: &str = include_str!("../example2.txt");

    #[test]
    fn test_puzzle_1() {
        let answer = puzzle_1(INPUT1.parse().unwrap());
        assert_eq!(answer, 5);
    }

    #[test]
    fn test_puzzle_2() {
        let answer = puzzle_2(INPUT2.parse().unwrap());
        assert_eq!(answer, 2);
    }
}
