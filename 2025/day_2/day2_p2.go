package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func powInt(base, exp int) int {
	result := 1
	for range exp {
		result *= base
	}
	return result
}

func main() {

	fmt.Println("day2")

	file, err := os.Open("input_t.txt")
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	scanner.Scan()

    result := 0
	for nums := range strings.SplitSeq(scanner.Text(), ",") {
		splitted := strings.Split(nums, "-")
		low, _ := strconv.Atoi(splitted[0])
		high, _ := strconv.Atoi(splitted[1])
		fmt.Println(low, high)

        for i:=low; i<=high; i++ { 
            if check_invalid(strconv.Itoa(i)){
                result += i
            }
        }
	} 
    fmt.Println(result)
}

func check_invalid(s string) bool {
    mid := len(s) / 2
    for i:=1; i<= mid; i++ {
        repeat_n := len(s) / i
        if strings. Repeat(s[:i], repeat_n) == s{
            fmt.Println("FOUND", s)
            return true 
        }
    }
    return false
}
