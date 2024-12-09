package day09

import (
	"strconv"
)

func expand(line string) ([]int, [][]int) {
	var result []int
	var emptySpaces [][]int

	on := true
	fileId := 0
	for _, char := range line {
		digit, _ := strconv.Atoi(string(char))

		toAppend := fileId
		if !on {
			toAppend = -1
			emptySpaces = append(emptySpaces, []int{len(result), digit})
		}

		for i := 0; i < digit; i++ {
			result = append(result, toAppend)
		}

		if on {
			fileId++
		}

		on = !on
	}
	return result, emptySpaces

}

func moveRight(expanded []int, idx int) int {
	for {
		if expanded[idx] != -1 {
			idx++
		} else {
			return idx
		}
	}
}

func moveLeft(expanded []int, idx int) int {
	for {
		if idx > 0 && expanded[idx] == -1 {
			idx--
		} else {
			return idx
		}
	}
}

func compact(expanded []int) {
	idxFree, idxEnd := moveRight(expanded, 0), moveLeft(expanded, len(expanded)-1)

	for {
		if idxFree >= idxEnd {
			break
		}

		expanded[idxFree], expanded[idxEnd] = expanded[idxEnd], expanded[idxFree]

		idxFree, idxEnd = moveRight(expanded, idxFree+1), moveLeft(expanded, idxEnd-1)
	}
}

func findStart(expanded []int, idx int) (int, int) {
	val := expanded[idx]
	size := 0
	for {
		if idx == -1 || val != expanded[idx] {
			return idx + 1, size
		}

		idx--
		size++
	}
}

func compactPart2(expanded []int, emptySpaces [][]int) {
	endBlockToMove := moveLeft(expanded, len(expanded)-1)

	for {
		startBlockToMove, sizeOfBlockToMove := findStart(expanded, endBlockToMove)
		if startBlockToMove == 0 {
			break
		}

		for i := 0; i < len(emptySpaces); i++ {
			if emptySpaces[i][0] < startBlockToMove && emptySpaces[i][1] >= sizeOfBlockToMove {
				startEmptySpace := emptySpaces[i][0]
				for j := 0; j < sizeOfBlockToMove; j++ {
					expanded[startEmptySpace+j], expanded[startBlockToMove+j] = expanded[startBlockToMove+j], expanded[startEmptySpace+j]
				}
				emptySpaces[i][0] += sizeOfBlockToMove
				emptySpaces[i][1] -= sizeOfBlockToMove
				break
			}
		}
		endBlockToMove = moveLeft(expanded, startBlockToMove-1)
	}
}

func computeChecksum(expanded []int) int64 {
	var result int64 = 0
	for i, n := range expanded {
		if n >= 0 {
			result += int64(i) * int64(n)
		}
	}
	return result
}

func PartOne(lines []string) string {
	expanded, _ := expand(lines[0])
	compact(expanded)
	checksum := computeChecksum(expanded)

	return strconv.FormatInt(checksum, 10)
}

func PartTwo(lines []string) string {
	expanded, emptySpaces := expand(lines[0])
	compactPart2(expanded, emptySpaces)
	checksum := computeChecksum(expanded)

	return strconv.FormatInt(checksum, 10)
}
