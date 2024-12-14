package solution

import "strconv"

func parseDay08(lines []string) map[rune][]Coordinate2D {
	frequencies := make(map[rune][]Coordinate2D)
	for i, line := range lines {
		for j, char := range line {
			if char != '.' {
				frequencies[char] = append(frequencies[char], Coordinate2D{i, j})
			}
		}
	}
	return frequencies
}

func inBounds(location Coordinate2D, gridSize int) bool {
	return location.X >= 0 && location.X < gridSize && location.Y >= 0 && location.Y < gridSize
}

func computeOneAntiNode(antenna1 Coordinate2D, antenna2 Coordinate2D) Coordinate2D {
	diffX := antenna1.X - antenna2.X
	diffY := antenna1.Y - antenna2.Y
	return Coordinate2D{antenna1.X + diffX, antenna1.Y + diffY}
}

func computeAllAntiNodes(antenna1 Coordinate2D, antenna2 Coordinate2D, gridSize int) []Coordinate2D {
	var antiNodes []Coordinate2D

	diffX := antenna1.X - antenna2.X
	diffY := antenna1.Y - antenna2.Y

	displacement := 0
	// go up
	for {
		candidate := Coordinate2D{diffX*displacement + antenna1.X, diffY*displacement + antenna1.Y}
		if inBounds(candidate, gridSize) {
			antiNodes = append(antiNodes, candidate)
			displacement++
		} else {
			break
		}
	}
	displacement = -1
	// go down
	for {
		candidate := Coordinate2D{diffX*displacement + antenna1.X, diffY*displacement + antenna1.Y}
		if inBounds(candidate, gridSize) {
			antiNodes = append(antiNodes, candidate)
			displacement--
		} else {
			break
		}
	}
	return antiNodes
}

func (d Day08) PartOne(lines []string) string {
	frequencies := parseDay08(lines)
	n := len(lines)
	antiNodeLocations := make(map[Coordinate2D]bool)
	for ident := range frequencies {
		for i, antenna1 := range frequencies[ident] {
			for j, antenna2 := range frequencies[ident] {
				if i != j {
					antiNode := computeOneAntiNode(antenna1, antenna2)
					if inBounds(antiNode, n) {
						antiNodeLocations[antiNode] = true
					}
				}
			}
		}
	}
	return strconv.Itoa(len(antiNodeLocations))
}

func (d Day08) PartTwo(lines []string) string {
	frequencies := parseDay08(lines)
	gridSize := len(lines)
	antiNodeLocations := make(map[Coordinate2D]bool)
	for ident := range frequencies {
		numAntennas := len(frequencies[ident])
		for i := 0; i < numAntennas; i++ {
			for j := i + 1; j < numAntennas; j++ {
				antiNodes := computeAllAntiNodes(frequencies[ident][i], frequencies[ident][j], gridSize)
				for _, antiNode := range antiNodes {
					antiNodeLocations[antiNode] = true

				}
			}
		}
	}
	return strconv.Itoa(len(antiNodeLocations))
}
