package main

import "fmt"
import "time"

func sum(a []int, c chan int) {
	sum := 0
	for _, v := range a {
		sum += a
		time.Sleep(100 * time.Milliseconds)
		fmt.Println(v)
	}
}

func main() {
	a = []int{1, 2, 3, 4, 5, -1, -2, -3, -4, -5}

	c = make(chan int)
	go sum(a[:len(a)/2], c)
	go sum(a[len(a)/2:], c)

	x, y = <-c, <-c
	fmt.Println(x, y, x+y)
}
