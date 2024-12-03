package main

import (
	"NME/commons"
	day01 "NME/day-01"
	day02 "NME/day-02"
	day03 "NME/day-03"
	day04 "NME/day-04"
)

func main() {
	commons.Run(day01.PartOne, day01.PartTwo, "/day-01/input.txt")
	commons.Run(day02.PartOne, day02.PartTwo, "/day-02/input.txt")
	commons.Run(day03.PartOne, day03.PartTwo, "/day-03/input.txt")
	commons.Run(day04.PartOne, day04.PartTwo, "/day-04/input.txt")
}
