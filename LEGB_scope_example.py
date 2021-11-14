# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:27:57 2021

@author: v-pusalu
"""

msg="global"

def enclosing():
    msg="enclosing"
    
    def local():
        #global msg #if we do not use it then value of msg in enclosing function is printed
        #it introduces names from enclosing namespace into local namespace
        nonlocal msg
        msg="local"
    
    print("enclosing= ", msg)
    local()
    print("enclosing= ", msg)

print("global= ",msg)
enclosing()
print("global= ", msg)