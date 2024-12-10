package day10

import (
	"container/list"
	"strconv"
)

type Node struct {
	Neighbors []*Node
	Position  Coordinate
	Value     int
}

type Coordinate struct {
	X, Y int
}

func PartOne(lines []string) string {
	graph := buildGraph(lines)

	result := 0
	for _, startNode := range graph[0] {
		result += findNumSinks(startNode)
	}

	return strconv.Itoa(result)
}

func PartTwo(lines []string) string {
	graph := buildGraph(lines)
	result := 0
	for _, startNode := range graph[0] {
		result += findRating(startNode)
	}

	return strconv.Itoa(result)
}

func findRating(node *Node) int {
	queue := list.New()
	queue.PushBack(node)

	result := 0
	for queue.Len() > 0 {
		front := queue.Front()
		queue.Remove(front)

		currentNode := front.Value.(*Node)

		if currentNode.Value == 9 {
			result++
		}

		for _, neighbor := range currentNode.Neighbors {
			queue.PushBack(neighbor)
		}
	}
	return result
}

func findNumSinks(node *Node) int {
	queue := list.New()
	queue.PushBack(node)
	sinks := map[Coordinate]bool{}

	for queue.Len() > 0 {
		front := queue.Front()
		queue.Remove(front)

		currentNode := front.Value.(*Node)

		if currentNode.Value == 9 {
			sinks[currentNode.Position] = true
		}

		for _, neighbor := range currentNode.Neighbors {
			queue.PushBack(neighbor)
		}
	}

	return len(sinks)
}

func buildGraph(lines []string) map[int][]*Node {
	graph := make(map[int][]*Node)
	blankNodes := make([][]Node, len(lines))
	for i, line := range lines {
		blankNodes[i] = make([]Node, len(line))
		for j, v := range line {
			intValue, _ := strconv.Atoi(string(v))
			blankNodes[i][j] = Node{
				Position: Coordinate{i, j},
				Value:    intValue,
			}
			graph[intValue] = append(graph[intValue], &blankNodes[i][j])
		}
	}

	neighborVectors := [][]int{
		{1, 0},
		{0, 1},
		{-1, 0},
		{0, -1},
	}
	for i := range blankNodes {
		for j := range blankNodes[i] {
			node := &blankNodes[i][j]
			for _, vector := range neighborVectors {
				a, b := vector[0]+i, vector[1]+j
				if a >= 0 && b >= 0 && a < len(blankNodes) && b < len(blankNodes) {
					neighbor := &blankNodes[a][b]
					if node.Value+1 == neighbor.Value {
						node.Neighbors = append(node.Neighbors, neighbor)
					}
				}
			}
		}
	}
	return graph
}
