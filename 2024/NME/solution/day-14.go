package solution

import (
	"fmt"
	"regexp"
	"strconv"
)

type Robot struct {
	X, Y   int
	dX, dY int
}

// W width, H height for input file
var W = 101
var H = 103

// W width, H height for example file
//var W = 11
//var H = 7

func parseDay14(lines []string) []Robot {
	robots := make([]Robot, len(lines))
	for i, line := range lines {
		r := regexp.MustCompile(`p=(\d+),(\d+) v=(-?\d+),(-?\d+)`)
		matches := r.FindStringSubmatch(line)

		X, _ := strconv.Atoi(matches[1])
		Y, _ := strconv.Atoi(matches[2])
		dX, _ := strconv.Atoi(matches[3])
		dY, _ := strconv.Atoi(matches[4])

		robots[i] = Robot{X, Y, dX, dY}
	}
	return robots
}

func stepDay14(robots []Robot) []Robot {
	for i, robot := range robots {
		robots[i] = Robot{(robot.X + robot.dX + W) % W, (robot.Y + robot.dY + H) % H, robot.dX, robot.dY}
	}
	return robots
}

func printRobots(robots []Robot) {
	grid := make([][]int, H)
	for i := range grid {
		grid[i] = make([]int, W)
		for j := range grid[i] {
			grid[i][j] = 0
		}
	}
	for _, robot := range robots {
		grid[robot.Y][robot.X] += 1
	}
	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == 0 {
				fmt.Printf(".")
			} else {
				fmt.Printf("%d", grid[i][j])
			}
		}
		fmt.Printf("\n")
	}
	fmt.Printf("\n")
}

func computeScore(robots []Robot) int {
	Q1, Q2, Q3, Q4 := 0, 0, 0, 0
	for _, robot := range robots {
		if robot.X < W/2 {
			if robot.Y < H/2 {
				Q1 += 1
			} else if robot.Y > H/2 {
				Q2 += 1
			}
		} else if robot.X > W/2 {
			if robot.Y < H/2 {
				Q3 += 1
			} else if robot.Y > H/2 {
				Q4 += 1
			}
		}
	}
	return Q1 * Q2 * Q3 * Q4
}

func (d Day14) PartOne(lines []string) string {
	robots := parseDay14(lines)

	for i := 0; i < 100; i++ {
		robots = stepDay14(robots)
	}
	score := computeScore(robots)
	return strconv.Itoa(score)
}

func hasChristmasTree(robots []Robot) bool {
	/*
		The christmas tree looks like this and is embedded somewhere in the grid - it does not occupy the full grid.
		Searching for the top frame is enough.

		1111111111111111111111111111111
		1.............................1
		1.............................1
		1.............................1
		1.............................1
		1..............1..............1
		1.............111.............1
		1............11111............1
		1...........1111111...........1
		1..........111111111..........1
		1............11111............1
		1...........1111111...........1
		1..........111111111..........1
		1.........11111111111.........1
		1........1111111111111........1
		1..........111111111..........1
		1.........11111111111.........1
		1........1111111111111........1
		1.......111111111111111.......1
		1......11111111111111111......1
		1........1111111111111........1
		1.......111111111111111.......1
		1......11111111111111111......1
		1.....1111111111111111111.....1
		1....111111111111111111111....1
		1.............111.............1
		1.............111.............1
		1.............111.............1
		1.............................1
		1.............................1
		1.............................1
		1.............................1
		1111111111111111111111111111111
	*/

	grid := make([][]bool, H)
	for i := range grid {
		grid[i] = make([]bool, W)
		for j := range grid[i] {
			grid[i][j] = false
		}
	}
	for _, robot := range robots {
		grid[robot.Y][robot.X] = true
	}
	for i := range grid {
		maxContiguous := 0
		currentContiguous := 0
		for j := range grid[i] {
			if !grid[i][j] {
				currentContiguous = 0
			} else {
				currentContiguous++
			}
			maxContiguous = max(maxContiguous, currentContiguous)
		}
		if maxContiguous > 30 {
			return true
		}
	}

	return false
}

func (d Day14) PartTwo(lines []string) string {
	robots := parseDay14(lines)

	for i := 1; i < 10000; i++ {
		robots = stepDay14(robots)
		if hasChristmasTree(robots) {
			return strconv.Itoa(i)
		}
	}

	return "-1"
}
