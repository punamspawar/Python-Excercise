# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 06:42:20 2021

@author: v-pusalu
"""
#string reverse and palindrome
str="mom"
def reverse(str):
    s=""
    for i in str:
        s=i+s
    return s
st=reverse(str)
print(st)
if str==st:
    print("{} is palindrom".format(str))
else:
    print("{} is not palindrom".format(str))