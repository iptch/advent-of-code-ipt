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
	v, w, x, y, z rune
	depth         int
}

func (a AtoAPath) print() {
	if a.v == EmptyRune {
		fmt.Printf("A")
	} else if a.w == EmptyRune {
		fmt.Printf("%cA", a.v)
	} else if a.x == EmptyRune {
		fmt.Printf("%c%cA", a.v, a.w)
	} else if a.y == EmptyRune {
		fmt.Printf("%c%c%cA", a.v, a.w, a.x)
	} else if a.z == EmptyRune {
		fmt.Printf("%c%c%c%cA", a.v, a.w, a.x, a.y)
	} else {
		fmt.Printf("%c%c%c%c%cA", a.v, a.w, a.x, a.y, a.z)
	}
}

func (a AtoAPath) toRunes() []rune {
	var p []rune

	if a.v == EmptyRune {
		p = []rune{'A', 'A'}
	} else if a.w == EmptyRune {
		p = []rune{'A', a.v, 'A'}
	} else if a.x == EmptyRune {
		p = []rune{'A', a.v, a.w, 'A'}
	} else if a.y == EmptyRune {
		p = []rune{'A', a.v, a.w, a.x, 'A'}
	} else if a.z == EmptyRune {
		p = []rune{'A', a.v, a.w, a.x, a.y, 'A'}
	} else {
		p = []rune{'A', a.v, a.w, a.x, a.y, a.z, 'A'}
	}

	return p
}

func (a AtoAPath) score() int {
	if a.v == EmptyRune {
		return 1
	} else if a.w == EmptyRune {
		return 2
	} else if a.x == EmptyRune {
		return 3
	} else if a.y == EmptyRune {
		return 4
	} else if a.z == EmptyRune {
		return 5
	} else {
		return 6
	}
}

const (
	EmptyRune = 'E'
)

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
	{'A', 'A'}: {'A'},
	{'A', '^'}: {'<', 'A'},
	{'A', '>'}: {'v', 'A'},
	{'A', 'v'}: {'<', 'v', 'A'},
	{'A', '<'}: {'v', '<', '<', 'A'},

	{'^', '^'}: {'A'},
	{'^', 'A'}: {'>', 'A'},
	{'^', '>'}: {'v', '>', 'A'},
	{'^', 'v'}: {'v', 'A'},
	{'^', '<'}: {'v', '<', 'A'},

	{'>', '>'}: {'A'},
	{'>', 'A'}: {'^', 'A'},
	{'>', 'v'}: {'<', 'A'},
	{'>', '<'}: {'<', '<', 'A'},
	{'>', '^'}: {'<', '^', 'A'},

	{'<', '<'}: {'A'},
	{'<', 'A'}: {'>', '>', '^', 'A'},
	{'<', '>'}: {'>', '>', 'A'},
	{'<', 'v'}: {'>', 'A'},
	{'<', '^'}: {'>', '^', 'A'},

	{'v', 'v'}: {'A'},
	{'v', 'A'}: {'^', '>', 'A'},
	{'v', '>'}: {'>', 'A'},
	{'v', '<'}: {'<', 'A'},
	{'v', '^'}: {'^', 'A'},
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

func expandOnce(path AtoAPath) []rune {
	p := path.toRunes()

	var expansion []rune
	previous := 'A'
	for _, current := range p {
		expansion = append(expansion, bestExpansion[RunePath{previous, current}]...)
		previous = current
	}

	return expansion
}

func splitIntoAtoAChunk(path []rune, depth int) []AtoAPath {
	var result []AtoAPath
	v, w, x, y, z := EmptyRune, EmptyRune, EmptyRune, EmptyRune, EmptyRune
	for _, char := range path[1:] {
		if char == 'A' {
			result = append(result, AtoAPath{v, w, x, y, z, depth})
			v, w, x, y, z = EmptyRune, EmptyRune, EmptyRune, EmptyRune, EmptyRune
		} else {
			if v == EmptyRune {
				v = char
			} else if w == EmptyRune {
				w = char
			} else if x == EmptyRune {
				x = char
			} else if y == EmptyRune {
				y = char
			} else if z == EmptyRune {
				z = char
			}
		}
	}

	return result
}

func expandPath(path AtoAPath) int {
	val, exists := cache[path]
	if exists {
		return val
	}

	if path.depth == 0 {
		return path.score()
	}

	expansion := expandOnce(path)
	aToaChunks := splitIntoAtoAChunk(expansion, path.depth)

	result := 0
	for _, aToaChunk := range aToaChunks {
		aToaChunk.depth = aToaChunk.depth - 1
		result += expandPath(aToaChunk)
	}

	cache[path] = result
	return result
}

func computeShortestSequenceBetter(line string, depth int) int {
	currentIteration := expandNumericKeypad(line)

	best := math.MaxInt
	for i := range currentIteration {
		currentScore := 0
		lineToExpand := append([]rune{'A'}, currentIteration[i]...)
		a2aChunks := splitIntoAtoAChunk(lineToExpand, depth)
		for _, a2aChunk := range a2aChunks {
			currentScore += expandPath(a2aChunk)
		}
		best = min(best, currentScore)
	}

	return best
}

func (d Day21) PartOne(lines []string) string {
	result := 0

	for _, line := range lines {
		shortestSequence := computeShortestSequenceBetter(line, 2)
		result += codeScore(line) * shortestSequence
	}

	return strconv.Itoa(result)
}

func (d Day21) PartTwo(lines []string) string {
	result := 0

	for _, line := range lines {
		shortestSequence := computeShortestSequenceBetter(line, 25)
		result += codeScore(line) * shortestSequence
	}

	return strconv.Itoa(result)
}
