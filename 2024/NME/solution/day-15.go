package solution

import (
	"fmt"
	"strconv"
)

type Cell int
type InstructionDirection int

const (
	Wall Cell = iota
	Box
	Empty
)

const (
	UP InstructionDirection = iota
	DOWN
	LEFT
	RIGHT
)

type WideCell int

const (
	WideWall WideCell = iota
	WideEmpty
	WideBoxLeft
	WideBoxRight
)

func parseDay15(lines []string) ([][]Cell, []InstructionDirection, Coordinate2D) {
	var grid [][]Cell
	var instructions []InstructionDirection
	var robot Coordinate2D

	parsingGrid := true
	for i, line := range lines {
		if line == "" {
			parsingGrid = false
			continue
		}

		if parsingGrid {
			grid = append(grid, make([]Cell, len(line)))
			for j, char := range line {
				switch char {
				case '#':
					grid[i][j] = Wall
				case 'O':
					grid[i][j] = Box
				case '.':
					grid[i][j] = Empty
				case '@':
					grid[i][j] = Empty
					robot = Coordinate2D{j, i}
				}
			}
		} else {
			for _, char := range line {
				var instruction InstructionDirection
				switch char {
				case '^':
					instruction = UP
				case 'v':
					instruction = DOWN
				case '<':
					instruction = LEFT
				case '>':
					instruction = RIGHT
				}
				instructions = append(instructions, instruction)
			}
		}
	}
	return grid, instructions, robot
}

func parseDay15Part2(lines []string) ([][]WideCell, []InstructionDirection, Coordinate2D) {
	var grid [][]WideCell
	var instructions []InstructionDirection
	var robot Coordinate2D

	parsingGrid := true
	for i, line := range lines {
		if line == "" {
			parsingGrid = false
			continue
		}

		if parsingGrid {
			grid = append(grid, make([]WideCell, len(line)*2))
			for j, char := range line {
				switch char {
				case '#':
					grid[i][2*j] = WideWall
					grid[i][2*j+1] = WideWall
				case 'O':
					grid[i][2*j] = WideBoxLeft
					grid[i][2*j+1] = WideBoxRight
				case '.':
					grid[i][2*j] = WideEmpty
					grid[i][2*j+1] = WideEmpty
				case '@':
					grid[i][2*j] = WideEmpty
					grid[i][2*j+1] = WideEmpty
					robot = Coordinate2D{2 * j, i}
				}
			}
		} else {
			for _, char := range line {
				var instruction InstructionDirection
				switch char {
				case '^':
					instruction = UP
				case 'v':
					instruction = DOWN
				case '<':
					instruction = LEFT
				case '>':
					instruction = RIGHT
				}
				instructions = append(instructions, instruction)
			}
		}
	}
	return grid, instructions, robot
}

func (cell Cell) toString() rune {
	switch cell {
	case Wall:
		return '#'
	case Box:
		return 'O'
	case Empty:
		return '.'
	}

	panic("unexpected cell")
}

func (cell WideCell) toString() rune {
	switch cell {
	case WideWall:
		return '#'
	case WideBoxLeft:
		return '['
	case WideBoxRight:
		return ']'
	case WideEmpty:
		return '.'
	}

	panic("unexpected cell")
}

func (instruction InstructionDirection) next(current Coordinate2D) Coordinate2D {
	switch instruction {
	case UP:
		return Coordinate2D{current.X, current.Y - 1}
	case DOWN:
		return Coordinate2D{current.X, current.Y + 1}
	case LEFT:
		return Coordinate2D{current.X - 1, current.Y}
	case RIGHT:
		return Coordinate2D{current.X + 1, current.Y}
	}

	panic("invalid instruction")
}

func (cell Coordinate2D) outOfBounds(width int, height int) bool {
	return cell.X < 0 || cell.Y < 0 || cell.X >= width || cell.Y >= height
}

func pushIfPossible(grid [][]Cell, robot Coordinate2D, instruction InstructionDirection) Coordinate2D {
	next := instruction.next(robot)
	for {
		switch grid[next.Y][next.X] {
		case Wall:
			return robot
		case Box:
			next = instruction.next(next)
		case Empty:
			grid[next.Y][next.X] = Box
			firstNext := instruction.next(robot)
			grid[firstNext.Y][firstNext.X] = Empty
			return firstNext
		}
	}
}

