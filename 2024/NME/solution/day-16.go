package solution

import (
	"container/heap"
	"fmt"
	"math"
	"strconv"
)

type MazeCell bool

const (
	WALL  MazeCell = true
	EMPTY MazeCell = false
)

type Reindeer struct {
	X, Y      int
	Direction Direction
	Scores    [][][]int
}

// MinReindeerHeap /* ------------------------------------------ */

// MinReindeerHeap is a type that implements heap.Interface
type MinReindeerHeap []Reindeer

// Len returns the number of elements in the heap
func (h MinReindeerHeap) Len() int {
	return len(h)
}

// Less returns true if the element at index i is less than the element at index j
func (h MinReindeerHeap) Less(i, j int) bool {
	return h[i].score() < h[j].score()
}

// Swap swaps the elements at indices i and j
func (h MinReindeerHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

// Push adds an element to the heap
func (h *MinReindeerHeap) Push(x interface{}) {
	*h = append(*h, x.(Reindeer))
}

// Pop removes and returns the smallest element from the heap
func (h *MinReindeerHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// Peek returns the smallest element without removing it
func (h MinReindeerHeap) Peek() Reindeer {
	if len(h) == 0 {
		panic("Heap is empty")
	}
	return h[0]
}

/* ------------------------------------------ */

func parseDay16(lines []string) ([][]MazeCell, Reindeer, Coordinate2D) {
	scores := make([][][]int, len(lines))
	for i := range scores {
		scores[i] = make([][]int, len(lines[i]))
		for j := range scores[i] {
			scores[i][j] = make([]int, 4)
			for k := range scores[i][j] {
				scores[i][j][k] = math.MaxInt
			}
		}
	}

	maze := make([][]MazeCell, len(lines))
	var reindeer Reindeer
	var end Coordinate2D
	for i, line := range lines {
		maze[i] = make([]MazeCell, len(line))
		for j, cell := range line {
			switch cell {
			case '#':
				maze[i][j] = WALL
			case '.':
				maze[i][j] = EMPTY
			case 'S':
				reindeer = Reindeer{j, i, Right, scores}
			case 'E':
				end = Coordinate2D{j, i}
			default:
				panic("unknown symbol")
			}
		}
	}

	return maze, reindeer, end
}

func (r Reindeer) next(maze [][]MazeCell) (Reindeer, bool) {
	nextA := r.X
	nextB := r.Y

	switch r.Direction {
	case Up:
		nextB = r.Y - 1
	case Down:
		nextB = r.Y + 1
	case Left:
		nextA = r.X - 1
	case Right:
		nextA = r.X + 1
	}

	if maze[nextB][nextA] == EMPTY {
		return Reindeer{nextA, nextB, r.Direction, r.Scores}, true
	} else {
		return r, false
	}

}

func (r Reindeer) prev(maze [][]MazeCell) (Reindeer, bool) {
	prevA := r.X
	prevB := r.Y

	switch r.Direction {
	case Up:
		prevB = r.Y + 1
	case Down:
		prevB = r.Y - 1
	case Left:
		prevA = r.X + 1
	case Right:
		prevA = r.X - 1
	}

	if maze[prevB][prevA] == EMPTY {
		return Reindeer{prevA, prevB, r.Direction, r.Scores}, true
	} else {
		return r, false
	}

}

func (r Reindeer) score() int {
	return r.Scores[r.X][r.Y][r.Direction]
}

func (r Reindeer) setScore(newScore int) {
	r.Scores[r.X][r.Y][r.Direction] = newScore
}

func (r Reindeer) turn90() (Reindeer, Reindeer) {
	var d1, d2 Direction

	switch r.Direction {
	case Up, Down:
		d1, d2 = Left, Right
	case Left, Right:
		d1, d2 = Up, Down
	}

	return Reindeer{r.X, r.Y, d1, r.Scores}, Reindeer{r.X, r.Y, d2, r.Scores}
}

func printScores(scores [][][]int, maze [][]MazeCell) {
	for i, row := range maze {
		for j, cell := range row {
			if cell == EMPTY {
				best := min(
					Reindeer{j, i, Up, scores}.score(),
					Reindeer{j, i, Down, scores}.score(),
					Reindeer{j, i, Left, scores}.score(),
					Reindeer{j, i, Right, scores}.score(),
				)
				if best == math.MaxInt {
					best = -1
				}
				fmt.Printf("%6d ", best)
			} else {
				fmt.Printf("#######")
			}
		}
		fmt.Printf("\n")
	}
	fmt.Printf("\n")
}

func walkToEnd(maze [][]MazeCell, reindeer Reindeer, end Coordinate2D) int {

	queue := &MinReindeerHeap{}
	heap.Init(queue)
	reindeer.setScore(0)
	queue.Push(reindeer)

	for queue.Len() > 0 {
		current := heap.Pop(queue).(Reindeer)

		next, hasMoved := current.next(maze)

		if hasMoved && next.score() > current.score()+1 {
			next.setScore(current.score() + 1)
			queue.Push(next)
		}

		turn1, turn2 := current.turn90()

		if turn1.score() > current.score()+1000 {
			turn1.setScore(current.score() + 1000)
			queue.Push(turn1)
		}

		if turn2.score() > current.score()+1000 {
			turn2.setScore(current.score() + 1000)
			queue.Push(turn2)
		}
	}

	return min(
		Reindeer{end.X, end.Y, Up, reindeer.Scores}.score(),
		Reindeer{end.X, end.Y, Down, reindeer.Scores}.score(),
		Reindeer{end.X, end.Y, Left, reindeer.Scores}.score(),
		Reindeer{end.X, end.Y, Right, reindeer.Scores}.score(),
	)
}

func (d Day16) PartOne(lines []string) string {
	maze, reindeer, end := parseDay16(lines)
	finalScore := walkToEnd(maze, reindeer, end)
	return strconv.Itoa(finalScore)
}

func printVisitedCells(visitedCells map[Coordinate2D]bool, maze [][]MazeCell) {
	for i, row := range maze {
		for j, cell := range row {
			if cell == EMPTY && visitedCells[Coordinate2D{j, i}] {
				fmt.Printf("O")
			} else if cell == EMPTY {
				fmt.Printf(".")
			} else {
				fmt.Printf("#")
			}
		}
		fmt.Printf("\n")
	}
	fmt.Printf("\n")
}

func walkBack(maze [][]MazeCell, reindeer Reindeer, end Coordinate2D) int {
	queue := &MinReindeerHeap{}
	heap.Init(queue)

	bestReindeer := Reindeer{end.X, end.Y, Up, reindeer.Scores}
	for _, d := range []Direction{Up, Down, Left, Right} {
		currentReindeer := Reindeer{end.X, end.Y, d, reindeer.Scores}
		if currentReindeer.score() < bestReindeer.score() {
			bestReindeer = currentReindeer
		}
	}
	queue.Push(bestReindeer)

	visitedCells := make(map[Coordinate2D]bool)

	for queue.Len() > 0 {
		current := heap.Pop(queue).(Reindeer)
		visitedCells[Coordinate2D{current.X, current.Y}] = true

		prev, hasMoved := current.prev(maze)
		if hasMoved && prev.score() < current.score() {
			queue.Push(prev)
		}

		turn1, turn2 := current.turn90()
		if turn1.score() < current.score() {
			queue.Push(turn1)
		}
		if turn2.score() < current.score() {
			queue.Push(turn2)
		}
	}

	return len(visitedCells)
}

func (d Day16) PartTwo(lines []string) string {
	maze, reindeer, end := parseDay16(lines)
	walkToEnd(maze, reindeer, end)
	optimalCells := walkBack(maze, reindeer, end)
	return strconv.Itoa(optimalCells)
}
