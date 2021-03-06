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

// Insertion Sort
func insertionSort(items []int) {
	var n = len(items)
	for i := 1; i < n; i++ {
		j := i
		for j > 0 {
			if items[j-1] > items[j] {
				items[j-1], items[j] = items[j], items[j-1]
			}
			j = j - 1
		}
	}
}

// Selection Sort
func selectionSort(items []int) {
	var n = len(items)
	for i := 0; i < n; i++ {
		var minIdx = i
		for j := i; j < n; j++ {
			if items[j] < items[minIdx] {
				minIdx = j
			}
		}
		items[i], items[minIdx] = items[minIdx], items[i]
	}
}
func main() {
	// Testing Bubble Sort
	slice := generateSlice(30)
	fmt.Println("Before Bubble Sort : \n", slice, "\n")
	bubbleSort(slice)
	fmt.Println("After Bubble Sort : \n", slice, "\n")

	// Testing Insertion Sort
	sliceI := generateSlice(20)
	fmt.Println("Before Insertion Sort: \n", sliceI, "\n")
	insertionSort(sliceI)
	fmt.Println("After Insertion Sort: \n", sliceI, "\n")

	// Testing Selection Sort
	sliceS := generateSlice(10)
	fmt.Println("Before Selection Sort: \n", sliceS, "\n")
	selectionSort(sliceS)
	fmt.Println("After Selection Sort: \n", sliceS, "\n")
}
