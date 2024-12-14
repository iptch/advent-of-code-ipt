package solution

import (
	"strconv"
)

func checkChar(c uint8, i int, j int, lines []string) bool {
	if 0 > i || i >= len(lines) || 0 > j || j >= len(lines) {
		return false //out of bounds
	}

	return lines[i][j] == c
}

func findXMAS(i int, j int, lines []string) int {
	neighs := [][][]int{
		{{1, 0}, {2, 0}, {3, 0}},
		{{1, -1}, {2, -2}, {3, -3}},
		{{0, -1}, {0, -2}, {0, -3}},
		{{-1, -1}, {-2, -2}, {-3, -3}},
		{{-1, 0}, {-2, 0}, {-3, 0}},
		{{-1, 1}, {-2, 2}, {-3, 3}},
		{{0, 1}, {0, 2}, {0, 3}},
		{{1, 1}, {2, 2}, {3, 3}},
	}

	result := 0

	for _, sequence := range neighs {
		if checkChar('M', i+sequence[0][0], j+sequence[0][1], lines) &&
			checkChar('A', i+sequence[1][0], j+sequence[1][1], lines) &&
			checkChar('S', i+sequence[2][0], j+sequence[2][1], lines) {
			result++
		}
	}

	return result
}

func findMAS(i int, j int, lines []string) int {
	if 0 > i || i >= len(lines) || 0 > j || j >= len(lines) {
		return 0 //out of bounds
	}

	// first two are M, second two are S
	neighs := [][][]int{
		{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}},
		{{1, -1}, {-1, -1}, {-1, 1}, {1, 1}},
		{{-1, 1}, {-1, -1}, {1, 1}, {1, -1}},
		{{-1, 1}, {1, 1}, {-1, -1}, {1, -1}},
	}

	for _, sequence := range neighs {
		if checkChar('M', i+sequence[0][0], j+sequence[0][1], lines) &&
			checkChar('M', i+sequence[1][0], j+sequence[1][1], lines) &&
			checkChar('S', i+sequence[2][0], j+sequence[2][1], lines) &&
			checkChar('S', i+sequence[3][0], j+sequence[3][1], lines) {
			return 1
		}
	}
	return 0
}

func (d Day04) PartOne(lines []string) string {
	counter := 0
	for i, line := range lines {
		for j, c := range line {
			if c == 'X' {
				counter += findXMAS(i, j, lines)
			}
		}
	}

	return strconv.Itoa(counter)
}

func (d Day04) PartTwo(lines []string) string {
	counter := 0
	for i, line := range lines {
		for j, c := range line {
			if c == 'A' {
				counter += findMAS(i, j, lines)
			}
		}
	}
	return strconv.Itoa(counter)
}
