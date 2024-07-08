package main

import (
	"fmt"
	"strconv"
)

func fizzBuzz(i int) string {
	var result string

	if i%3 == 0 && i%5 == 0 {
		result = strconv.Itoa(i) + ":FizzBuzz"
		//fmt.Printf("%d: FizzBuzz\n", i)
	} else if i%3 == 0 {
		//fmt.Printf("%d: Fizz\n", i)
		result = strconv.Itoa(i) + ":Fizz"
	} else if i%5 == 0 {
		//fmt.Printf("%d: Buzz\n", i)
		result = strconv.Itoa(i) + ":Buzz"
	} else {
		//	fmt.Printf("%d\n", i)
		result = strconv.Itoa(i)
	}
	return result
}

func main() {
	for i := 1; i <= 100; i++ {
		fmt.Printf("%s\n", fizzBuzz(i))
	}
}
