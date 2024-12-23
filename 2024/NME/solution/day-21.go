package solution

import (
	"fmt"
	"math"
	"strconv"
	"unicode"
)

type RunePath struct {
	start, end rune
}

type AtoAPath struct {
	path   [5]rune
	length int
	depth  int
}

func (a AtoAPath) print() {
	for i := 0; i < a.length; i++ {
		fmt.Printf("%c", a.path[i])
	}
	fmt.Printf("A")
}

/*
	+---+---+---+
	| 7 | 8 | 9 |
	+---+---+---+
	| 4 | 5 | 6 |
	+---+---+---+
	| 1 | 2 | 3 |
	+---+---+---+
		| 0 | A |
		+---+---+
*/

var RuneToPosition = map[rune]Coordinate2D{
	'7': {0, 0},
	'8': {0, 1},
	'9': {0, 2},
	'4': {1, 0},
	'5': {1, 1},
	'6': {1, 2},
	'1': {2, 0},
	'2': {2, 1},
	'3': {2, 2},
	'0': {3, 1},
	'A': {3, 2},
}

var PositionToRune = map[Coordinate2D]rune{
	Coordinate2D{0, 0}: '7',
	Coordinate2D{0, 1}: '8',
	Coordinate2D{0, 2}: '9',
	Coordinate2D{1, 0}: '4',
	Coordinate2D{1, 1}: '5',
	Coordinate2D{1, 2}: '6',
	Coordinate2D{2, 0}: '1',
	Coordinate2D{2, 1}: '2',
	Coordinate2D{2, 2}: '3',
	Coordinate2D{3, 1}: '0',
	Coordinate2D{3, 2}: 'A',
}

/*
		+---+---+
		| ^ | A |
	+---+---+---+
	| < | v | > |
	+---+---+---+
*/

var bestExpansion = map[RunePath][]rune{
	{'A', 'A'}: {},
	{'A', '^'}: {'<'},
	{'A', '>'}: {'v'},
	{'A', 'v'}: {'<', 'v'},
	{'A', '<'}: {'v', '<', '<'},

	{'^', '^'}: {},
	{'^', 'A'}: {'>'},
	{'^', '>'}: {'v', '>'},
	{'^', 'v'}: {'v'},
	{'^', '<'}: {'v', '<'},

	{'>', '>'}: {},
	{'>', 'A'}: {'^'},
	{'>', 'v'}: {'<'},
	{'>', '<'}: {'<', '<'},
	{'>', '^'}: {'<', '^'},

	{'<', '<'}: {},
	{'<', 'A'}: {'>', '>', '^'},
	{'<', '>'}: {'>', '>'},
	{'<', 'v'}: {'>'},
	{'<', '^'}: {'>', '^'},

	{'v', 'v'}: {},
	{'v', 'A'}: {'^', '>'},
	{'v', '>'}: {'>'},
	{'v', '<'}: {'<'},
	{'v', '^'}: {'^'},
}

var CACHE = make(map[RunePath][][]rune)

var cache = make(map[AtoAPath]int)

func expandNumericKeypad(sequence string) [][]rune {
	result := [][]rune{{}}
	previous := 'A'
	for _, current := range sequence {
		var newResult [][]rune
		possiblePaths := possiblePathsNumeric(RunePath{previous, current})
		for _, optionsSoFar := range result {
			for _, option := range possiblePaths {
				optionsSoFarCopy := make([]rune, len(optionsSoFar))
				copy(optionsSoFarCopy, optionsSoFar)
				newOption := append(optionsSoFarCopy, option...)
				newOptionWithPress := append(newOption, 'A')
				newResult = append(newResult, newOptionWithPress)
			}
		}
		previous = current
		result = newResult
	}
	return result
}

