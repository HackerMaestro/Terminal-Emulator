#!/bin/python3

# Importing the modules necessary to make our terminal emulator
import os, socket

# Creating a socket for network based commands
masterSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Defining functions
def makeDir(location):
    os.mkdir(location)

def pathExist(path):
    print(os.path.exists(path))

def changeDir(path):
    os.chdir(path)

def removeDir(path):
    os.rmdir(path)

def portscan(port, server):
    try:
        masterSocket.connect((server, port))
        return True
    except:
        return False

def ipAddress(website):
  try:
    print(socket.gethostbyname(website))
  except:
    print("The webaddress which you entered was invalid.")

# Creating a while loop so that the terminal keeps on running untill the user types in "exit"
running = True # Boolean variable

while running: # Event loop (a while loop)
    user_input = input(os.getcwd() + ">")
    if user_input == "exit":
        running = False
        exit()
    elif user_input == "mkdir":
        print("Please enter in the path which you would like your directory to be in.")
        locations = input(">>>$")
        if os.path.exists(locations) == True:
            print("That path does exist.")
            os.chdir(locations)
            print("Please enter in the name of your directory.")
            path = input(">>>$")
            makeDir(path)
        else:
            print("That path doesn't exist.")
    elif user_input == "pathExist":
        print("Please enter in the path of which you want to know whether it exists or not.")
        path = input(">>>$")
        if os.path.exists == True:
            print("This path does exist.")
        else:
            print("This path does not exist.")
    elif user_input == "pwd":
        print(os.getcwd())
    elif user_input == "cd":
        print("Please type in the path of the directory which you would like to move to.")
        newDirectory = input(">>>$")
        if os.path.exists(newDirectory) == True:
            changeDir(newDirectory)
        else:
            print("That directory doesn't exist.")
    elif user_input == "rm":
        print("Please enter the path of the directory (including the name of the directory).")
        Dir = input(">>>$")
        if os.path.exists(Dir) == True:
            removeDir(Dir)
        else:
            print("That directory doesn't exist.")
    elif user_input == "portscan":
        num1 = input("What is the starting port for the scanning (inclusive of this port). Please the port number in figures.\n>>>$")
        num2 = input("Up till which port would you like to scan (inclusive of this port). Please enter the port number in figures.\n>>>$")
        IPAddress = input("Please enter in the IP address of the targetted host.\n>>>$")
        for x in range(int(num1), (int(num2) + 1)):
            print(portscan(x, IPAddress))
    elif user_input == "getIPaddress":
        print("Please enter in the webaddress which you would like to find the IP address of.")
        webpage = input(">>>$")
        ipAddress(webpage)
    else:
        print("That command does not exist.")
