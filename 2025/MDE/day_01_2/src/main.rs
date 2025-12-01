use regex::Regex;
use std::io;
use std::ops::Div;

fn process_line(line: &str, dial: &mut i32, re: &Regex) -> i32 {
    let trimmed_line = line.trim();
    match re.captures(trimmed_line) {
        Some(m) => {
            let n = 100;
            let direction = if m[1].eq("L") { -1 } else { 1 };
            let distance = &m[2].parse::<i32>().unwrap();

            // Left and right margins until zero position
            let p = *dial;
            // Special case: When dial is at zero, both left and right margins are 100
            let ml = if p == 0 { n } else { p };
            let mr = n - p;

            // Advance the dial
            *dial = (*dial + distance * direction).rem_euclid(n);

            let m = distance.rem_euclid(n);
            let x = if direction == 1 && m >= mr || direction == -1 && m >= ml {
                1
            } else {
                0
            };

            (distance.div(n)) + x
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
                let zero_crossings = process_line(&input, &mut dial, &re);

                counter += zero_crossings
            }
            Err(_) => {
                println!("Failed to read line!");
                break;
            }
        }
    }

    println!("Final counter value: {}", counter);
}
