package main

import "fmt"

func Sum(numbers []int) int {
	sum := 0
	for _, val := range numbers {
		sum += val
	}
	fmt.Println("sum : ", sum)
	return sum
}

func main() {
	fmt.Println("")
	Sum([]int{1, 2, 3, 4, 5}) // 15
	Sum([]int{3, 5, 3, 5, 3}) // 19
	Sum(nil)                  // 0
}
