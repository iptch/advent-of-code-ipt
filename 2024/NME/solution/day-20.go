package solution

import (
	"container/heap"
	"fmt"
	"math"
	"strconv"
)

type Coordinate2DWithCheatsAndDistance struct {
	Coordinates Coordinate2D
	CanCheat    bool
	IsCheating  bool
	CheatStart  Coordinate2D
	CheatEnd    Coordinate2D
	Distance    int
}

// MinHeap /* ------------------------------------------ */

// MinHeap is a type that implements heap.Interface
type CheatingMinHeap []Coordinate2DWithCheatsAndDistance

// Len returns the number of elements in the heap
func (h CheatingMinHeap) Len() int {
	return len(h)
}

// Less returns true if the element at index i is less than the element at index j
func (h CheatingMinHeap) Less(i, j int) bool {
	return h[i].Distance < h[j].Distance
}

// Swap swaps the elements at indices i and j
func (h CheatingMinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

// Push adds an element to the heap
func (h *CheatingMinHeap) Push(x interface{}) {
	*h = append(*h, x.(Coordinate2DWithCheatsAndDistance))
}

// Pop removes and returns the smallest element from the heap
func (h *CheatingMinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// Peek returns the smallest element without removing it
func (h CheatingMinHeap) Peek() Coordinate2DWithCheatsAndDistance {
	if len(h) == 0 {
		panic("Heap is empty")
	}
	return h[0]
}

/* ------------------------------------------ */

func parseDay20(lines []string) ([][]bool, Coordinate2D, Coordinate2D) {
	n := len(lines)
	grid := make([][]bool, n)
	var start, end Coordinate2D

	for i, line := range lines {
		grid[i] = make([]bool, n)
		for j, c := range line {
			switch c {
			case '#':
				grid[i][j] = true
			case '.':
				grid[i][j] = false
			case 'S':
				grid[i][j] = false
				start = Coordinate2D{i, j}
			case 'E':
				grid[i][j] = false
				end = Coordinate2D{i, j}
			}
		}
	}

	return grid, start, end
}

func djikstra(grid [][]bool, start Coordinate2D, end Coordinate2D) [][]int {
	distances := make([][]int, len(grid))
	for i := range distances {
		distances[i] = make([]int, len(grid[i]))
		for j := range distances[i] {
			distances[i][j] = math.MaxInt32
		}
	}

	h := &MinHeap{}
	heap.Init(h)

	distances[start.X][start.Y] = 0
	h.Push(Coordinate2DWithDistance{start, 0})

	for h.Len() > 0 {
		current := heap.Pop(h).(Coordinate2DWithDistance)

		for _, neighbor := range current.Coordinates.Neighbors4() {
			if neighbor.OutOfBounds(len(grid), len(grid[0])) == false &&
				grid[neighbor.X][neighbor.Y] == false &&
				distances[neighbor.X][neighbor.Y] > current.Distance+1 {
				distances[neighbor.X][neighbor.Y] = current.Distance + 1
				heap.Push(h, Coordinate2DWithDistance{Coordinate2D{neighbor.X, neighbor.Y}, current.Distance + 1})
			}
		}
	}

	return distances
}

func printDistances(grid [][]bool, distances [][][]int) {
	for i, row := range grid {
		for j := range row {
			best := math.MaxInt32
			for k := range distances[i][j] {
				best = min(best, distances[i][j][k])
			}
			if best == math.MaxInt32 {
				fmt.Printf(" -1 ")
			} else {
				fmt.Printf(" %2v ", best)
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

func countCheats(grid [][]bool, distances [][]int, maxCheatDistance int) int {
	result := 0
	for i := range len(distances) {
		for j := range distances[i] {
			if distances[i][j] != math.MaxInt32 {
				for a := -maxCheatDistance; a <= maxCheatDistance; a++ {
					for b := -maxCheatDistance; b <= maxCheatDistance; b++ {
						dist := abs(a) + abs(b)
						if dist <= maxCheatDistance {
							cheatEnd := Coordinate2D{i + a, j + b}
							if cheatEnd.OutOfBounds(len(grid), len(grid[0])) == false &&
								grid[cheatEnd.X][cheatEnd.Y] == false {
								timeSaved := distances[cheatEnd.X][cheatEnd.Y] - distances[i][j] - dist
								if timeSaved >= 100 {
									result++
								}
							}
						}
					}
				}
			}
		}
	}
	return result
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func (d Day20) PartOne(lines []string) string {
	grid, start, end := parseDay20(lines)
	distances := djikstra(grid, start, end)
	cheats := countCheats(grid, distances, 2)
	return strconv.Itoa(cheats)
}

func (d Day20) PartTwo(lines []string) string {
	grid, start, end := parseDay20(lines)
	distances := djikstra(grid, start, end)
	cheats := countCheats(grid, distances, 20)
	return strconv.Itoa(cheats)
}
