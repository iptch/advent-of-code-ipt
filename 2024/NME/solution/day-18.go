package solution

import (
	"container/heap"
	"fmt"
	"math"
	"regexp"
	"strconv"
)

const (
	SIZE       = 71
	BytesPart1 = 1024
)

func parseDay18(lines []string, numLinesToParse int) [][]bool {
	grid := make([][]bool, SIZE)
	for i := range grid {
		grid[i] = make([]bool, SIZE)
		for j := range grid[i] {
			grid[i][j] = false
		}
	}

	re := regexp.MustCompile("^([0-9]+),([0-9]+)$")
	for i := 0; i < numLinesToParse; i++ {
		matches := re.FindStringSubmatch(lines[i])
		x, _ := strconv.Atoi(matches[1])
		y, _ := strconv.Atoi(matches[2])
		grid[y][x] = true
	}

	return grid
}

func printBooleanGrid(grid [][]bool) {
	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] {
				fmt.Printf("#")
			} else {
				fmt.Printf(".")
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

func printDistanceGrid(grid [][]bool, distances [][]int) {
	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] {
				fmt.Printf(" ### ")
			} else if distances[i][j] == math.MaxInt {
				fmt.Printf("  -1 ")
			} else {
				fmt.Printf("%4d ", distances[i][j])
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

func shortestPath(grid [][]bool, start Coordinate2D, end Coordinate2D) int {
	distances := make([][]int, SIZE)
	for i := range distances {
		distances[i] = make([]int, SIZE)
		for j := range distances[i] {
			distances[i][j] = math.MaxInt
		}
	}

	h := &MinHeap{}
	heap.Init(h)

	distances[start.X][start.Y] = 0
	h.Push(Coordinate2DWithDistance{start, 0})

	for h.Len() > 0 {
		current := heap.Pop(h).(Coordinate2DWithDistance)
		d := current.Distance

		for _, neighbor := range current.Coordinates.Neighbors4() {
			if neighbor.OutOfBounds(SIZE, SIZE) == false &&
				grid[neighbor.X][neighbor.Y] == false &&
				distances[neighbor.X][neighbor.Y] > d+1 {
				distances[neighbor.X][neighbor.Y] = d + 1
				h.Push(Coordinate2DWithDistance{neighbor, d + 1})
			}
		}
	}

	return distances[end.X][end.Y]
}

func (d Day18) PartOne(lines []string) string {
	grid := parseDay18(lines, BytesPart1)
	result := shortestPath(grid,
		Coordinate2D{0, 0},
		Coordinate2D{SIZE - 1, SIZE - 1},
	)
	return strconv.Itoa(result)
}

func (d Day18) PartTwo(lines []string) string {
	mi := BytesPart1 + 1
	ma := len(lines) - 1
	for mi < ma {
		mid := (mi + ma) / 2
		grid := parseDay18(lines, mid)
		if shortestPath(grid, Coordinate2D{0, 0}, Coordinate2D{SIZE - 1, SIZE - 1}) == math.MaxInt {
			ma = mid
		} else {
			mi = mid + 1
		}
	}
	return lines[mi-1]
}
