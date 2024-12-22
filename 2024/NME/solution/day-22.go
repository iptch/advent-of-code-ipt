package solution

import (
	"strconv"
)

const (
	modulo       = 16777216
	iterations   = 2000
	sequenceSize = 4
)

func customHash(seed int) int {
	seed = seed ^ (seed<<6)%modulo
	seed = seed ^ (seed>>5)%modulo
	seed = seed ^ (seed<<11)%modulo
	return seed
}

func (d Day22) PartOne(lines []string) string {
	var result = 0
	for _, line := range lines {
		seed, _ := strconv.Atoi(line)
		for i := 0; i < iterations; i++ {
			seed = customHash(seed)
		}
		result += seed
	}
	return strconv.Itoa(result)
}

func (d Day22) PartTwo(lines []string) string {
	result := 0
	scores := map[[4]int]int{}

	for _, line := range lines {
		seed, _ := strconv.Atoi(line)
		var sequence = [sequenceSize]int{}
		currentScores := map[[4]int]int{}
		for j := 0; j < iterations; j++ {
			nextSeed := customHash(seed)
			previousPrice := seed % 10
			currentPrice := nextSeed % 10
			diff := currentPrice - previousPrice
			newSequence := [sequenceSize]int{}
			for k := 0; k < sequenceSize-1; k++ {
				newSequence[k] = sequence[k+1]
			}
			newSequence[sequenceSize-1] = diff

			if j >= sequenceSize {
				if _, foundInThisSequence := currentScores[newSequence]; foundInThisSequence == false {
					currentScores[newSequence] = currentPrice
					if _, foundInOtherSequences := scores[newSequence]; foundInOtherSequences {
						scores[newSequence] += currentPrice
					} else {
						scores[newSequence] = currentPrice
					}
				}
			}

			sequence = newSequence
			seed = nextSeed
		}
	}

	for _, value := range scores {
		result = max(result, value)
	}

	return strconv.Itoa(result)

}
