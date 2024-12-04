package day03

import (
	"regexp"
	"strconv"
)

func PartOne(lines []string) string {
	result := 0

	for _, line := range lines {
		r := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
		for _, instruction := range r.FindAllStringSubmatch(line, -1) {
			a, _ := strconv.Atoi(instruction[1])
			b, _ := strconv.Atoi(instruction[2])
			result += a * b
		}
	}

	return strconv.Itoa(result)

}

func PartTwo(lines []string) string {
	resultTwo := 0

	enabled := true
	for _, line := range lines {
		r := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)`)
		for _, instruction := range r.FindAllStringSubmatch(line, -1) {
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

	return strconv.Itoa(resultTwo)
}
