# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:18:42 2026

@author: shray
"""
def addition(x,y):
    s=x+y
    return s
def substraction(x,y):
    s=x-y
    return s
def multiply(x,y):
    s=x*y
    return s
def division(x,y):
    s=x/y
    return s
print("Choices")
print("Choice 1: Addition of 2 numbers\nChoice 2: Substraction\nChoice 3: Multiplication\nChoice 4: Division\n")
ch=int(input("Enter your choice:"))
if ch==1:
    x=int(input("Enter one number:"))
    y=int(input("Enter another number:"))
    a=addition(x,y)
    print("Addition of 2 number is:",a)
elif ch==2:
    x=int(input("Enter one number:"))
    y=int(input("Enter another number:"))
    a=substraction(x,y)
    print("Substraction of 2 number is:",a)
elif ch==3:
    x=int(input("Enter one number:"))
    y=int(input("Enter another number:"))
    a=multiply(x,y)
    print("Multiplication of 2 number is:",a)
elif ch==4:
    x=int(input("Enter one number:"))
    y=int(input("Enter another number:"))
    a=division(x,y)
    print("Division of 2 number is:",a)
else:
    print("Invalid choice")
    
    