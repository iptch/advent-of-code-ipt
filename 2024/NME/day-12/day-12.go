package day12

import (
	"container/list"
	"strconv"
)

type Coordinate struct {
	X, Y int
}

func computeRegionPrice(x int, y int, visited map[Coordinate]bool, lines []string) int {
	area := 0
	perimeter := 0

	queue := list.New()
	queue.PushBack(Coordinate{x, y})
	visited[Coordinate{x, y}] = true
	crop := lines[x][y]

	neighborVectors := [][]int{
		{1, 0}, {0, 1}, {-1, 0}, {0, -1},
	}
	for queue.Len() > 0 {
		front := queue.Front()
		queue.Remove(front)

		area++
		currentPosition := front.Value.(Coordinate)
		for _, neighborVector := range neighborVectors {
			a, b := neighborVector[0]+currentPosition.X, neighborVector[1]+currentPosition.Y
			if a < 0 || b < 0 || a >= len(lines) || b >= len(lines) {
				perimeter++
			} else {
				if lines[a][b] == crop {
					_, neighborVisited := visited[Coordinate{a, b}]
					if !neighborVisited {
						queue.PushBack(Coordinate{a, b})
						visited[Coordinate{a, b}] = true
					}
				} else {
					perimeter++
				}
			}
		}
	}

	return area * perimeter
}

func computeRegionPricePart2(x int, y int, visited map[Coordinate]bool, lines [][]rune) int {
	area := 0
	perimeter := 0

	queue := list.New()
	queue.PushBack(Coordinate{x, y})
	visited[Coordinate{x, y}] = true
	crop := lines[x][y]

	neighborVectors := [][]int{
		{1, 0}, {0, 1}, {-1, 0}, {0, -1},
		{1, 1}, {1, -1}, {-1, 1}, {-1, -1},
	}

	for queue.Len() > 0 {
		front := queue.Front()
		queue.Remove(front)

		area++
		currentPosition := front.Value.(Coordinate)
		differentNeighbors := 0
		for i, neighborVector := range neighborVectors {
			a, b := neighborVector[0]+currentPosition.X, neighborVector[1]+currentPosition.Y
			if a < 0 || b < 0 || a >= len(lines) || b >= len(lines) {
				differentNeighbors++
			} else {
				if lines[a][b] == crop {
					_, neighborVisited := visited[Coordinate{a, b}]
					// i<4 makes it so that we only take into account up,down,left,right neighbors, not diagonal ones.
					// Depends on the order of elements in neighborVectors
					if !neighborVisited && i < 4 {
						queue.PushBack(Coordinate{a, b})
						visited[Coordinate{a, b}] = true
					}
				} else {
					differentNeighbors++
				}
			}
		}

		if differentNeighbors == 1 || differentNeighbors == 4 || differentNeighbors == 5 {
			perimeter++
		}
	}
	return area / 4 * perimeter
}

func PartOne(lines []string) string {
	visited := map[Coordinate]bool{}
	result := 0
	for i, line := range lines {
		for j, _ := range line {
			_, isVisited := visited[Coordinate{i, j}]
			if !isVisited {
				result += computeRegionPrice(i, j, visited, lines)
			}
		}
	}
	return strconv.Itoa(result)
}

func double(lines []string) [][]rune {
	result := make([][]rune, len(lines)*2)
	for i, line := range lines {
		result[2*i] = make([]rune, len(line)*2)
		result[2*i+1] = make([]rune, len(line)*2)
		for j, char := range line {
			result[2*i][2*j] = char
			result[2*i+1][2*j] = char
			result[2*i][2*j+1] = char
			result[2*i+1][2*j+1] = char
		}
	}
	return result
}

func PartTwo(lines []string) string {
	doubledLines := double(lines)
	visited := map[Coordinate]bool{}
	result := 0
	for i, line := range doubledLines {
		for j, _ := range line {
			_, isVisited := visited[Coordinate{i, j}]
			if !isVisited {
				result += computeRegionPricePart2(i, j, visited, doubledLines)
			}
		}
	}
	return strconv.Itoa(result)
}
