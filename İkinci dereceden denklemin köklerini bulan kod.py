#!/usr/bin/python3
# _*_ coding: utf-8 _*_

a=int(input("x karenin katsayısını girin:"))
b=int(input("x'in katsayısını girin:"))
c=int(input("sabit terimi girin:"))
delta=(b**2)-(4*a*c)
if delta>0:
    x1=(-b+delta**0.5)/2*a
    x2=(-b-delta**0.5)/2*a
    print("iki reel kök var",x1,x2)
elif delta==0:
    x1=-b/2*a
    x2=-b/2*a
    print("iki aynı kök vardır",x1,x2)
else:
    print("reel kök yoktur"
