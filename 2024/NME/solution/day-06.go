package solution

import (
	"strconv"
)

type Position struct {
	X, Y int
	D    Direction
}

type Coordinates struct {
	X, Y int
}

type Direction int

const (
	Up Direction = iota
	Left
	Down
	Right
)

type Terrain int

const (
	Open Terrain = iota
	Blocked
)

func findGuard(lines []string) Position {
	for i, line := range lines {
		for j, char := range line {
			if char == '^' {
				return Position{i, j, Up}
			}
		}
	}
	return Position{-1, -1, Up}
}

func outOfBounds(position Position, grid [][]Terrain) bool {
	return position.X < 0 || position.Y < 0 || position.X >= len(grid) || position.Y >= len(grid)
}

func walk(position Position, grid [][]Terrain) Position {
	if hasObstacleInFront(position, grid) {
		return turn(position)
	}

	return walkForward(position)
}

func hasObstacleInFront(position Position, grid [][]Terrain) bool {
	newPosition := walkForward(position)
	if outOfBounds(newPosition, grid) {
		return false
	}
	return grid[newPosition.X][newPosition.Y] == Blocked
}

func walkForward(position Position) Position {
	switch position.D {
	case Up:
		return Position{position.X - 1, position.Y, Up}
	case Right:
		return Position{position.X, position.Y + 1, Right}
	case Down:
		return Position{position.X + 1, position.Y, Down}
	case Left:
		return Position{position.X, position.Y - 1, Left}
	}
	return position
}

func turn(position Position) Position {
	var newDirection Direction
	switch position.D {
	case Up:
		newDirection = Right
	case Right:
		newDirection = Down
	case Down:
		newDirection = Left
	case Left:
		newDirection = Up
	}
	return Position{position.X, position.Y, newDirection}
}

func (d Day06) PartOne(lines []string) string {
	grid, guardPosition := parseDay06(lines)

	seenPositions := make(map[Coordinates]bool)
	seenPositions[Coordinates{guardPosition.X, guardPosition.Y}] = true
	for {
		guardPosition = walk(guardPosition, grid)
		if outOfBounds(guardPosition, grid) {
			return strconv.Itoa(len(seenPositions))
		}
		seenPositions[Coordinates{guardPosition.X, guardPosition.Y}] = true
	}
}

func parseDay06(lines []string) ([][]Terrain, Position) {
	grid := make([][]Terrain, len(lines))
	guardPosition := Position{}
	for i, line := range lines {
		grid[i] = make([]Terrain, len(line))
		for j, char := range line {
			if char == '^' {
				guardPosition.X, guardPosition.Y = i, j
			}
			if char == '#' {
				grid[i][j] = Blocked
			} else {
				grid[i][j] = Open
			}
		}
	}
	return grid, guardPosition
}

func hasLoop(grid [][]Terrain, guardPosition Position) bool {
	seenPositions := make(map[Position]bool)
	seenPositions[guardPosition] = true
	for {
		guardPosition = walk(guardPosition, grid)
		if outOfBounds(guardPosition, grid) {
			return false
		}

		_, ok := seenPositions[guardPosition]
		if ok {
			return true
		}
		seenPositions[guardPosition] = true
	}
}

func (d Day06) PartTwo(lines []string) string {
	grid, originalGuardPosition := parseDay06(lines)

	guardPosition := Position{originalGuardPosition.X, originalGuardPosition.Y, originalGuardPosition.D}
	visitedPositions := make(map[Coordinates]bool)
	visitedPositions[Coordinates{guardPosition.X, guardPosition.Y}] = true
	for {
		guardPosition = walk(guardPosition, grid)
		if outOfBounds(guardPosition, grid) {
			break
		}
		visitedPositions[Coordinates{guardPosition.X, guardPosition.Y}] = true
	}

	loops := 0
	for visitedPosition := range visitedPositions {
		grid[visitedPosition.X][visitedPosition.Y] = Blocked
		if hasLoop(grid, Position{originalGuardPosition.X, originalGuardPosition.Y, originalGuardPosition.D}) {
			loops++
		}
		grid[visitedPosition.X][visitedPosition.Y] = Open
	}

	return strconv.Itoa(loops)
}
