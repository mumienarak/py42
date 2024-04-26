#!/usr/bin/python3
arr = [2,8,9,48,8,22,-12,2]
arr1 = list(dict.fromkeys(arr))
#dict cannot have dupl
#convert list to dic then convert back to list
arr2 = []
for i in range(len(arr1)):
   if arr1[i] > 5:
    arr2.append(arr1[i]+2)
print(arr)
print(arr2)