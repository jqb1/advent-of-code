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

	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	scanner.Scan()

    result := 0
	for nums := range strings.SplitSeq(scanner.Text(), ",") {
		splitted := strings.Split(nums, "-")
		low_str := splitted[0]
		low, _ := strconv.Atoi(splitted[0])
		high, _ := strconv.Atoi(splitted[1])
		fmt.Println(low, high)

        new_num, _  := strconv.Atoi(low_str)
		for new_num <= high {
            if len(low_str) != 1 && len(low_str)%2 != 0 {
		    	new_num = powInt(10, len(low_str))
                low_str = strconv.Itoa(new_num)
                continue
	    	}
            l1 := low_str[:len(low_str)/2]
            new_num, _ = strconv.Atoi(l1+l1)
            if new_num <= high && new_num >= low {
                fmt.Println("FOUND", new_num)
                result += new_num
            }

            new_num, _ = strconv.Atoi(l1)
            new_num += 1
            l1 = strconv.Itoa(new_num)
            new_num, _ = strconv.Atoi(l1+l1)
            low_str = strconv.Itoa(new_num)
		}
	} 
    fmt.Println(result)
}
