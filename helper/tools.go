// Tools for AoC
package helper

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func getSession() string {
	session := os.Getenv("SESSION_ID")
	if session == "" {
		fmt.Println("SESSION_ID not set")
		panic(1)
	}
	return session
}

func GetPuzzleInput(day uint8, year uint16) (string, error) {
	url := fmt.Sprintf("https://adventofcode.com/%d/day/%d/input", year, day)
	session := getSession()

	request, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return "", fmt.Errorf("Error creating request: %w", err)
	}

	request.AddCookie(&http.Cookie{
		Name:  "session",
		Value: session,
	})

	client := http.Client{}
	response, err := client.Do(request)
	if err != nil {
		return "", fmt.Errorf("Error making request: %w", err)
	}
	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		return "", fmt.Errorf("Error reading body: %w", err)
	}

	return string(body), nil
}

func PrintError(err error) {
	if err != nil {
		fmt.Println(err)
		return
	}
}
