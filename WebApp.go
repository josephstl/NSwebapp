package main

// imports

import (
	"bytes"
	d "dialog"
	f "fmt"
	"log"
	"os"
	"os/exec"
)

var (
	exPath       string
	chr32, chr64 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
	opnChrm      bool
)

func main() {
	// this checks for chrome in the 32bit and 64 bit program files folders
	if fileExists(chr32) {
		exPath = chr32
		opnChrm = true
	} else if fileExists(chr64) {
		exPath = chr64
		opnChrm = true
	} else {
		// this gives the error message for if chrome is not found
		d.Message("%s", "Chrome does not exist. Please download and install Chrome from www.google.com/chrome/ and try again").Title("Error").Error()
	}
	//this gets the current directory then add all the proper context to
	currDir, err := os.Getwd()
	if err != nil {
		log.Println(err)
	}
	localURL := "file:///" + currDir + "\\Wrapper.html"

	userflag := "--app=" + localURL

	if opnChrm {
		// creates a object that calls an executible
		syscall := exec.Command(exPath, userflag)
		// runs and error checks the executible
		var stderr bytes.Buffer
		syscall.Stderr = &stderr
		err := syscall.Start()
		if err != nil {
			f.Println(stderr.String())
			log.Fatal(err)
		}

		// this creates a dialog box when you close the webapp window that asks you if you would like to reopen the window
	}

}

//this checks if a file exists this is usefull for finding the chrome exicutible
func fileExists(filename string) bool {
	info, err := os.Stat(filename)
	if os.IsNotExist(err) {
		return false
	}
	return !info.IsDir()
}
