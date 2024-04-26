#!/usr/bin/python3
a = int(input("Enter a number less than 25 : "))
if a > 25 :
    print("Error")
else:
    for i in range (a,26):
        print("inside the loop, my valuable is", i)
        