// Day 1
package main

import (
	"fmt"
	"io"
	"net/http"
)

func getPuzzleInput(url string) (string, error) {
	response, err := http.Get(url)
	if err != nil {
		return "", fmt.Errorf("Error fetching url: %w", err)
	}

	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		return "", fmt.Errorf("Error reading body: %w", err)
	}

	return string(body), nil
}

func main() {
	url := "https://adventofcode.com/2024/day/1/input"
	puzzleInput, err := getPuzzleInput(url)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(puzzleInput)
}
