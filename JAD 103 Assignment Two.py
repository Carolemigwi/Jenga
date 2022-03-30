#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write and test a python class Length with attributes feet and inches. Include the init method and appropriate getters and setters. Include a method __str__ to output the length object in the format : feet’ inches” e  5’ 11”
    class length:#class attribute
    feet= int(input("Feet': "))
    inches= int(input("Inches": "))
    def __init__(self,feet,inches):
            self.feet=feet
            self.inches=inches
    def print_length(self):                 
        print(str(self.feet)+str(self.inches))


# In[ ]:


#Update the Length class above to include operator methods to add and subtract two length objects. For instance 5’11”+2’4”= 8’3”


# In[ ]:





# In[ ]:




