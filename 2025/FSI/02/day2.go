package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func countDigits(n int) int {
	absN := math.Abs(float64(n))
	return int(math.Floor(math.Log10(absN))) + 1
}

func makeDuplicate(n int) int {
	var duplicate_n = n + n*(int(math.Pow10(countDigits(n))))
	return duplicate_n
}

func repeatN(num int, n int) int {
	var digits = countDigits(num)
	var repeated_num = num
	for ; n > 1; n-- {
		var factor int = int(math.Pow10(digits * (n - 1)))
		repeated_num += factor * num
	}
	return repeated_num
}

func getLeading(n int) int {
	var leading int = n / (int(math.Pow10((countDigits(n)) / 2)))
	return leading
}

func getLeadingN(num int, n int) int {
	var leading int = num / (int(math.Pow10((countDigits(num) - n))))
	return leading
}

func getSequenceLengths(n int) []int {
	var sequence_lengths []int

	for sl := 1; sl <= (n / 2); sl++ {
		if n%sl == 0 {
			sequence_lengths = append(sequence_lengths, sl)
		}
	}
	return sequence_lengths
}

func part1(filePath string) {
	bytes, err := os.ReadFile(filePath)
	check(err)
	content := string(bytes)

	ids := strings.Split(content, ",")
	var sum int = 0
	for _, id := range ids {
		id_first_last := strings.Split(id, "-")

		var start_str string = strings.TrimSpace(id_first_last[0])
		var end_str string = strings.TrimSpace(id_first_last[1])

		start, err := strconv.Atoi(start_str)
		check(err)
		end, err := strconv.Atoi(end_str)
		check(err)

		var startmod int = start
		if countDigits(start)%2 == 1 {
			startmod = int(math.Pow10(countDigits(start)))
		}

		var candidate int = makeDuplicate(getLeading(startmod))
		for candidate <= end {
			if candidate > start {
				sum += candidate
				fmt.Printf("start: %d candiate: %d end: %d\n", start, candidate, end)
			}
			candidate = makeDuplicate(getLeading(candidate) + 1)
		}
	}
	fmt.Println(sum)
}

func part2(filePath string) {
	bytes, err := os.ReadFile(filePath)
	check(err)
	content := string(bytes)

	ids := strings.Split(content, ",")
	var sum int = 0
	for _, id := range ids {
		id_first_last := strings.Split(id, "-")

		var start_str string = strings.TrimSpace(id_first_last[0])
		var end_str string = strings.TrimSpace(id_first_last[1])

		start, err := strconv.Atoi(start_str)
		check(err)
		end, err := strconv.Atoi(end_str)
		check(err)

		var _ = start
		var _ = end

		start_len := countDigits(start)
		end_len := countDigits(end)

		// fmt.Printf("23 repeated 3: %d\n", repeatN(23, 3))
		// fmt.Printf("123456 lead 3: %d\n", getLeadingN(123456, 1))
		//fmt.Printf("start: %d\n", start)
		for digits := start_len; digits <= end_len; digits++ {
			//fmt.Printf("start: %d, digits: %d\n", start, digits)
			var startmod = start
			if start_len < digits {
				startmod = int(math.Pow10(digits - 1))
				fmt.Printf("modified start from %d to %d\n", start, startmod)
			}

			seqlengths := getSequenceLengths(digits)
			//fmt.Println("seq: ", s			}
			intSet := make(map[int]struct{})
			var exists = struct{}{}
			for _, seqlen := range seqlengths {

				var candidate int = repeatN(getLeadingN(startmod, seqlen), digits/seqlen)

				for candidate <= end {
					if candidate >= start {
						// fmt.Printf("candidate for %d is %d\n", start, candidate)
						// sum += candidate
						intSet[candidate] = exists

					}
					candidate = repeatN(getLeadingN(candidate, seqlen)+1, digits/seqlen)
				}

			}

			for key, _ := range intSet {
				sum += key
				fmt.Printf("candidate for %d is %d\n", start, key)
			}

		}
	}
	fmt.Println(sum)
}

func main() {
	// part1("test.txt")
	// part1("input.txt")
	// part2("test.txt")
	part2("input.txt")

}
