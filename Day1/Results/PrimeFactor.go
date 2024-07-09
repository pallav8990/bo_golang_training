package main

import (
	"fmt"
	"math"
)

// Function to check if a number is prime
func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// Function to find two factors of a non-prime number
func findFactors(n int) (int, int) {
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return i, n / i
		}
	}
	return 1, n // fallback, should never hit this
}

func main() {
	for i := 2; i <= 25; i++ {
		if isPrime(i) {
			fmt.Printf("%d is  prime\n", i)
		} else {
			factor1, factor2 := findFactors(i)
			fmt.Printf("%d is product of %d * %d\n", i, factor1, factor2)
		}
	}
}
