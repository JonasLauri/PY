#! /usr/bin/env python3
# 5 Basic calculator
import math
from math import sqrt


def add(x, y):
    # This adds 2 numbers
    return x + y


def subtract(x, y):
    # This subtracts 2 numbers
    return x - y


def multiple(x, y):
    # This multiples 2 numbers
    return x * y


def divide(x, y):
    # This divides 2 numbers
    return x / y


def calculator():
    # Operations
    print("Select operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiple")
    print("4. Divide")
    print("5. Square root")

    # Take choise
    choise = input("Enter your choise (1/2/3/4/5): ")
    if int(choise) <= 4:
        num1 = float(input("Your first number: "))
        num2 = float(input("Your second number: "))
    elif int(choise) == 5:
        num1 = float(input("Your number: "))
    else:
        print("Negative option, please enter right option")
        return calculator()

    # Conditions
    if choise == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choise == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choise == '3':
        print(num1, "*", num2, "=", multiple(num1, num2))
    elif choise == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choise == '5':
        print("Square root of,", num1, "=", sqrt(num1))


if __name__ == "__main__":
    calculator()



