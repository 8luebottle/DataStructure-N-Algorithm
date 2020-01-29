package main

import "fmt"

type Stack []string

// Check Empty Stack
func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

// Push
func (s *Stack) Push(str string) {
	*s = append(*s, str)
}

// Pop
func (s *Stack) Pop() (string, bool) {
	if s.IsEmpty() {
		return "", false
	} else {
		index := len(*s) - 1 // Top Most Element
		element := (*s)[index]
		*s = (*s)[:index]
		return element, true
	}
}

func main() {
	var stack Stack

	// Testing
	stack.Push("Late ")
	stack.Push("Night ")
	stack.Push("Coding.")

	for len(stack) > 0 {
		x, y := stack.Pop()
		if y == true {
			fmt.Println(x)
		}
	}
}
