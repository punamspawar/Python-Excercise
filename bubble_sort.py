# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 20:15:16 2021

@author: v-pusalu
"""

lst=[7,6,1,9,4]
sec_max=0
#lst=sorted(lst)
n=len(lst)
for i in range(n-1):
    for j in range(0,n-i-1):
        if lst[j]<lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
        
            
print(lst)
