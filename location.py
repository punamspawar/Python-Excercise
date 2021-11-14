# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 16:15:59 2021

@author: v-pusalu
"""
from utility import typename

def auto_repr(cls):
    print(f"Decorating {cls.__name__} with auto_repr")
    members=vars(cls)
    for name, member in members.items():
        print(name,member)
        
    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")
        
    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not overrides __init__")
        
    sig=inspect.signature(cls.__init__)
    parameter_names=list(sig.parameters)
    
    if not all(
        isinstance(members.get(name, None), property)
        for name in parameter_names
     ):
        raise TypeError(
            f"cannot apply auto_repr to {cls.__name__} because not all"
            "__init__ parameters have matching properties"
            )        
    
    def synthesized_repr(self):
        return "{typename}({args})".format(
            typename=typename(self),
            args=", ".join(
                "{name=value!r}".format(
                    name=name
                    value=getattr(self, name)
                    )for name in parameter_names 
                )
            )
    
    setattr(cls, "__repr__", synthesized_repr)
    return cls



@auto_repr
class Location:
    
    def __init__(self,name, position):
        self._name=name
        self._position=position
        
    @property
    def name(self):
        return self._name
    
    @property()
    def position(self):
        return self._position
    
    def __repr__(self):
        return f"{typename(self)}(name={self.name},position={self.position})"
    
    def __str__(self):
        return self.name
    
hong_kong=Location("Hong Kong", EarthPosition(22.29,114.16))
