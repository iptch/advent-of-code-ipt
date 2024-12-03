package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	// read and parse input
	readFile, _ := os.Open("2024/NME/day-03/example2.txt")

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	resultOne := 0
	resultTwo := 0

	enabled := true
	for fileScanner.Scan() {
		line := fileScanner.Text()

		// part 1
		regexPart1 := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
		for _, instruction := range regexPart1.FindAllStringSubmatch(line, -1) {
			a, _ := strconv.Atoi(instruction[1])
			b, _ := strconv.Atoi(instruction[2])
			resultOne += a * b
		}

		// part 2
		regexPart2 := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)`)
		for _, instruction := range regexPart2.FindAllStringSubmatch(line, -1) {
			switch instruction[0] {
			case "do()":
				enabled = true
			case "don't()":
				enabled = false
			default:
				if enabled {
					a, _ := strconv.Atoi(instruction[1])
					b, _ := strconv.Atoi(instruction[2])
					resultTwo += a * b
				}
			}
		}

	}

	fmt.Println(resultOne)
	fmt.Println(resultTwo)

}
