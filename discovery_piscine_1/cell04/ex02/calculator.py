#!/usr/bin/python3
x = int(input("Give me the first number: "))
y = int(input("Give me the second number: "))

try:
  print(x,"+",y ," = ",x+y)
  print(x,"-",y ," = ",x-y)
  print(x,"*",y ," = ",x*y)
  print(x,"/",y ," = ",x/y)
except ZeroDivisionError: 
  print("Error: cannot divide by zero")
