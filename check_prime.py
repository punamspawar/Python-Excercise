# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 20:09:07 2021

@author: v-pusalu
"""

ip=int(input("Enter a number"))

if ip>1:
    for i in range(2,ip):
        if ip%i==0:
            print("{} is not prime".format(ip))
            break
    else:
        print("{} is prime".format(ip))