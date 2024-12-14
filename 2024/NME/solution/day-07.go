package solution

import (
	"math"
	"strconv"
	"strings"
)

type Equation struct {
	Result int64
	Values []int64
}

func parseDay07(lines []string) []Equation {
	res := make([]Equation, len(lines))
	for i, line := range lines {
		testValAndRest := strings.Split(line, ": ")
		testVal, _ := strconv.ParseInt(testValAndRest[0], 10, 64)
		values := strings.Split(testValAndRest[1], " ")
		intValues := make([]int64, len(values))
		for j, v := range values {
			intValues[j], _ = strconv.ParseInt(v, 10, 64)
		}

		res[i] = Equation{testVal, intValues}
	}
	return res
}

func valid(equation Equation, resultSoFar int64, idx int) bool {
	if equation.Result < resultSoFar {
		return false
	}

	if len(equation.Values) == idx {
		return resultSoFar == equation.Result
	}

	nextVal := equation.Values[idx]
	return valid(equation, resultSoFar+nextVal, idx+1) ||
		valid(equation, resultSoFar*nextVal, idx+1)
}

func validPart2(equation Equation, resultSoFar int64, idx int) bool {
	if equation.Result < resultSoFar {
		return false
	}

	if len(equation.Values) == idx {
		return resultSoFar == equation.Result
	}

	nextVal := equation.Values[idx]
	return validPart2(equation, resultSoFar+nextVal, idx+1) ||
		validPart2(equation, resultSoFar*nextVal, idx+1) ||
		validPart2(equation, concatenate(resultSoFar, nextVal), idx+1)
}

func concatenate(left int64, right int64) int64 {
	numDigitsRight := float64(len(strconv.FormatInt(right, 10)))
	return left*int64(math.Pow(10, numDigitsRight)) + right
}

func (d Day07) PartOne(lines []string) string {
	equations := parseDay07(lines)
	var result int64 = 0
	for _, equation := range equations {
		if valid(equation, 0, 0) {
			result += equation.Result
		}
	}
	return strconv.FormatInt(result, 10)
}

func (d Day07) PartTwo(lines []string) string {
	equations := parseDay07(lines)
	var result int64 = 0
	for _, equation := range equations {
		if validPart2(equation, 0, 0) {
			result += equation.Result
		}
	}
	return strconv.FormatInt(result, 10)
}
