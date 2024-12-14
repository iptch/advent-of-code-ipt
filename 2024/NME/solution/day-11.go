package solution

import (
	"strconv"
	"strings"
)

type Key struct {
	Stone     int64
	StepsToGo int
}

func parseDay11(line string) []int64 {
	var result []int64
	stringNums := strings.Split(line, " ")
	for _, stringNum := range stringNums {
		num, _ := strconv.ParseInt(stringNum, 10, 64)
		result = append(result, num)
	}
	return result
}

func blink(stones []int64) []int64 {
	var newStones []int64
	for _, stone := range stones {
		stringStone := strconv.FormatInt(stone, 10)
		if stone == 0 {
			newStones = append(newStones, 1)
		} else if len(stringStone)%2 == 0 {
			stoneOne, _ := strconv.ParseInt(stringStone[:len(stringStone)/2], 10, 64)
			stoneTwo, _ := strconv.ParseInt(stringStone[len(stringStone)/2:], 10, 64)
			newStones = append(newStones, stoneOne)
			newStones = append(newStones, stoneTwo)

		} else {
			newStones = append(newStones, stone*2024)
		}
	}
	return newStones
}

func memo_step(stone int64, stepsToGo int, m map[Key]int64) int64 {
	key := Key{stone, stepsToGo}
	if _, exists := m[key]; !exists {
		m[key] = step(stone, stepsToGo, m)
	}
	return m[key]
}

func step(stone int64, stepsToGo int, m map[Key]int64) int64 {
	if stepsToGo == 0 {
		return 1
	}

	stringStone := strconv.FormatInt(stone, 10)
	if stone == 0 {
		return memo_step(1, stepsToGo-1, m)
	} else if len(stringStone)%2 == 0 {
		stoneOne, _ := strconv.ParseInt(stringStone[:len(stringStone)/2], 10, 64)
		stoneTwo, _ := strconv.ParseInt(stringStone[len(stringStone)/2:], 10, 64)
		return memo_step(stoneOne, stepsToGo-1, m) + memo_step(stoneTwo, stepsToGo-1, m)
	} else {
		return memo_step(stone*2024, stepsToGo-1, m)
	}
}

func (d Day11) PartOne(lines []string) string {
	stones := parseDay11(lines[0])

	for i := 0; i < 25; i++ {
		stones = blink(stones)
	}

	return strconv.Itoa(len(stones))
}

func (d Day11) PartTwo(lines []string) string {
	stones := parseDay11(lines[0])

	m := make(map[Key]int64)

	var result int64 = 0
	for _, stone := range stones {
		result += step(stone, 75, m)
	}

	return strconv.FormatInt(result, 10)
}
