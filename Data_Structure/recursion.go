package main

import "fmt"

// Factorial
func fac(n int) int {
	if n <= 0 {
		return 1
	}
	return n * fac(n-1)
}

// Fibonacci
func fib() func() int {
	f1 := 0
	f2 := 1
	return func() int {
		f2, f1 = (f1 + f2), f2
		return f1
	}
}

func main() {
	// Test Factorial
	fmt.Println(fac(5)) // Try 5

	fmt.Print("\n")

	// Test Fibonacci
	gen := fib()
	for i := 0; i < 10; i++ {
		fmt.Println(gen())
	}
}
