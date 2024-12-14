package commons

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type Problem interface {
	PartOne(lines []string) string
	PartTwo(lines []string) string
}

type Args struct {
	Problem          Problem
	InputFilePartOne string
	InputFilePartTwo string
}

type Result struct {
	Solution  string
	Duration  time.Duration
	InputFile string
	Part      int
}

type Run struct {
	Args         Args
	ResultDayOne Result
	ResultDayTwo Result
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func timeIt(function func([]string) string, args []string) (string, time.Duration) {
	start := time.Now()
	solution := function(args)
	elapsed := time.Since(start)

	return solution, elapsed
}

func FormatWithApostrophe(n int64) string {
	reversed := reverseString(strconv.FormatInt(n, 10))

	// Insert apostrophes every 3 characters
	var builder strings.Builder
	for i, r := range reversed {
		if i > 0 && i%3 == 0 {
			builder.WriteRune('\'')
		}
		builder.WriteRune(r)
	}

	return reverseString(builder.String())
}

func Compute(args Args) Run {
	inputPartOne := readLines(args.InputFilePartOne)
	inputPartTwo := readLines(args.InputFilePartTwo)

	solutionDayOne, durationDayOne := timeIt(args.Problem.PartOne, inputPartOne)
	solutionDayTwo, durationDayTwo := timeIt(args.Problem.PartTwo, inputPartTwo)

	return Run{
		Args: args,
		ResultDayOne: Result{
			Solution:  solutionDayOne,
			Duration:  durationDayOne,
			InputFile: args.InputFilePartOne,
			Part:      1,
		},
		ResultDayTwo: Result{
			Solution:  solutionDayTwo,
			Duration:  durationDayTwo,
			InputFile: args.InputFilePartTwo,
			Part:      2,
		},
	}
}

func readLines(inputFile string) []string {
	workingDir, err := os.Getwd()
	if err != nil {
		panic(err)
	}

	file, err := os.Open(fmt.Sprintf("%s/solution/inputs/%s", workingDir, inputFile))
	if err != nil {
		panic(err)
	}

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	var input []string

	for fileScanner.Scan() {
		input = append(input, fileScanner.Text())
	}

	return input
}
