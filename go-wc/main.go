package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var (
		scanner           = bufio.NewScanner(os.Stdin)
		line, word, bytes uint64
	)

	for scanner.Scan() {
		line++
		bytes += uint64(len(scanner.Bytes())) + 1 // newline
		for _, x := range strings.Split(scanner.Text(), " ") {
			if x != "" {
				word++
			}
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}

	fmt.Println(line, word, bytes)
}
