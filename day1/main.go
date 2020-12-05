package main

import (
	"io/ioutil"
	"fmt"
	"log"
)

func main() {
	bytes, err := ioutil.ReadFile("input.txt")
	if err != nil {
	log.Fatal(err)
	}

	for i, i  {
		fmt.Println(bytes[i])
	}

}