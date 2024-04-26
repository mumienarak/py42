#!/usr/bin/python3
try:
  x = float(input("Give me a number: "))
  y = float(x)
except ValueError:
    print("This number is not a valid number.")
else:
    if x.is_integer():
       print("This number is an integer.")
    else:
       print("This number is a float.")