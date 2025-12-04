package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func setSlice(sl *[]int, setlen int, set int) {
	for i := (len(*sl) - setlen); i < len(*sl); i++ {
		(*sl)[i] = set
	}
}

func getMaxJoltage(batteries []int, batN int) int {
	var _ = batN

	max_candidates := make([]int, batN)
	setSlice(&max_candidates, batN, -10)

	for bindex, el := range batteries {
		for cindex, candidate := range max_candidates {
			if el > candidate && ((len(batteries) - bindex) >= (batN - cindex)) {
				max_candidates[cindex] = el
				// reset following fields
				setSlice(&max_candidates, batN-cindex-1, -10)
				break
			}
		}
	}

	var joltage int = 0
	for cindex, candidate := range max_candidates {
		joltage += candidate * int(math.Pow10(batN-cindex-1))
	}

	return joltage
}

func part(filepath string, batN int) {
	file, err := os.Open(filepath)
	check(err)

	defer file.Close()
	scanner := bufio.NewScanner(file)

	var combinedJoltage = 0
	for scanner.Scan() {
		var batteries_str string = scanner.Text()

		var batteries []int
		for _, ch := range batteries_str {
			battery, err := strconv.Atoi(string(ch))
			check(err)
			batteries = append(batteries, battery)
		}

		var joltage = getMaxJoltage(batteries, batN)
		fmt.Printf("joltage: %d\n", joltage)
		combinedJoltage += joltage
	}
	fmt.Printf("combinedJoltage: %d", combinedJoltage)
}

func main() {

	// part("test.txt", 2) // part 1
	// part("input.txt", 2) // part 1
	// part("test.txt", 12) // part 2
	part("input.txt", 12) // part 2
}
