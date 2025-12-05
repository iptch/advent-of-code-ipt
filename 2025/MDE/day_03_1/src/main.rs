fn process_line(line_raw: &str) -> u32 {
    let line = line_raw.trim();
    let mut left = None;
    let mut left_idx = 0;
    for il in 0..line.len() - 1 {
        let c = line.chars().nth(il).unwrap().to_digit(10).unwrap();
        if left.is_none() || left.is_some() && left.unwrap() < c {
            left = Option::from(c);
            left_idx = il;
        }
    }

    let mut right = None;
    for ir in left_idx + 1..line.len() {
        let c = line.chars().nth(ir).unwrap().to_digit(10).unwrap();
        if right.is_none() || right.is_some() && right.unwrap() < c {
            right = Option::from(c);
        }
    }

    10 * left.unwrap() + right.unwrap()
}

fn main() {
    let mut joltage: u32 = 0;
    let mut input = String::new();

    loop {
        match std::io::stdin().read_line(&mut input) {
            Ok(n) => {
                if n == 0 {
                    break;
                }
                joltage += process_line(&input);
                input.clear();
            }
            Err(_) => {
                println!("failed to read line");
                break;
            }
        }
    }

    println!("total joltage: {} jolts", joltage);
}
