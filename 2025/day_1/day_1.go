package main

import "fmt"
import "os"
import "bufio"
import "strconv"

func abs(x int) int{ 
  if x < 0 {
    return -x
  }
  return x
}

func main(){
  file, err := os.Open("input.txt");
  if err != nil {
    panic(err);
  }

  scanner := bufio.NewScanner(file)
  var dial int = 50
  var cntr int = 0
  for scanner.Scan() {
    line := scanner.Text()
    dir := string(line[0])
    num, err := strconv.Atoi(line[1:])
    if err != nil {
      panic(err)
    }
    fmt.Println(line)
    var passes int = 0 
    if dir == "L" {
      if dial != 0 {
        passes, dial = ((100 - dial)+num)/100, (dial - num) % 100
      } else {
        passes, dial = (dial+num)/100, (dial - num) % 100
      }

    } else {
      passes, dial = abs((dial+num)/100), (dial + num) % 100
    }
    if dial < 0 {dial = 100 + dial}

    //6764 too low
    // 6785 incorrect

    fmt.Printf("Passes:%v, dial position %v\n", passes, dial)
    
    cntr += passes
  }
  fmt.Println(cntr)
}
