package commons

import (
	"bufio"
	"fmt"
	"os"
	"time"
)

func timeIt(function func([]string) string, args []string) (string, time.Duration) {
	start := time.Now()
	result := function(args)
	elapsed := time.Since(start)

	return result, elapsed
}

func Run(partOne func([]string) string, partTwo func([]string) string, inputFile string) {

	workingDir, err := os.Getwd()
	if err != nil {
		panic(err)
	}

	readFile, err := os.Open(workingDir + inputFile)
	if err != nil {
		panic(err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	// two lists so they can be modified by the solving functions
	var listPartOne []string
	var listPartTwo []string

	for fileScanner.Scan() {
		line := fileScanner.Text()
		// strings are immutable, this is fine
		listPartOne = append(listPartOne, line)
		listPartTwo = append(listPartTwo, line)
	}

	timePartOne, resultPartOne := timeIt(partOne, listPartOne)
	timePartTwo, resultPartTwo := timeIt(partTwo, listPartTwo)

	fmt.Printf("| %-30s| %-10s|%30s |\n", inputFile+` - Part 1`, resultPartOne, timePartOne)
	fmt.Printf("| %-30s| %-10s|%30s |\n", inputFile+` - Part 2`, resultPartTwo, timePartTwo)
}
