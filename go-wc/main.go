package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var (
		scanner = bufio.NewScanner(os.Stdin)

		line  int
		word  int
		bytes int
	)

	for scanner.Scan() {
		line++
		bytes += len(scanner.Bytes()) + 1 // newline
		for _, x := range strings.Split(scanner.Text(), " ") {
			if x != "" {
				word++
			}
		}
	}

	fmt.Println(line, word, bytes)
}
