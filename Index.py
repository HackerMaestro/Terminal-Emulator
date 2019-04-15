import os, socket

"""Creating a socket for network based commands"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""Defining functions"""
def ipAddress(website):
  try:
    print(socket.gethostbyname(website))
  except:
    print("The webaddress which you entered was invalid.")
    
def pwd():
  print(os.getcwd())
  
def cd(path):
  os.chdir(path)
    
"""Programming the event loop"""
running = True

while running:
  user_input = input(">>>$")
  if user_input == "getIPAddress":
    webaddress = input(">>>$")
    ipAddress(webaddress)
  elif user_input == "pwd":
    pwd()
  elif user_input == "cd":
    path = input(">>>$")
    pathExists = os.path.exists(path)
    if pathExists:
      cd(path)
    else:
      print("That path doesn't exist")
  elif user_input == "exit":
    running = False
  else:
    print("The command which you entered was invalid.")
