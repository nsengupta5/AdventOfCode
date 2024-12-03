// Day 2
package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"

	"github.com/nsengupta5/AdventOfCode/helper"
)

func getReports(strReports []string) (reports [][]int, err error) {
	for _, strReport := range strReports {
		intReport, err := covertLevelsToInts(strReport)
		if err != nil {
			return nil, err
		}
		reports = append(reports, intReport)
	}

	return
}

func covertLevelsToInts(report string) (intLevels []int, err error) {
	arrReport := strings.Split(report, " ")

	for _, level := range arrReport {
		intLevel, err := strconv.Atoi(level)
		if err != nil {
			return nil, fmt.Errorf("Error converting level to integer: %w", err)
		}
		intLevels = append(intLevels, intLevel)
	}

	return
}

func isSafeReport(report []int) bool {
	return isConsistentlyIncreasingOrDecreasing(report) && isValidAdjacentRange(report)
}

func isValidAdjacentRange(report []int) bool {
	var leftPtr = 0
	var rightPtr = 1

	for rightPtr < len(report) {
		distance := math.Abs(float64(report[leftPtr]) - float64(report[rightPtr]))
		if distance < 1 || distance > 3 {
			return false
		}
		leftPtr++
		rightPtr++
	}

	return true
}

func isConsistentlyIncreasingOrDecreasing(report []int) bool {
	var isIncreasing int8 = -1

	for i := range len(report) - 1 {
		switch isIncreasing {
		case -1:
			if report[i+1] > report[i] {
				isIncreasing = 1
			} else {
				isIncreasing = 0
			}
		case 0:
			if report[i+1] > report[i] {
				return false
			}
		case 1:
			if report[i+1] < report[i] {
				return false
			}
		}
	}

	return true
}

func getNumOfSafeReports(reports [][]int) (numSafeReports int) {
	for _, report := range reports {
		if isSafeReport(report) {
			numSafeReports++
		} else {
			for idx := 0; idx < len(report); idx++ {
				modifiedReport := make([]int, 0, len(report)-1)
				modifiedReport = append(modifiedReport, report[:idx]...)
				modifiedReport = append(modifiedReport, report[idx+1:]...)

				if isSafeReport(modifiedReport) {
					numSafeReports++
					break
				}
			}
		}
	}
	return
}

func main() {
	const day uint8 = 2
	const year uint16 = 2024

	puzzleInput, err := helper.GetPuzzleInput(day, year)

	helper.PrintError(err)

	strReports := strings.Split(puzzleInput, "\n")
	reports, err := getReports(strReports[:len(strReports)-1])
	helper.PrintError(err)

	numSafeReports := getNumOfSafeReports(reports)
	fmt.Println("Total number of safe reports:", numSafeReports)
}