func oneStep(grid [][]Cell, instruction InstructionDirection, robot Coordinate2D) Coordinate2D {
	next := instruction.next(robot)

	switch grid[next.Y][next.X] {
	case Empty:
		return next
	case Wall:
		return robot
	case Box:
		return pushIfPossible(grid, robot, instruction)
	}

	panic("invalid cell type")
}

func score(grid [][]Cell) int {
	result := 0
	for i, row := range grid {
		for j, cell := range row {
			if cell == Box {
				result += 100*i + j
			}
		}
	}
	return result
}

func scorePart2(grid [][]WideCell) int {
	result := 0
	for i, row := range grid {
		for j, cell := range row {
			if cell == WideBoxLeft {
				result += 100*i + j
			}
		}
	}
	return result
}

func printGrid(grid [][]Cell, robot Coordinate2D) {
	for i, row := range grid {
		for j, cell := range row {
			if i == robot.Y && j == robot.X {
				fmt.Printf("%c", '@')
			} else {
				fmt.Printf("%c", cell.toString())
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

func printWideGrid(grid [][]WideCell, robot Coordinate2D) {
	for i, row := range grid {
		for j, cell := range row {
			if i == robot.Y && j == robot.X {
				fmt.Printf("%c", '@')
			} else {
				fmt.Printf("%c", cell.toString())
			}
		}
		fmt.Println()
	}
	fmt.Println()
}

func (d Day15) PartOne(lines []string) string {
	grid, instructions, robot := parseDay15(lines)
	for _, instruction := range instructions {
		robot = oneStep(grid, instruction, robot)
	}
	return strconv.Itoa(score(grid))
}

func canPush(grid [][]WideCell, instruction InstructionDirection, cell Coordinate2D) bool {
	next := instruction.next(cell)
	switch grid[next.Y][next.X] {
	case WideWall:
		return false
	case WideEmpty:
		return true
	case WideBoxLeft:
		if instruction == LEFT || instruction == RIGHT {
			return canPush(grid, instruction, next)
		} else {
			return canPush(grid, instruction, next) && canPush(grid, instruction, Coordinate2D{next.X + 1, next.Y})
		}
	case WideBoxRight:
		if instruction == LEFT || instruction == RIGHT {
			return canPush(grid, instruction, next)
		} else {
			return canPush(grid, instruction, next) && canPush(grid, instruction, Coordinate2D{next.X - 1, next.Y})
		}
	}

	panic("invalid next cell type")
}

func push(grid [][]WideCell, instruction InstructionDirection, cell Coordinate2D) {
	next := instruction.next(cell)
	switch grid[next.Y][next.X] {
	case WideWall:
		panic("can not push into a wall")
	case WideEmpty:
		grid[next.Y][next.X] = grid[cell.Y][cell.X]
	case WideBoxLeft:
		if instruction == LEFT || instruction == RIGHT {
			push(grid, instruction, next)
			grid[next.Y][next.X] = grid[cell.Y][cell.X]
		} else {
			push(grid, instruction, next)
			push(grid, instruction, Coordinate2D{next.X + 1, next.Y})
			grid[next.Y][next.X] = grid[cell.Y][cell.X]
			grid[next.Y][next.X+1] = WideEmpty
		}
	case WideBoxRight:
		if instruction == LEFT || instruction == RIGHT {
			push(grid, instruction, next)
			grid[next.Y][next.X] = grid[cell.Y][cell.X]
		} else {
			push(grid, instruction, next)
			push(grid, instruction, Coordinate2D{next.X - 1, next.Y})
			grid[next.Y][next.X] = grid[cell.Y][cell.X]
			grid[next.Y][next.X-1] = WideEmpty
		}
	}
}

func ontStepPart2(grid [][]WideCell, instruction InstructionDirection, robot Coordinate2D) Coordinate2D {
	next := instruction.next(robot)

	switch grid[next.Y][next.X] {
	case WideEmpty:
		return next
	case WideWall:
		return robot
	case WideBoxLeft, WideBoxRight:
		if canPush(grid, instruction, robot) {
			push(grid, instruction, robot)
			return next
		} else {
			return robot
		}
	}

	panic("invalid cell type")
}

func (d Day15) PartTwo(lines []string) string {
	grid, instructions, robot := parseDay15Part2(lines)
	for _, instruction := range instructions {
		robot = ontStepPart2(grid, instruction, robot)
	}
	return strconv.Itoa(scorePart2(grid))
}
