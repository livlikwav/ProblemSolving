package main

import (
	"fmt"
)

func main() {
	var A, B int32
	fmt.Scan(&A, &B)
	fmt.Printf("%v\n%v\n%v\n%v\n%v", A+B, A-B, A*B, A/B, A%B)
}
