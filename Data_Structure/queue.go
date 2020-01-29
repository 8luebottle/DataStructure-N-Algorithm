package main

import "fmt"

// to ENQUEUE use built-in append function
func enqueue(queue []int, element int) []int {
	queue = append(queue, element)
	fmt.Println("Enqueued : ", element)
	return queue
}

// to DEQUEUE use Slice off
func dequeue(queue []int) []int {
	element := queue[0]
	fmt.Println("Dequeued : ", element)
	return queue[1:]
}

func main() {
	// Testing Queue & Dequeue
	var queue []int

	queue = enqueue(queue, 100)
	queue = enqueue(queue, 200)
	queue = enqueue(queue, 4500)

	fmt.Println("Queue : ", queue)

	queue = dequeue(queue)
	fmt.Println("Queue : ", queue)

	queue = enqueue(queue, 9999)
	fmt.Println("Queue : ", queue)
}
