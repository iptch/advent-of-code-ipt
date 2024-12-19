package solution

import (
	"regexp"
	"strconv"
	"strings"
)

func parseDay19(lines []string) ([]string, []string) {
	regexTowels := regexp.MustCompile("[a-z]+")
	towels := regexTowels.FindAllString(lines[0], -1)
	patterns := lines[2:]
	return towels, patterns
}

func possibleBuildsMemo(towels []string, pattern string, idx int, memo map[int]int) int {
	_, exists := memo[idx]
	if exists == false {
		memo[idx] = possibleBuilds(towels, pattern, idx, memo)
	}
	return memo[idx]
}

func possibleBuilds(towels []string, pattern string, idx int, memo map[int]int) int {
	result := 0

	if idx >= len(pattern) {
		return 0
	}

	current := pattern[idx:]
	for _, towel := range towels {
		if towel == current {
			result++
		}

		if strings.HasPrefix(current, towel) {
			result += possibleBuildsMemo(towels, pattern, idx+len(towel), memo)
		}
	}

	return result
}

func (d Day19) PartOne(lines []string) string {
	towels, patterns := parseDay19(lines)

	result := 0
	for _, pattern := range patterns {
		if possibleBuilds(towels, pattern, 0, make(map[int]int)) > 0 {
			result++
		}
	}

	return strconv.Itoa(result)
}

func (d Day19) PartTwo(lines []string) string {
	towels, patterns := parseDay19(lines)

	result := 0
	for _, pattern := range patterns {
		result += possibleBuilds(towels, pattern, 0, make(map[int]int))
	}

	return strconv.Itoa(result)
}
