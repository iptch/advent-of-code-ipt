fn process_line(line_raw: &str) -> u64 {
    let mut joltage: u64 = 0;
    let mut start = 0;
    let line = line_raw.trim();
    for pos in 0..12 {
        let end = line.len() - 11 + pos;
        let mut max: Option<u64> = None;
        let mut max_index = start;
        for i in start..end {
            let c = line_raw.chars().nth(i).unwrap().to_digit(10).unwrap() as u64;
            if max.is_none() || max.unwrap() < c {
                max = Option::from(c);
                max_index = i;
            }
        }
        start = max_index + 1;
        joltage += max.unwrap() * 10_u64.pow((11 - pos) as u32)
    }
    joltage
}

fn main() {
    let mut joltage: u64 = 0;
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
