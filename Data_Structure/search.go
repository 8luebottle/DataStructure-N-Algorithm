package main

// Binary Search from Go Library
func binarySearch(n int, f func(int) bool) int {
	// Define f(-1) == false and f(n) == true
	// Array : n  Comparison function : f

	i, j := 0, n
	for i < j {
		h := i + (j-i)/2 // avoid Overflow when computing h

		if !f(h) { // i <= h < j
			i = h + 1 // preserves f(i-1) == false
		} else {
			j = h // preserves f(j) == true
		}
	}
	return i
}
