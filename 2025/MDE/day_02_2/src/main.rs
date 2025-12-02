#[derive(Debug)]
struct Range {
    from: u64,
    to: u64,
}

fn consists_of_repetitions(id: &str, s: usize) -> bool {
    let mut previous_slice: Option<&str> = None;
    let slice_size = id.len() / s;
    for slice_idx in 0..s {
        let slice = &id[slice_idx * slice_size..(slice_idx + 1) * slice_size];
        if previous_slice.is_some() && !previous_slice.eq(&Option::from(slice)) {
            return false;
        }
        previous_slice = Option::from(slice);
    }

    true
}

fn is_invalid(n: u64) -> bool {
    let n_str = n.to_string();

    for s in 2..n_str.len() + 1 {
        if n_str.len() % s == 0 {
            if consists_of_repetitions(&n_str, s) {
                return true;
            }
        }
    }

    false
}

fn sum_invalid_ids(range: &Range) -> u64 {
    let mut sum = 0;
    for n in range.from..range.to + 1 {
        if is_invalid(n) {
            sum += n
        }
    }

    sum
}

fn parse_line(line: &String) {
    let str_ranges: Vec<&str> = line.split(",").collect();
    println!("str_ranges: {:?}", str_ranges);
    let mut invalid_id_sum = 0;
    for str_range in str_ranges {
        let range_limits: Vec<&str> = str_range.split("-").collect();
        let range = Range {
            from: range_limits[0].parse().unwrap(),
            to: range_limits[1].parse().unwrap(),
        };
        println!("range: {:?}", range);
        invalid_id_sum += sum_invalid_ids(&range);
    }
    println!("Sum of invalid IDs: {}", invalid_id_sum);
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    parse_line(&input);
}
