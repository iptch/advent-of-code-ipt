package solution

import (
	"sort"
	"strconv"
	"strings"
)

type Vertex struct {
	Name      string
	Neighbors *[]Vertex
}

func parseDay23(lines []string) (map[string]Vertex, map[string]map[string]bool) {
	graph := make(map[string]Vertex)
	adjacencyMatrix := make(map[string]map[string]bool)

	for _, line := range lines {
		n1, n2 := line[:2], line[3:]
		value1, exists1 := graph[n1]
		if exists1 == false {
			value1 = Vertex{n1, &[]Vertex{}}
			graph[n1] = value1
		}
		value2, exists2 := graph[n2]
		if exists2 == false {
			value2 = Vertex{n2, &[]Vertex{}}
			graph[n2] = value2
		}
		*value1.Neighbors = append(*value1.Neighbors, value2)
		*value2.Neighbors = append(*value2.Neighbors, value1)
	}

	for key, value := range graph {
		adjacencyMatrix[key] = make(map[string]bool)
		for _, vertex := range *value.Neighbors {
			adjacencyMatrix[key][vertex.Name] = true
		}
	}

	return graph, adjacencyMatrix
}

func (d Day23) PartOne(lines []string) string {
	graph, _ := parseDay23(lines)

	result := 0
	for key, value := range graph {
		for i := 0; i < len(*value.Neighbors); i++ {
			for j := i + 1; j < len(*value.Neighbors); j++ {
				n1, n2 := (*value.Neighbors)[i], (*value.Neighbors)[j]
				for a := 0; a < len(*n1.Neighbors); a++ {
					if (*n1.Neighbors)[a].Name == n2.Name {
						if key[0] == 't' || n1.Name[0] == 't' || n2.Name[0] == 't' {
							result++
						}
					}
				}
			}
		}
	}

	return strconv.Itoa(result / 3)
}

func choose(neighbors *[]Vertex, n int) [][]Vertex {
	var result [][]Vertex
	var helper func(int, []Vertex)

	helper = func(start int, combination []Vertex) {
		if len(combination) == n {
			combinationCopy := make([]Vertex, n)
			copy(combinationCopy, combination)
			result = append(result, combinationCopy)
			return
		}

		for i := start; i < len(*neighbors); i++ {
			helper(i+1, append(combination, (*neighbors)[i]))
		}
	}

	helper(0, []Vertex{})
	return result
}

func fullyConnected(vertices []Vertex, adjacencyMatrix map[string]map[string]bool) bool {
	result := true
	for i := 0; i < len(vertices); i++ {
		for j := i + 1; j < len(vertices); j++ {
			_, connected := adjacencyMatrix[vertices[i].Name][vertices[j].Name]
			result = result && connected
		}
	}
	return result
}

func biggestFullyConnectedSubGraph(value Vertex, adjacencyMatrix map[string]map[string]bool) []Vertex {
	for i := len(*value.Neighbors); i > 0; i-- {
		combinations := choose(value.Neighbors, i)
		for _, combination := range combinations {
			if fullyConnected(combination, adjacencyMatrix) {
				return append(combination, value)
			}
		}
	}
	return []Vertex{}
}

func prettyPrint(result []Vertex) string {
	var names []string
	for _, value := range result {
		names = append(names, value.Name)
	}
	sort.Strings(names)
	return strings.Join(names, ",")
}

func (d Day23) PartTwo(lines []string) string {
	graph, adjacencyMatrix := parseDay23(lines)

	var result []Vertex
	for _, value := range graph {
		maxFullyConnected := biggestFullyConnectedSubGraph(value, adjacencyMatrix)
		if len(maxFullyConnected) > len(result) {
			result = maxFullyConnected
		}
	}
	return prettyPrint(result)
}
