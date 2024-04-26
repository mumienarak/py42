#!/usr/bin/python3
x = float(input("1st number: "))
y = float(input("2nd number: "))
z = x*y
print(x,"x",y,"=",z)
if z < 0 :
    print("negative")
elif z > 0 :
    print("positive")
else:
    print("zero")