#!/bin/python3

# Importing the modules necessary to make our terminal emulator
import os, socket, time

# Creating a socket for network based commands
masterSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Defining functions
def pwd():
  print(os.getcwd())
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

print("\t\t\t\t\t\t\t\t\t\tadiOS")

directories = []

while running: # Event loop (a while loop)
    user_input = input(os.getcwd() + ">")
    user2 = user_input.split()
    if len(user2) == 1:
        if user2[0] == "exit":
            print("adiOS")
            for i in range(5):
                print(5- i)
                time.sleep(1)
            exit()
        elif user2[0] == "pwd":
            pwd()
        elif user2[0] == "ls":
            print(directories)
    if len(user2) == 2:
        if user2[0] == "cd":
            if os.path.exists(user2[1]) == True:
                changeDir(user2[1])
        elif user2[0] == "mkdir":
            makeDir(user2[1])
            directories.append(user2[1])
        elif user2[0] == "pathExists":
            pathExist(user2[1])
        elif user2[0] == "getIPaddress":
            try:
                ipAddress(user2[1])
            except:
                print("The webaddress which you entered was wrong.")
        elif user2[0] == "rm":
            if os.path.exists(user2[1]) == True:
                removeDir(user2[1])
                directories.remove(user2[1])
            else:
                print("That path doesn't exist")
    elif len(user2) == 3:
        if user2[0] == "mkdir":
            if os.path.exists(user2[1]) == True:
                makeDir(user2[2])
                directories.append(user2[2])
            else:
                print("That path doesn't exist")
    elif len(user2) == 4:
        if user2[0] == "portscan":
            port1 = int(user2[1])
            port2 = int(user2[1])
            try:
                for port in range(port1, port2 + 1):
                    if portscan(port, user2[3]) == True:
                        print("%d: Open" % port)
                    else:
                        print("%d: Closed" % port)
            except:
                print("We could not connect to that webaddress.")
            
    else:
        print("That command doesn't exists")
