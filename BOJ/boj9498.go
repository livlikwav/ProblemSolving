package main

import (
	"fmt"
)

func main() {
	var A int32
	fmt.Scan(&A)
	switch {
	case 100 >= A && A >= 90:
		fmt.Println("A")
	case 90 > A && A >= 80:
		fmt.Println("B")
	case 80 > A && A >= 70:
		fmt.Println("C")
	case 70 > A && A >= 60:
		fmt.Println("D")
	default:
		fmt.Println("F")

	}

}
