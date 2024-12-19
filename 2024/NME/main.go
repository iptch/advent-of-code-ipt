package main

import (
	"NME/commons"
	"NME/solution"
	"fmt"
	"sort"
	"time"
)

func main() {
	justSome := []commons.Args{
		{Problem: solution.Day20{}, InputFilePartOne: "day-20/example.txt", InputFilePartTwo: "day-20/example.txt"},
	}

	argsToRun := []commons.Args{
		{Problem: solution.Day01{}, InputFilePartOne: "day-01/input.txt", InputFilePartTwo: "day-01/input.txt"},
		{Problem: solution.Day02{}, InputFilePartOne: "day-02/input.txt", InputFilePartTwo: "day-02/input.txt"},
		{Problem: solution.Day03{}, InputFilePartOne: "day-03/input.txt", InputFilePartTwo: "day-03/input.txt"},
		{Problem: solution.Day04{}, InputFilePartOne: "day-04/input.txt", InputFilePartTwo: "day-04/input.txt"},
		{Problem: solution.Day05{}, InputFilePartOne: "day-05/input.txt", InputFilePartTwo: "day-05/input.txt"},
		{Problem: solution.Day06{}, InputFilePartOne: "day-06/input.txt", InputFilePartTwo: "day-06/input.txt"},
		{Problem: solution.Day07{}, InputFilePartOne: "day-07/input.txt", InputFilePartTwo: "day-07/input.txt"},
		{Problem: solution.Day08{}, InputFilePartOne: "day-08/input.txt", InputFilePartTwo: "day-08/input.txt"},
		{Problem: solution.Day09{}, InputFilePartOne: "day-09/input.txt", InputFilePartTwo: "day-09/input.txt"},
		{Problem: solution.Day10{}, InputFilePartOne: "day-10/input.txt", InputFilePartTwo: "day-10/input.txt"},
		{Problem: solution.Day11{}, InputFilePartOne: "day-11/input.txt", InputFilePartTwo: "day-11/input.txt"},
		{Problem: solution.Day12{}, InputFilePartOne: "day-12/input.txt", InputFilePartTwo: "day-12/input.txt"},
		{Problem: solution.Day13{}, InputFilePartOne: "day-13/input.txt", InputFilePartTwo: "day-13/input.txt"},
		{Problem: solution.Day14{}, InputFilePartOne: "day-14/input.txt", InputFilePartTwo: "day-14/input.txt"},
		{Problem: solution.Day15{}, InputFilePartOne: "day-15/input.txt", InputFilePartTwo: "day-15/input.txt"},
		{Problem: solution.Day16{}, InputFilePartOne: "day-16/input.txt", InputFilePartTwo: "day-16/input.txt"},
		{Problem: solution.Day17{}, InputFilePartOne: "day-17/input.txt", InputFilePartTwo: "day-17/input.txt"},
		{Problem: solution.Day18{}, InputFilePartOne: "day-18/input.txt", InputFilePartTwo: "day-18/input.txt"},
		{Problem: solution.Day19{}, InputFilePartOne: "day-19/input.txt", InputFilePartTwo: "day-19/input.txt"},
		{Problem: solution.Day20{}, InputFilePartOne: "day-20/input.txt", InputFilePartTwo: "day-20/input.txt"},
		{Problem: solution.Day21{}, InputFilePartOne: "day-21/input.txt", InputFilePartTwo: "day-21/input.txt"},
		{Problem: solution.Day22{}, InputFilePartOne: "day-22/input.txt", InputFilePartTwo: "day-22/input.txt"},
		{Problem: solution.Day23{}, InputFilePartOne: "day-23/input.txt", InputFilePartTwo: "day-23/input.txt"},
		{Problem: solution.Day24{}, InputFilePartOne: "day-24/input.txt", InputFilePartTwo: "day-24/input.txt"},
		{Problem: solution.Day25{}, InputFilePartOne: "day-25/input.txt", InputFilePartTwo: "day-25/input.txt"},
	}

	if len(justSome) > 0 {
		argsToRun = justSome
	}

	var results []commons.Result
	for _, args := range argsToRun {
		run := commons.Compute(args)
		results = append(results, run.ResultDayOne, run.ResultDayTwo)
	}

	sort.Slice(results, func(i, j int) bool {
		if results[i].Duration == results[j].Duration {
			return results[i].InputFile < results[j].InputFile
		}
		return results[i].Duration > results[j].Duration
	})

	fmt.Println("| ----------------------------- | ------------------ | ------------------------------ |")
	fmt.Println("| Input                         | Execution Duration | Solution                       |")
	fmt.Println("| ----------------------------- | ------------------ | ------------------------------ |")
	for _, result := range results {
		fmt.Printf("| Part %d - %-20s | %15s μs | %30s |\n",
			result.Part,
			result.InputFile,
			commons.FormatWithApostrophe(time.Duration.Microseconds(result.Duration)),
			result.Solution)
	}
	fmt.Println("| ----------------------------- | ------------------ | ------------------------------ |")

	totalDuration := time.Duration(0)
	for _, result := range results {
		totalDuration += result.Duration
	}
	fmt.Println("Total Time:", commons.FormatWithApostrophe(time.Duration.Microseconds(totalDuration)), "μs")

}
