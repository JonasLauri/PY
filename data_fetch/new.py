# For learning purposes, some code
#! /usr/bin/env python
from words import *

def data():
    print("Enter your name")
    name = input()
    if name == 'Jonas':
        print("Hello, Jonas!, how is your day?")
    else:
        print("What isn't you")
    day = input()
    if day == "good":
        print("whats great! Good day!")
    print("do you want fetch some data?")
    answer = input()
    if answer == "yes":
        print("Your address : ")
        main()
        

data()



    
    
