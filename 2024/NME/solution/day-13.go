package solution

import (
	"regexp"
	"strconv"
)

type LinearEquations struct {
	X1, Y1, B1 int
	X2, Y2, B2 int
}

func parseDay13(lines []string) []LinearEquations {
	var result []LinearEquations
	for i := 0; i < (len(lines)+2)/4; i++ {
		result = append(result, parseOneEquation(lines[4*i:4*i+3]))
	}
	return result
}

func parseOneEquation(lines []string) LinearEquations {
	regexLeftHand := regexp.MustCompile(`Button .: X\+(\d+), Y\+(\d+)`)
	matchesLine0 := regexLeftHand.FindAllStringSubmatch(lines[0], -1)
	matchesLine1 := regexLeftHand.FindAllStringSubmatch(lines[1], -1)

	regexRightHand := regexp.MustCompile(`Prize: X=(\d+), Y=(\d+)`)
	matchesLine2 := regexRightHand.FindAllStringSubmatch(lines[2], -1)

	X1, _ := strconv.Atoi(matchesLine0[0][1])
	X2, _ := strconv.Atoi(matchesLine0[0][2])
	Y1, _ := strconv.Atoi(matchesLine1[0][1])
	Y2, _ := strconv.Atoi(matchesLine1[0][2])
	B1, _ := strconv.Atoi(matchesLine2[0][1])
	B2, _ := strconv.Atoi(matchesLine2[0][2])

	return LinearEquations{X1, Y1, B1, X2, Y2, B2}
}

func evaluate(e LinearEquations) (int, int) {
	B := (e.X1*e.B2 - e.X2*e.B1) / (e.X1*e.Y2 - e.X2*e.Y1)
	A := (e.B1 - e.Y1*B) / e.X1

	if A*e.X1+B*e.Y1 != e.B1 || A*e.X2+B*e.Y2 != e.B2 {
		return 0, 0
	}

	return A, B
}

func (d Day13) PartOne(lines []string) string {
	equations := parseDay13(lines)
	result := 0
	for _, equation := range equations {
		A, B := evaluate(equation)
		result += 3*A + B
	}
	return strconv.Itoa(result)
}

func (d Day13) PartTwo(lines []string) string {
	equations := parseDay13(lines)
	result := 0
	for _, equation := range equations {
		equation.B1 = equation.B1 + 10000000000000
		equation.B2 = equation.B2 + 10000000000000
		A, B := evaluate(equation)
		result += 3*A + B
	}
	return strconv.Itoa(result)
}
