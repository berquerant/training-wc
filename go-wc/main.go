package main

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"os"
	"unicode"
)

func main() {
	var (
		reader = bufio.NewReader(os.Stdin)

		line  int
		word  int
		bytes int

		prevIsSpace bool
		isTail      bool
		metChar     bool
	)

	for {
		r, size, err := reader.ReadRune()
		isEOF := errors.Is(err, io.EOF)
		if !isEOF && err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(1)
		}

		bytes += size
		isSpace := unicode.IsSpace(r)

		switch {
		case isSpace:
			if r == '\n' {
				line++
			}
		case prevIsSpace && isTail && metChar:
			// space non-space
			// and have encountered a char except space before the rune
			word++
		}

		if isEOF {
			break
		}

		prevIsSpace = isSpace
		isTail = true
		if !metChar && !isSpace {
			metChar = true
		}
	}

	fmt.Println(line, word, bytes)
}
