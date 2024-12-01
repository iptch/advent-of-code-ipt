package main

import (
	"bufio"
	"fmt"
	"os"
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

func main() {
	// read and parse input
	readFile, _ := os.Open("2024/NME/day-01/input.txt")

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	var list1 []int
	var list2 []int

	for fileScanner.Scan() {
		a := strings.Split(fileScanner.Text(), "   ")
		num1, _ := strconv.Atoi(a[0])
		num2, _ := strconv.Atoi(a[1])
		list1 = append(list1, num1)
		list2 = append(list2, num2)
	}

	// part 1
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
	fmt.Println(res)

	// part 2
	var res2 = 0
	for _, number := range list1 {
		res2 += count(list2, number) * number
	}
	fmt.Println(res2)
}
