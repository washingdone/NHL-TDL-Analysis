package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("../2022NHLTDL.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close() // NTS: Defer pushes run until function ends

	scanner := bufio.NewScanner(file)
	var outputString string
	for scanner.Scan() {
		stringArr := strings.Split(scanner.Text(), ",")
		fmt.Println(stringArr)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
