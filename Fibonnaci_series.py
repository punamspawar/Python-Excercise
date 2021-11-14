# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 20:24:07 2021

@author: v-pusalu
"""

terms=int(input("How many numbers you want in Fibonnaci series:"))
n1,n2=0,1
if terms<=0:
    print("Please enter positive number")
elif terms==1:
    print("Fibonnaci series: {}".format(terms))
else:
    while terms!=0:
        print(n1)
        nth=n1+n2
        #print(nth)
        n1=n2
        n2=nth
        terms-=1