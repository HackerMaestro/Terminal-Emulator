import os, sys, tkinter

#Declaring variables
currentDirectory = os.getcwd()

#Defining functions
def makeDirectory(path, name):
    os.chdir(path)
    os.mkdir(name)

def getCurrentDirectory():
    print(currentDirectory)

def changeDirectory(path):
    os.chdir(path)

