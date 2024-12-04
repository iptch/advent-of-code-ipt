package day02

import (
	"strconv"
	"strings"
)

func isSafe(report []int) bool {
	increasing := report[0] < report[1]

	prev := report[0]
	for i := 1; i < len(report); i++ {
		next := report[i]

		if increasing {
			if prev >= next || next-prev < 1 || next-prev > 3 {
				return false
			}
		} else {
			if prev <= next || prev-next < 1 || prev-next > 3 {
				return false
			}
		}

		prev = next
	}

	return true
}

func parse(lines []string) [][]int {
	var reports [][]int
	for _, line := range lines {
		line := strings.Split(line, " ")
		var report []int
		for _, reading := range line {
			intReading, _ := strconv.Atoi(reading)
			report = append(report, intReading)
		}
		reports = append(reports, report)
	}
	return reports
}

func PartOne(lines []string) string {
	reports := parse(lines)

	safeReports := 0
	for _, report := range reports {
		if isSafe(report) {
			safeReports++
		}
	}
	return strconv.Itoa(safeReports)
}

func PartTwo(lines []string) string {
	reports := parse(lines)

	safeReports := 0
	for _, report := range reports {
		isSafePart2 := false
		for i, _ := range report {
			var amendedReport []int
			for j, _ := range report {
				if i != j {
					amendedReport = append(amendedReport, report[j])
				}
			}
			isSafePart2 = isSafePart2 || isSafe(amendedReport)
		}
		if isSafePart2 {
			safeReports++
		}
	}
	return strconv.Itoa(safeReports)
}
