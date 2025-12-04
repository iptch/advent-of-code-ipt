package main

import (
	"bufio"
	"fmt"
	"os"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readInput(path string) [][]int {
	file, err := os.Open(path)
	check(err)
	defer file.Close()
	scanner := bufio.NewScanner(file)

	inputMap := make([][]int, 0, 200)

	var rowidx int = 0
	for scanner.Scan() {
		var row string = scanner.Text()

		inputMap = append(inputMap, make([]int, len(row)))

		for colidx, ch := range row {
			if ch == '.' {
				inputMap[rowidx][colidx] = 0
			} else {
				inputMap[rowidx][colidx] = 1
			}
		}
		rowidx++
	}
	return inputMap
}

func part1(path string) {
	inputMap := readInput(path)

	minRow := 0
	maxRow := len(inputMap)
	minCol := 0
	maxCol := len(inputMap[0])

	neighboursN := make([][]int, maxRow)
	for r := range neighboursN {
		neighboursN[r] = make([]int, maxCol)
		for c := range neighboursN[0] {
			// empty spaces are 20
			neighboursN[r][c] = +20 - 20*inputMap[r][c]
		}
	}

	for row := range inputMap {
		for col := range inputMap[0] {
			if inputMap[row][col] == 1 {
				for drow := -1; drow <= 1; drow++ {
					for dcol := -1; dcol <= 1; dcol++ {
						crow := row + drow
						ccol := col + dcol
						if minRow <= crow && crow < maxRow && minCol <= ccol && ccol < maxCol && (ccol != col || crow != row) {
							neighboursN[crow][ccol]++
						}
					}
				}
			}
		}
	}

	var goodPlaces int = 0
	for r := range neighboursN {
		for c := range neighboursN[0] {
			if neighboursN[r][c] < 4 {
				goodPlaces++
			}
		}
	}

	fmt.Println(inputMap)
	fmt.Println(neighboursN)
	fmt.Println(goodPlaces)

}

func part2(path string) {
	inputMap := readInput(path)

	minRow := 0
	maxRow := len(inputMap)
	minCol := 0
	maxCol := len(inputMap[0])

	var totalGoodPlaces int = 0
	var goodPlaces int = 1
	for goodPlaces > 0 {

		neighboursN := make([][]int, maxRow)
		for r := range neighboursN {
			neighboursN[r] = make([]int, maxCol)
			for c := range neighboursN[0] {
				// empty spaces are 20
				neighboursN[r][c] = +20 - 20*inputMap[r][c]
			}
		}

		for row := range inputMap {
			for col := range inputMap[0] {
				if inputMap[row][col] == 1 {
					for drow := -1; drow <= 1; drow++ {
						for dcol := -1; dcol <= 1; dcol++ {
							crow := row + drow
							ccol := col + dcol
							if minRow <= crow && crow < maxRow && minCol <= ccol && ccol < maxCol && (ccol != col || crow != row) {
								neighboursN[crow][ccol]++
							}
						}
					}
				}
			}
		}

		goodPlaces = 0
		for r := range neighboursN {
			for c := range neighboursN[0] {
				if neighboursN[r][c] < 4 {
					goodPlaces++
					inputMap[r][c] = 0
				}
			}
		}
		totalGoodPlaces += goodPlaces
	}
	fmt.Println(totalGoodPlaces)
}

func main() {
	// part1("input.txt")
	part2("input.txt")
}
