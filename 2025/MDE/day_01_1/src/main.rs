use regex::Regex;
use std::io;
use std::ops::{Add, Sub};

fn process_line(line: &str, dial: &mut i32, re: &Regex) -> bool {
    println!("Dial value is {}", dial);
    let trimmed_line = line.trim();
    match re.captures(trimmed_line) {
        Some(m) => {
            let direction = &m[1];
            let distance = &m[2].parse::<i32>().unwrap();
            if direction.eq("L") {
                *dial = dial.sub(distance).rem_euclid(100);
            } else {
                *dial = dial.add(distance).rem_euclid(100);
            }
            *dial == 0
        }
        None => {
            panic!("Invalid line: {}", line);
        }
    }
}

fn main() {
    let re = Regex::new("^([LR])(\\d+)$").unwrap();
    let mut dial: i32 = 50;
    let mut input = String::new();
    let mut counter = 0;

    loop {
        input.clear();
        match io::stdin().read_line(&mut input) {
            Ok(n) => {
                if n == 0 {
                    break;
                }
                if process_line(&input, &mut dial, &re) {
                    counter += 1;
                }
            }
            Err(_) => {
                println!("Failed to read line!");
                break;
            }
        }
    }

    println!("Final counter value: {}", counter);
}
