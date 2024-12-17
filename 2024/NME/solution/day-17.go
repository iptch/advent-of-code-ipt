package solution

import (
	"regexp"
	"strconv"
	"strings"
)

type Program struct {
	RegisterA, RegisterB, RegisterC int64
	Instructions                    []*Instruction
	InstructionPointer              int64
	OutputBuffer                    []int64
}

type Instruction struct {
	OpCode int64
	Name   string
}

var adv = Instruction{0, "adv"}
var bxl = Instruction{1, "bxl"}
var bst = Instruction{2, "bst"}
var jnz = Instruction{3, "jnz"}
var bxc = Instruction{4, "bxc"}
var out = Instruction{5, "out"}
var bdv = Instruction{6, "bdv"}
var cdv = Instruction{7, "cdv"}

var opCodeToInstruction = map[string]*Instruction{
	"0": &adv,
	"1": &bxl,
	"2": &bst,
	"3": &jnz,
	"4": &bxc,
	"5": &out,
	"6": &bdv,
	"7": &cdv,
}

func (p *Program) Run() {
	for int(p.InstructionPointer) < len(p.Instructions) {
		p.Instructions[p.InstructionPointer].Execute(p)
	}
}

func (i *Instruction) Execute(program *Program) {
	switch i.OpCode {
	case adv.OpCode:
		program.RegisterA = program.RegisterA / (1 << program.ComboOperand())
		program.NextInstruction()
	case bxl.OpCode:
		program.RegisterB = program.RegisterB ^ program.LiteralOperand()
		program.NextInstruction()
	case bst.OpCode:
		program.RegisterB = program.ComboOperand() % 8
		program.NextInstruction()
	case jnz.OpCode:
		if program.RegisterA == 0 {
			program.NextInstruction()
		} else {
			program.InstructionPointer = program.LiteralOperand()
		}
	case bxc.OpCode:
		program.RegisterB = program.RegisterB ^ program.RegisterC
		program.NextInstruction()
	case out.OpCode:
		program.OutputBuffer = append(program.OutputBuffer, program.ComboOperand()%8)
		program.NextInstruction()
	case bdv.OpCode:
		program.RegisterB = program.RegisterA / (1 << program.ComboOperand())
		program.NextInstruction()
	case cdv.OpCode:
		program.RegisterC = program.RegisterA / (1 << program.ComboOperand())
		program.NextInstruction()
	}
}

func (p *Program) Equal(other []int64) bool {
	if len(p.OutputBuffer) != len(other) {
		return false
	}

	for i := 0; i < len(p.OutputBuffer); i++ {
		if p.OutputBuffer[i] != other[i] {
			return false
		}
	}

	return true
}

func (p *Program) Reset() {
	var outputBuffer []int64
	p.OutputBuffer = outputBuffer
	p.InstructionPointer = 0
}

func (p *Program) NextInstruction() {
	p.InstructionPointer += 2
}

func (p *Program) LiteralOperand() int64 {
	return p.Instructions[p.InstructionPointer+1].OpCode
}

func (p *Program) ComboOperand() int64 {
	n := p.LiteralOperand()
	switch n {
	case 0, 1, 2, 3:
		return n
	case 4:
		return p.RegisterA
	case 5:
		return p.RegisterB
	case 6:
		return p.RegisterC
	default:
		panic("invalid operand")
	}
}

func parseDay17(lines []string) *Program {
	re := regexp.MustCompile(`\d+`)
	rax, _ := strconv.Atoi(re.FindAllStringSubmatch(lines[0], -1)[0][0])
	rbx, _ := strconv.Atoi(re.FindAllStringSubmatch(lines[1], -1)[0][0])
	rcx, _ := strconv.Atoi(re.FindAllStringSubmatch(lines[2], -1)[0][0])

	var ins []*Instruction
	for _, match := range re.FindAllStringSubmatch(lines[4], -1) {
		instruction := opCodeToInstruction[match[0]]
		ins = append(ins, instruction)
	}

	var outputBuffer []int64
	return &Program{int64(rax), int64(rbx), int64(rcx), ins, 0, outputBuffer}
}

func printNumbers(numbers []int64) string {
	var strNumbers []string
	for _, num := range numbers {
		strNumbers = append(strNumbers, strconv.FormatInt(num, 10))
	}
	return strings.Join(strNumbers, ",")
}

func (d Day17) PartOne(lines []string) string {
	program := parseDay17(lines)
	program.Run()
	return printNumbers(program.OutputBuffer)
}

func (d Day17) PartTwo(lines []string) string {
	/*
		The program runs in a loop, cutting off the last three bits of register A in every iteration until A==0.

		One number between 1 and 8 gets printed in every iteration, and that number depends only on the value of A.

		In other words, output = f(A), where f is some function that only depends on A.

		For our input, say [1,2,4,7], we need a number N with {len(input) * bits} such that
		 f(N[0:3])  = 7
		 f(N[0:6])  = 4
		 f(N[0:9])  = 2
		 f(N[0:12]) = 1

		We start by looking for the last number in our input, searching all 0-7 possible numbers and keep track of
		all possible solutions.

		Then we go to number 4 and search bits 3,4,5, while leaving the bits 0,1,2 fixed from our previously
		found solutions.

		This goes on until we reach the first number in our input.

		It is theoretically possible that we don't find an input, but the example is constructed in such a way that
		we will always find an input.
	*/
	program := parseDay17(lines)
	reversedInstructions := make([]int64, len(program.Instructions))
	for i, instruction := range program.Instructions {
		reversedInstructions[len(program.Instructions)-1-i] = instruction.OpCode
	}

	results := []int64{0}
	for _, targetInstruction := range reversedInstructions {
		var newResults []int64
		for _, previousResult := range results {
			var j int64
			for j = 0; j < 8; j++ {
				// shift the previously found result by 3 bits to the left, making space for the next partial result
				newPotentialResult := (previousResult << 3) + j
				// setup and run the program for the new partial result
				program.Reset()
				program.RegisterA = newPotentialResult
				program.Run()
				// if the first output of the program matches the instruction we are looking for, we store the partial result
				if program.OutputBuffer[0] == targetInstruction {
					newResults = append(newResults, newPotentialResult)
				}
			}
		}
		results = newResults

	}

	// We are asked for return the smallest result. Because of the way we search (from smallest to biggest option),
	// the smallest result will always be in first position.
	return strconv.FormatInt(results[0], 10)
}
