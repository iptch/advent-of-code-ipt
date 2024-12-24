package solution

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

type Gate struct {
	OP       Op
	IN1, IN2 string
	OUT      string
}

const (
	switches = 4
)

type Op int

const (
	AND Op = iota
	OR
	XOR
)

func parseDay24(lines []string) (map[string]*Gate, []string, []string, []string, map[string]bool) {
	gates := make(map[string]*Gate)
	var xs, ys, zs []string
	startingValues := make(map[string]bool)

	parsingValues := true
	for _, line := range lines {
		if line == "" {
			parsingValues = false
			continue
		}

		if parsingValues {
			name := line[:3]
			value := line[5]
			var booleanValue bool
			if value == '0' {
				booleanValue = false
			} else if value == '1' {
				booleanValue = true
			} else {
				panic(booleanValue)
			}

			startingValues[name] = booleanValue

			if name[0] == 'x' {
				xs = append(xs, name)
			}

			if name[0] == 'y' {
				ys = append(ys, name)
			}
		} else {
			opStart := line[4]

			input1 := line[:3]
			var input2 string
			var output string
			var op Op
			switch opStart {
			case 'A':
				op = AND
				input2 = line[8:11]
				output = line[15:]
			case 'O':
				op = OR
				input2 = line[7:10]
				output = line[14:]
			case 'X':
				op = XOR
				input2 = line[8:11]
				output = line[15:]
			default:
				panic(opStart)
			}

			gates[output] = &Gate{op, input1, input2, output}
			if output[0] == 'z' {
				zs = append(zs, output)
			}
		}
	}

	return gates, xs, ys, zs, startingValues
}

func computeCircuit(input string, gates map[string]*Gate, values map[string]bool) {
	_, exists := values[input]
	if exists {
		return
	}

	gate := gates[input]

	computeCircuit(gate.IN1, gates, values)
	computeCircuit(gate.IN2, gates, values)

	input1 := values[gate.IN1]
	input2 := values[gate.IN2]

	var result bool
	switch gate.OP {
	case AND:
		result = input1 && input2
	case OR:
		result = input1 || input2
	case XOR:
		result = input1 != input2
	}
	values[input] = result

}

func assembleResult(inputs []string, symbol rune, values map[string]bool) int {
	result := 0
	for i := len(inputs) - 1; i >= 0; i-- {
		var key string
		if i < 10 {
			key = fmt.Sprintf("%c0%d", symbol, i)
		} else {
			key = fmt.Sprintf("%c%d", symbol, i)
		}
		value := values[key]
		if value {
			result = (result << 1) + 1
		} else {
			result = result << 1
		}
	}
	return result
}

