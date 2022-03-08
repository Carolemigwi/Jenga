#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Extract the words miss from s
s= "Mississippi"
print(s[0:4])


# In[2]:


#Extract the word sip from s
s= "Mississippi"
print(s[6:9])


# In[4]:


#Print the length of s
len(s)


# In[13]:


#Extract  and repeat the  word ‘sis’ 3 times 
sis=(s[3:6])*3
print(sis)


# In[19]:


#Create a string ‘Kenya ‘ and use ‘Miss’ extracted in i) to create a new string , ‘Miss Kenya’
K="Kenya"
MK=(s[0:4])+(" ")+K
print(MK)


# In[55]:


#indexing
print(s[0:7])


# In[54]:


#reversing
s2=len(s) # calculate length of the list
s3=s[s2::-1] # slicing 
print (s3) # print the reversed string


# In[56]:


#slicing
print(s[5:])


# In[68]:


#appending
MK1=["Miss","Kenya"]
MK1.append(2022)
print(MK1)


# In[69]:


#removing
MK1.remove('Kenya')
print(MK1)


# In[72]:


#sorting
books = ['The War of Art', '5am Club', 'Big Magic']
books.sort()
print(books)


# In[74]:


#Write and test a function , by_three ,  to print the numbers divisible by 3 between 1 and a number n
def result(by_three):
     
    # iterate from 0 to N
    for num in range(by_three):
    
            if num % 3 == 0:
                print(str(num) + " ", end = "")
                 
            else:
                pass


# In[76]:


#test
by_three=100
result(by_three)


# In[ ]:


#Rewrite a lambda version of the function by_three


# In[79]:


#Write and test a  function to reverse the contents of a list

lst = [10, 11, 12, 13, 14, 15]

def Reverse(lst):
    return [ele for ele in reversed(lst)]
     
print(Reverse(lst))

