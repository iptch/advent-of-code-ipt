use std::{collections::HashMap, str::FromStr};

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

fn puzzle_1(input: Input, n: usize) -> i64 {
    let boxes = input.boxes;

    let mut connections = vec![];

    for i in 0..boxes.len() {
        for j in (i + 1)..boxes.len() {
            connections.push((&boxes[i], &boxes[j], dist(&boxes[i], &boxes[j])));
        }
    }
    connections.sort_by_key(|(_, _, dist)| *dist);

    let mut num_components: i32 = 0;
    let mut box_to_component: HashMap<&Box, i32> = HashMap::new();
    let mut component_to_boxes: HashMap<i32, Vec<&Box>> = HashMap::new();

    for i in 0..n {
        let (box1, box2, _) = connections[i];
        let box1_comp = box_to_component.get(box1);
        let box2_comp = box_to_component.get(box2);

        if let Some(comp1) = box1_comp
            && let Some(comp2) = box2_comp
        {
            if comp1 != comp2 {
                let comp = *comp1;
                let other_boxes = component_to_boxes.remove(comp2).unwrap();
                for b in other_boxes {
                    *box_to_component.get_mut(b).unwrap() = comp;
                    component_to_boxes.get_mut(&comp).unwrap().push(b);
                }
            }
        } else if let Some(comp1) = box1_comp {
            let comp = *comp1;
            box_to_component.insert(box2, comp);
            component_to_boxes.get_mut(&comp).unwrap().push(box2);
        } else if let Some(comp2) = box2_comp {
            let comp = *comp2;
            box_to_component.insert(box1, comp);
            component_to_boxes.get_mut(&comp).unwrap().push(box1);
        } else {
            let component = num_components;
            num_components += 1;
            box_to_component.insert(box1, component);
            box_to_component.insert(box2, component);
            component_to_boxes.insert(component, vec![box1, box2]);
        }
    }

    component_to_boxes
        .values()
        .map(|v| v.len() as i64)
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

    let mut connections = vec![];

    for i in 0..boxes.len() {
        for j in (i + 1)..boxes.len() {
            connections.push((&boxes[i], &boxes[j], dist(&boxes[i], &boxes[j])));
        }
    }
    connections.sort_by_key(|(_, _, dist)| *dist);

    let mut num_components: i32 = 0;
    let mut box_to_component: HashMap<&Box, i32> = HashMap::new();
    let mut component_to_boxes: HashMap<i32, Vec<&Box>> = HashMap::new();
    let mut largest_component: usize = 0;

    for (box1, box2, _) in connections {
        let box1_comp = box_to_component.get(box1);
        let box2_comp = box_to_component.get(box2);

        if let Some(comp1) = box1_comp
            && let Some(comp2) = box2_comp
        {
            if comp1 != comp2 {
                let comp = *comp1;
                let other_boxes = component_to_boxes.remove(comp2).unwrap();
                for b in other_boxes {
                    *box_to_component.get_mut(b).unwrap() = comp;
                    component_to_boxes.get_mut(&comp).unwrap().push(b);
                }
                largest_component =
                    largest_component.max(component_to_boxes.get_mut(&comp).unwrap().len())
            }
        } else if let Some(comp1) = box1_comp {
            let comp = *comp1;
            box_to_component.insert(box2, comp);
            component_to_boxes.get_mut(&comp).unwrap().push(box2);
            largest_component =
                largest_component.max(component_to_boxes.get_mut(&comp).unwrap().len())
        } else if let Some(comp2) = box2_comp {
            let comp = *comp2;
            box_to_component.insert(box1, comp);
            component_to_boxes.get_mut(&comp).unwrap().push(box1);
            largest_component =
                largest_component.max(component_to_boxes.get_mut(&comp).unwrap().len())
        } else {
            let component = num_components;
            num_components += 1;
            box_to_component.insert(box1, component);
            box_to_component.insert(box2, component);
            component_to_boxes.insert(component, vec![box1, box2]);
            largest_component = largest_component.max(2)
        }

        if largest_component == boxes.len() {
            return (box1.x as i64) * (box2.x as i64);
        }
    }
    unreachable!();
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
