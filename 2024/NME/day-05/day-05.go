package day05

import (
	"strconv"
	"strings"
)

func isValidOrderingOrFix(rules [][]int, ordering []int) bool {
	var m = make(map[int]int)
	for i, v := range ordering {
		m[v] = i
	}

	ok := true
	for _, rule := range rules {
		first, second := rule[0], rule[1]

		idxFirst, hasFirst := m[first]
		idxSecond, hasSecond := m[second]

		if hasFirst && hasSecond && idxFirst > idxSecond {
			ordering[idxFirst], ordering[idxSecond] = ordering[idxSecond], ordering[idxFirst]
			m[first], m[second] = idxSecond, idxFirst
			ok = false
		}
	}

	if !ok {
		isValidOrderingOrFix(rules, ordering)
	}

	return ok
}

func parse(lines []string) ([][]int, [][]int) {
	var rules [][]int
	var orderings [][]int

	parsingRules := true
	for _, line := range lines {
		if parsingRules {
			if line == "" {
				parsingRules = false
			} else {
				page1, _ := strconv.Atoi(line[:2])
				page2, _ := strconv.Atoi(line[3:])
				rules = append(rules, []int{page1, page2})
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
	return rules, orderings
}

func PartOne(lines []string) string {
	rules, orderings := parse(lines)

	result := 0
	for _, ordering := range orderings {
		if isValidOrderingOrFix(rules, ordering) {
			result += ordering[len(ordering)/2]
		}
	}

	return strconv.Itoa(result)
}

func PartTwo(lines []string) string {
	rules, orderings := parse(lines)

	result := 0
	for _, ordering := range orderings {
		if !isValidOrderingOrFix(rules, ordering) {
			result += ordering[len(ordering)/2]
		}
	}

	return strconv.Itoa(result)
}
