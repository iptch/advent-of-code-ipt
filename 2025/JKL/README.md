# Jan's 2025 Advent of Code Solutions

## Run

From inside one of the `day-*/` directories:
```sh
# run on test input and compare against known solution
cargo test
# run on problem input and print result
cargo run
```

From root directory:
```sh
# run all tests for all days
cargo test
# run a specific days solution on the problem input
cargo run --bin day-XY
```

## Adding a Solution

> [!NOTE]
> In order to adhere to the [Advent of Code FAQ section on copying][aoc_faq_copying],
> the `input.txt` of the individual days is `.gitignore`d and should not be
> commited.

1. Make a copy of `template/` named `day-XY/`, it will automatically be part of
the cargo workspace
1. Fill the `example.txt` with the example input from AoC
1. Fill the `input.txt` with your personal problem input from AoC
1. Address `todo!("...")` in the code
   1. Set expected example outputs in tests
   2. Modify `Input` struct to match the problem and implement parsing logic
   3. Solve problems and implement solutions


[aoc_faq_copying]: https://adventofcode.com/2025/about#faq_copying
