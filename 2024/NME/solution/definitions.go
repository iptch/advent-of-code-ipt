package solution

type Day01 struct{}
type Day02 struct{}
type Day03 struct{}
type Day04 struct{}
type Day05 struct{}
type Day06 struct{}
type Day07 struct{}
type Day08 struct{}
type Day09 struct{}
type Day10 struct{}
type Day11 struct{}
type Day12 struct{}
type Day13 struct{}
type Day14 struct{}
type Day15 struct{}
type Day16 struct{}
type Day17 struct{}
type Day18 struct{}
type Day19 struct{}
type Day20 struct{}
type Day21 struct{}
type Day22 struct{}
type Day23 struct{}
type Day24 struct{}
type Day25 struct{}

type Coordinate2D struct {
	X, Y int
}

type Coordinate2DWithDistance struct {
	Coordinates Coordinate2D
	Distance    int
}

func (c Coordinate2D) OutOfBounds(width int, height int) bool {
	return c.X < 0 || c.X >= width || c.Y < 0 || c.Y >= height
}

func (c Coordinate2D) Neighbors4() [4]Coordinate2D {
	return [4]Coordinate2D{
		{c.X + 1, c.Y},
		{c.X - 1, c.Y},
		{c.X, c.Y + 1},
		{c.X, c.Y - 1},
	}
}

// MinHeap /* ------------------------------------------ */

// MinHeap is a type that implements heap.Interface
type MinHeap []Coordinate2DWithDistance

// Len returns the number of elements in the heap
func (h MinHeap) Len() int {
	return len(h)
}

// Less returns true if the element at index i is less than the element at index j
func (h MinHeap) Less(i, j int) bool {
	return h[i].Distance < h[j].Distance
}

// Swap swaps the elements at indices i and j
func (h MinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

// Push adds an element to the heap
func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Coordinate2DWithDistance))
}

// Pop removes and returns the smallest element from the heap
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// Peek returns the smallest element without removing it
func (h MinHeap) Peek() Coordinate2DWithDistance {
	if len(h) == 0 {
		panic("Heap is empty")
	}
	return h[0]
}

/* ------------------------------------------ */
