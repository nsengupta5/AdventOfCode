// Day 1
package main

import (
	"fmt"
	"math"
	"slices"
	"strconv"
	"strings"

	"github.com/nsengupta5/AoC/helper"
)

func getColumns(puzzleInput string) ([]string, []string) {
	pairs := strings.Split(puzzleInput, "\n")
	leftCol := []string{}
	rightCol := []string{}

	for i := range len(pairs) - 1 {
		pair := strings.Split(pairs[i], "   ")
		leftCol = append(leftCol, pair[0])
		rightCol = append(rightCol, pair[1])
	}

	return leftCol, rightCol
}

func getTotalDistance(leftCol []string, rightCol []string) (int, error) {
	var totalDistance float64

	for i := range len(leftCol) {
		leftNum, err := strconv.Atoi(leftCol[i])
		if err != nil {
			return -1, fmt.Errorf("Error coverting left column value to integer: %w", err)
		}
		rightNum, err := strconv.Atoi(rightCol[i])
		if err != nil {
			return -1, fmt.Errorf("Error coverting right column value to integer: %w", err)
		}
		totalDistance += math.Abs(float64(leftNum - rightNum))
	}

	return int(totalDistance), nil
}

func getSimilarityScore(leftCol []string, rightCol []string) (int, error) {
	var similarityScore int
	cache := make(map[string]int)

	var ptr int

	for i := range len(leftCol) {
		val, exists := cache[leftCol[i]]
		if exists {
			similarityScore += val

		} else {
			counts := 0

			leftNum, err := strconv.Atoi(leftCol[i])
			if err != nil {
				return -1, fmt.Errorf("Error coverting left column value to integer: %w", err)
			}

			for j := ptr; j < len(rightCol); j++ {
				rightNum, err := strconv.Atoi(rightCol[j])
				if err != nil {
					return -1, fmt.Errorf("Error coverting right column value to integer: %w", err)
				}

				if rightNum == leftNum {
					counts++
				} else if rightNum > leftNum {
					ptr = j
					break
				}
			}

			score := leftNum * counts
			cache[leftCol[i]] = score
			similarityScore += score
		}
	}
	return similarityScore, nil
}

func main() {
	const day uint8 = 1
	const year uint16 = 2024
	session := helper.GetSession()

	puzzleInput, err := helper.GetPuzzleInput(day, year, session)
	helper.PrintError(err)

	leftCol, rightCol := getColumns(puzzleInput)
	slices.Sort(leftCol)
	slices.Sort(rightCol)

	totalDistance, err := getTotalDistance(leftCol, rightCol)
	helper.PrintError(err)

	similarityScore, err := getSimilarityScore(leftCol, rightCol)
	helper.PrintError(err)

	fmt.Println("Total Distance: ", totalDistance)
	fmt.Println("Total Similarity Score: ", similarityScore)
}
