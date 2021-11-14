# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:28:01 2021

@author: v-pusalu
"""

class ShippingContainer:
    
    #Class attribute
    next_serial=1337
    
   # @staticmethod
   # def _generate_serial():
    #    result=ShippingContainer.next_serial
     #   ShippingContainer.next_serial += 1
      #  return result
    
    @classmethod
    def _generate_serial(cls):  #cls is a class attribute
        result=cls.next_serial
        cls.next_serial += 1
        return result
    
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])  
    
    @classmethod
    def create_empty_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))  
    
    def __init__(self, owner_code, contents):
        self.owner_code=owner_code
        self.contents=contents
        
        #following will give an unbound error as next_serial variable is not knwon
        #to this instance
        #self.serial=next_serial
        
       # self.serial=ShippingContainer.next_serial
       # ShippingContainer.next_serial += 1
       
       #by using static method
        self.serial=ShippingContainer._generate_serial()