func prettyPrintResults(values map[string]bool) {
	var keys []string
	for k := range values {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	for _, k := range keys {
		r := 0
		if values[k] {
			r = 1
		}
		fmt.Printf("%s: %d\n", k, r)
	}
}

func prettyPrintGates(gates map[string]*Gate) {
	for _, value := range gates {
		var opString string
		switch value.OP {
		case AND:
			opString = "AND"
		case OR:
			opString = "OR"
		case XOR:
			opString = "XOR"
		}
		fmt.Printf("%s %s %s -> %s\n", value.IN1, opString, value.IN2, value.OUT)
	}
	fmt.Println()
}

func computeResult(zs []string, values map[string]bool, gates map[string]*Gate) int {
	for _, z := range zs {
		computeCircuit(z, gates, values)
	}
	return assembleResult(zs, 'z', values)
}

func (d Day24) PartOne(lines []string) string {
	gates, _, _, zs, startingValues := parseDay24(lines)
	result := computeResult(zs, startingValues, gates)
	return strconv.Itoa(result)
}

func permuteAndChooseN(n int, gates *[]*Gate) [][]*Gate {
	var result [][]*Gate
	var helper func(int, []*Gate)

	helper = func(start int, combination []*Gate) {
		if len(combination) == n {
			combinationCopy := make([]*Gate, n)
			copy(combinationCopy, combination)
			result = append(result, combinationCopy)
			return
		}

		for i := start; i < len(*gates); i++ {
			helper(i+1, append(combination, (*gates)[i]))
		}
	}

	helper(0, []*Gate{})
	var actualResult [][]*Gate
	for _, choice := range result {
		for _, permutation := range permute(choice) {
			actualResult = append(actualResult, permutation)
		}
	}
	return actualResult
}

func permute(gates []*Gate) [][]*Gate {
	var result [][]*Gate
	var helper func([]*Gate, int)

	helper = func(currentGates []*Gate, n int) {
		if n == 1 {
			// Make a copy of the current permutation and add to result
			temp := make([]*Gate, len(currentGates))
			copy(temp, currentGates)
			result = append(result, temp)
			return
		}
		for i := 0; i < n; i++ {
			helper(currentGates, n-1)
			if n%2 == 1 {
				// Swap first and last element for odd n
				currentGates[0], currentGates[n-1] = currentGates[n-1], currentGates[0]
			} else {
				// Swap current element with last element for even n
				currentGates[i], currentGates[n-1] = currentGates[n-1], currentGates[i]
			}
		}
	}

	helper(gates, len(gates))
	return result
}

func prettyPrintSwitches(gates []*Gate) string {
	result := make([]string, len(gates))
	for i, gate := range gates {
		result[i] = gate.OUT
	}
	sort.Strings(result)
	return strings.Join(result, ",")
}

func printGraph(gates map[string]*Gate) {
	for _, gate := range gates {
		var s string
		switch gate.OP {
		case AND:
			s = "AND"
		case OR:
			s = "OR"
		case XOR:
			s = "XOR"
		}
		fmt.Printf("%s -> %s_%s\n", gate.IN1, s, gate.OUT)
		fmt.Printf("%s -> %s_%s\n", gate.IN2, s, gate.OUT)
		fmt.Printf("%s_%s -> %s\n", s, gate.OUT, gate.OUT)
	}
}

func swap(gateA *Gate, gateB *Gate, gates map[string]*Gate) {
	gateA.OUT, gateB.OUT = gateB.OUT, gateA.OUT
	gates[gateA.OUT] = gateA
	gates[gateB.OUT] = gateB
}

func (d Day24) PartTwo(lines []string) string {
	gates, xs, ys, zs, startingValues := parseDay24(lines)

	copiedStartingValues := make(map[string]bool)
	for key, value := range startingValues {
		copiedStartingValues[key] = value
	}
	x, y := assembleResult(xs, 'x', copiedStartingValues), assembleResult(ys, 'y', copiedStartingValues)
	expectedOutput := x + y

	gateList := make([]*Gate, len(gates))
	i := 0
	for _, gate := range gates {
		gateList[i] = gate
		i++
	}

	// TODO: I found these values manually by looking at the a graph rendering
	// TODO (continued): Automate finding the values by inspecting the blocks of the carry bit adder
	permutations := [][]*Gate{
		{
			gates["dhg"],
			gates["z06"],
			gates["dpd"],
			gates["brk"],
			gates["z23"],
			gates["bhd"],
			gates["z38"],
			gates["nbf"],
		},
	}
	for _, possibleSwitch := range permutations {
		for i := 0; i < len(possibleSwitch)/2; i++ {
			swap(possibleSwitch[2*i], possibleSwitch[2*i+1], gates)
		}
		copiedStartingValues = make(map[string]bool)
		for key, value := range startingValues {
			copiedStartingValues[key] = value
		}

		computedOutput := computeResult(zs, copiedStartingValues, gates)
		if expectedOutput == computedOutput {
			return prettyPrintSwitches(possibleSwitch)
		}
		for i := 0; i < len(possibleSwitch)/2; i++ {
			swap(possibleSwitch[2*i], possibleSwitch[2*i+1], gates)
		}
	}

	panic("no valid permutations found")
}
