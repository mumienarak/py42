#!/usr/bin/python3
for w in range(11):
    a = []
    for i in range(11):
        a.append(str(w * i))
        a_ii = " ".join(a)
    print("Table de",w,':',a_ii,)