package main

import (
	"fmt"
	"math/rand"
	"time"
)

func generateSlice(size int) []int {
	slice := make([]int, size, size)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < size; i++ {
		slice[i] = rand.Intn(999) - rand.Intn(999)
	}
	return slice
}

// Bubble Sort
func bubbleSort(items []int) {
	var (
		n      = len(items)
		sorted = false
	)
	for !sorted {
		swapped := false
		for i := 0; i < n-1; i++ {
			if items[i] > items[i+1] {
				items[i+1], items[i] = items[i], items[i+1]
				swapped = true
			}
		}
		if !swapped {
			sorted = true
		}
		n = n - 1
	}
}

func main() {
	// Testing Bubble Sort
	slice := generateSlice(30)
	fmt.Println("Before Bubble Sort : \n", slice, "\n")
	bubbleSort(slice)
	fmt.Println("After Bubble Sort : \n", slice, "\n")
}
