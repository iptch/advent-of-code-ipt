package commons

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type Args struct {
	Function  func([]string) string
	Day       int
	Part      int
	InputFile string
}

type Result struct {
	Solution string
	Duration time.Duration
}

type Run struct {
	Args   Args
	Result Result
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

func Compute(args Args) Result {

	workingDir, err := os.Getwd()
	if err != nil {
		panic(err)
	}

	dayString := strconv.Itoa(args.Day)
	if args.Day < 10 {
		dayString = "0" + dayString
	}

	readFile, err := os.Open(fmt.Sprintf("%s/day-%s/%s", workingDir, dayString, args.InputFile))
	if err != nil {
		panic(err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	var input []string

	for fileScanner.Scan() {
		input = append(input, fileScanner.Text())
	}

	solution, duration := timeIt(args.Function, input)

	return Result{solution, duration}
}