func possiblePathsNumeric(path RunePath) [][]rune {
	cacheHit, exists := CACHE[path]
	if exists {
		return cacheHit
	}

	S, E := RuneToPosition[path.start], RuneToPosition[path.end]

	result := [][]Coordinate2D{{S}}
	distance := S.manhattanDistance(E)
	for i := 0; i < distance; i++ {
		var nextResult [][]Coordinate2D
		for _, resultSoFar := range result {
			for _, neighbor := range resultSoFar[len(resultSoFar)-1].Neighbors4() {
				_, ok := PositionToRune[neighbor]
				if ok && neighbor.manhattanDistance(E) == distance-i-1 {
					resultSoFarCopy := make([]Coordinate2D, len(resultSoFar))
					copy(resultSoFarCopy, resultSoFar)
					newResult := append(resultSoFarCopy, neighbor)
					nextResult = append(nextResult, newResult)
				}
			}
		}
		result = nextResult
	}

	actualResult := make([][]rune, len(result))
	for i, oneResult := range result {
		actualResult[i] = make([]rune, len(oneResult)-1)
		for j := 0; j < len(oneResult)-1; j++ {
			s, e := oneResult[j], oneResult[j+1]
			if s.X+1 == e.X {
				actualResult[i][j] = 'v'
			} else if s.X-1 == e.X {
				actualResult[i][j] = '^'
			} else if s.Y+1 == e.Y {
				actualResult[i][j] = '>'
			} else if s.Y-1 == e.Y {
				actualResult[i][j] = '<'
			} else {
				panic("omg")
			}
		}
	}

	CACHE[path] = actualResult
	return actualResult
}

func (c Coordinate2D) manhattanDistance(other Coordinate2D) int {
	return abs(c.X-other.X) + abs(c.Y-other.Y)
}

func printSequences(sequences [][]rune) {
	for _, sequence := range sequences {
		for _, r := range sequence {
			fmt.Printf("%c", r)
		}
		fmt.Println()
	}
	fmt.Println()
}

func codeScore(code string) int {
	res := ""
	for _, char := range code {
		if unicode.IsDigit(char) {
			res += string(char)
		}
	}
	i, _ := strconv.Atoi(res)
	return i
}

func (a AtoAPath) toSlice() []rune {
	result := make([]rune, a.length+1)
	for i := range a.length {
		result[i] = a.path[i]
	}
	result[a.length] = 'A'
	return result
}

func (a AtoAPath) expandOnce() []AtoAPath {
	var expansions []AtoAPath
	previous := 'A'
	for _, current := range a.toSlice() {
		expansion := bestExpansion[RunePath{previous, current}]
		var fixedLengthPath [5]rune
		for i := 0; i < len(expansion); i++ {
			fixedLengthPath[i] = expansion[i]
		}
		expansions = append(expansions, AtoAPath{fixedLengthPath, len(expansion), a.depth - 1})
		previous = current
	}

	return expansions
}

func (a AtoAPath) expandPathMemo() int {
	_, exists := cache[a]
	if exists == false {
		cache[a] = a.expandPath()
	}
	return cache[a]
}

func (a AtoAPath) expandPath() int {
	if a.depth == 0 {
		return a.length + 1
	}

	result := 0
	for _, aToaChunk := range a.expandOnce() {
		result += aToaChunk.expandPathMemo()
	}
	return result
}

func splitIntoAtoAChunk(fullPath []rune) []AtoAPath {
	var result []AtoAPath
	currentLength := 0
	for i, char := range fullPath {
		if char == 'A' {
			var fixedLengthPath [5]rune
			for j := 0; j < currentLength; j++ {
				fixedLengthPath[j] = fullPath[i-currentLength+j]
			}
			result = append(result, AtoAPath{path: fixedLengthPath, length: currentLength})
			currentLength = 0
		} else {
			currentLength++
		}
	}

	return result
}

func shortestSequence(line string, depth int) int {
	numericExpansion := expandNumericKeypad(line)

	best := math.MaxInt
	for i := range numericExpansion {
		currentScore := 0
		a2aChunks := splitIntoAtoAChunk(numericExpansion[i])
		for _, a2aChunk := range a2aChunks {
			a2aChunk.depth = depth
			currentScore += a2aChunk.expandPath()
		}
		best = min(best, currentScore)
	}

	return best
}

func solve(lines []string, depth int) int {
	result := 0
	for _, line := range lines {
		result += codeScore(line) * shortestSequence(line, depth)
	}
	return result
}

func (d Day21) PartOne(lines []string) string {
	return strconv.Itoa(solve(lines, 2))
}

func (d Day21) PartTwo(lines []string) string {
	return strconv.Itoa(solve(lines, 25))
}
