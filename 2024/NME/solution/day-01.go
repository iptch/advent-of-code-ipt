package solution

import (
	"slices"
	"strconv"
	"strings"
)

// count number of elements in a slice
func count(slice []int, element int) int {
	count := 0
	for _, value := range slice {
		if value == element {
			count++
		}
	}
	return count
}

func parseDay01(lines []string) ([]int, []int) {
	var list1 []int
	var list2 []int

	for _, line := range lines {
		a := strings.Split(line, "   ")
		num1, _ := strconv.Atoi(a[0])
		num2, _ := strconv.Atoi(a[1])
		list1 = append(list1, num1)
		list2 = append(list2, num2)
	}

	return list1, list2
}

func (d Day01) PartOne(lines []string) string {
	list1, list2 := parseDay01(lines)

	slices.Sort(list1)
	slices.Sort(list2)

	var res = 0
	for i, numberList1 := range list1 {
		numberList2 := list2[i]
		diff := numberList1 - numberList2
		if diff < 0 {
			diff = numberList2 - numberList1
		}
		res += diff
	}

	return strconv.Itoa(res)
}

func (d Day01) PartTwo(lines []string) string {
	list1, list2 := parseDay01(lines)

	slices.Sort(list1)
	slices.Sort(list2)

	var res = 0
	for _, number := range list1 {
		res += count(list2, number) * number
	}
	return strconv.Itoa(res)
}
