package main

import (
"bufio"
"fmt"
"os"
"strconv"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func part1() {
	file, err := os.Open("input.txt")
  check(err)	
  
  defer file.Close()
  scanner := bufio.NewScanner(file)
  var pos int = 50
	var zero_count int = 0
  
  for scanner.Scan() {
    var line string = scanner.Text()

		var dir string = line[0:1]
		step, err := strconv.Atoi(line[1:]);
		check(err)

		if(dir == "L") {
			pos -= step
		} else {
			pos += step
		}

		pos = pos % 100

		if(pos == 0) {
			zero_count += 1
		}
  }
  fmt.Println("part1: ", zero_count)
}

func part2(){
	file, err := os.Open("input.txt")
  check(err)	
  
  defer file.Close()
  scanner := bufio.NewScanner(file)
  var pos int = 50
	var zero_count int = 0
  
  for scanner.Scan() {
    var line string = scanner.Text()

		var dir string = line[0:1]
		step, err := strconv.Atoi(line[1:]);
		check(err)

		var full_rot int = step / 100
		zero_count += full_rot
		step = step - full_rot * 100

		var newpos int = 0
		if(dir == "L") {
			newpos = pos - step
		} else {
			newpos = pos + step
		}
		
		if (newpos > 100) {
			zero_count += 1
		}
		if(newpos < 0 && pos != 0){
			zero_count += 1
		}

		pos = (newpos + 100) % 100	

		if (pos == 0) {
			zero_count += 1
		}

		fmt.Println("pos: ",pos)
		fmt.Println("zc: ", zero_count)

  }
	fmt.Println("part2: ", zero_count)
}

func main() {
	part1()
	part2()
}
