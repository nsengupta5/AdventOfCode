package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getNumFromLine(line string) int {
	var number string
	lineLen := len(line)

	for i := 0; i < lineLen; i++ {
		if unicode.IsDigit(rune(line[i])) {
			number += string(line[i])
			break
		}
	}

	for i := lineLen - 1; i >= 0; i-- {
		if unicode.IsDigit(rune(line[i])) {
			number += string(line[i])
			break
		}
	}

	result, err := strconv.Atoi(number)
	check(err)
	return result
}

func main() {
	file, err := os.Open("./input.txt")
	check(err)
	defer file.Close()

	var total int
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		total += getNumFromLine(scanner.Text())
	}

	fmt.Println(total)
}
