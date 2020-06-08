# NSwebapp
Netsapians Webapp

Setup:
Download and install Go and Python 3
in the go path make 3 folders pkg, bin, and src
in CMD, Powershell, terminal, etc type this comand 
	go get github.com/josephstl/NSwebapp
	go get github.com/sqweek/dialog
	pip install pyinstaller
	pip install easygui

this will download all the necessary files in the src folder under src/github and install the python compiler

to compile:
for the main executible type in to the terminal:
	go build -ldflags -H=windowsgui webapp.go
for the launcher in the terminal type:
	pyinstaller –-onefile –-noconsole updater/Launcher.py
	