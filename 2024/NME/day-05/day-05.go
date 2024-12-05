package day05

import (
	"sort"
	"strconv"
	"strings"
)

type Rule struct {
	Before int
	After  int
}

func areEqual(slice1 []int, slice2 []int) bool {
	if len(slice1) != len(slice2) {
		return false
	}

	for i := 0; i < len(slice1); i++ {
		if slice1[i] != slice2[i] {
			return false
		}
	}
	return true
}

func isValidOrderingOrFix(rules map[Rule]struct{}, ordering []int) bool {
	original := make([]int, len(ordering))
	copy(original, ordering)

	sort.Slice(ordering, func(i, j int) bool {
		_, exists := rules[Rule{ordering[i], ordering[j]}]
		return exists
	})

	return areEqual(original, ordering)
}

func parse(lines []string) ([][]int, map[Rule]struct{}) {
	rules := make(map[Rule]struct{})
	var orderings [][]int

	parsingRules := true
	for _, line := range lines {
		if parsingRules {
			if line == "" {
				parsingRules = false
			} else {
				page1, _ := strconv.Atoi(line[:2])
				page2, _ := strconv.Atoi(line[3:])
				rules[Rule{page1, page2}] = struct{}{}
			}
		} else {
			var ordering []int
			for _, pageNumberString := range strings.Split(line, ",") {
				pageNumber, _ := strconv.Atoi(pageNumberString)
				ordering = append(ordering, pageNumber)
			}
			orderings = append(orderings, ordering)
		}
	}

	return orderings, rules
}

func PartOne(lines []string) string {
	orderings, rules := parse(lines)

	result := 0
	for _, ordering := range orderings {
		if isValidOrderingOrFix(rules, ordering) {
			result += ordering[len(ordering)/2]
		}
	}

	return strconv.Itoa(result)
}

func PartTwo(lines []string) string {
	orderings, rules := parse(lines)

	result := 0
	for _, ordering := range orderings {
		if !isValidOrderingOrFix(rules, ordering) {
			result += ordering[len(ordering)/2]
		}
	}

	return strconv.Itoa(result)
}
