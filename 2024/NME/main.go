package main

import (
	"NME/commons"
	day01 "NME/day-01"
	day02 "NME/day-02"
	day03 "NME/day-03"
	day04 "NME/day-04"
	day05 "NME/day-05"
	day06 "NME/day-06"
	day07 "NME/day-07"
	day08 "NME/day-08"
	day09 "NME/day-09"
	day10 "NME/day-10"
	"fmt"
	"sort"
	"time"
)

func main() {
	justSome := []commons.Args{
		{day10.PartOne, 10, 1, "input.txt"},
		{day10.PartTwo, 10, 2, "input.txt"},
	}

	argsToRun := []commons.Args{
		{day01.PartOne, 1, 1, "input.txt"},
		{day01.PartTwo, 1, 2, "input.txt"},
		{day02.PartOne, 2, 1, "input.txt"},
		{day02.PartTwo, 2, 2, "input.txt"},
		{day03.PartOne, 3, 1, "input.txt"},
		{day03.PartTwo, 3, 2, "input.txt"},
		{day04.PartOne, 4, 1, "input.txt"},
		{day04.PartTwo, 4, 2, "input.txt"},
		{day05.PartOne, 5, 1, "input.txt"},
		{day05.PartTwo, 5, 2, "input.txt"},
		{day06.PartOne, 6, 1, "input.txt"},
		{day06.PartTwo, 6, 2, "input.txt"},
		{day07.PartOne, 7, 1, "input.txt"},
		{day07.PartTwo, 7, 2, "input.txt"},
		{day08.PartOne, 8, 1, "input.txt"},
		{day08.PartTwo, 8, 2, "input.txt"},
		{day09.PartOne, 9, 1, "input.txt"},
		{day09.PartTwo, 9, 2, "input.txt"},
		{day10.PartOne, 10, 1, "input.txt"},
		{day10.PartTwo, 10, 2, "input.txt"},
	}

	if len(justSome) != 0 {
		argsToRun = justSome
	}

	var runs []commons.Run
	for _, args := range argsToRun {
		runs = append(runs, commons.Run{Args: args, Result: commons.Compute(args)})
	}

	sort.Slice(runs, func(i, j int) bool {
		return runs[i].Result.Duration > runs[j].Result.Duration
	})

	fmt.Println("| ------ | ------------------ | ------------------------------ |")
	fmt.Println("| Puzzle | Execution Duration | Solution                       |")
	fmt.Println("| ------ | ------------------ | ------------------------------ |")
	for _, run := range runs {
		fmt.Printf("| %4d_%d | %15s μs | %30s |\n",
			run.Args.Day,
			run.Args.Part,
			commons.FormatWithApostrophe(time.Duration.Microseconds(run.Result.Duration)),
			run.Result.Solution)
	}
	fmt.Println("| ------ | ------------------ | ------------------------------ |")

	totalDuration := time.Duration(0)
	for _, run := range runs {
		totalDuration += run.Result.Duration
	}
	fmt.Println("Total Time:", commons.FormatWithApostrophe(time.Duration.Microseconds(totalDuration)), "μs")
}
