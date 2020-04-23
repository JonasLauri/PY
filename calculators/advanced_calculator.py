# dictionary lookup and recursion calculator
from operator import add, sub, mul, truediv


operators = {"+": add,
             "-": sub,
             "*": mul,
             "/": truediv
             }


def calculate(a):
    if a.isdigit():
        return float(a)
    for b in operators.keys():
        left, operator, right = a.partition(b)
        if operator in operators:
            return operators[operator](calculate(left), calculate(right))


calc = input("Enter your calculation:\n")
print("Answer: " + str(calculate(calc)))
