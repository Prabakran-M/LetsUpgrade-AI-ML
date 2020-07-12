#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Research on whether addition, subtraction, multiplication, division, floor division and modulo operations be performed on complex numbers. Based on your study, implement a Python program to demonstrate these operations.

a = 3 + 2j
b = 5 + 7j

print ( "Addition : ",a+b)
print ( "Subtraction : ",a-b)
print ( "Multiplication : ",a*b)
print ( "Division : ",a/b)

#Floor divison and modulo cannot be performed on complex numbers.
#print ( "Floor divison : ",a//b)
#print ( "Modulo : ",a%b)


# In[15]:


#Research on range() functions and its parameters. Create a markdown cell and write in your own words (no copy-paste from google please) what you understand about it. Implement a small program of your choice on the same.

# * The range starts at 0
# * It ends at -1
# * The range operator helps us to enter a list of variables to the desired numbers by just adding a range operator in front of the code.

a = range(10)
for x in a:
    print(x)


# In[19]:


#Consider two numbers. Perform their subtraction and if the result of subtraction is greater than 25, print their multiplication result else print their division result.
a = 100
b = 70
c = a-b
if c >= 25:
    print(" ",a*b)
else:
    print(" ",a/b)


# In[6]:


#Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the result as "square of that number minus 2".

a = range(10) #[10, 75, 50, 61, 33, 80, 9, 8, 69, 59] 

for i in a : 
    if i % 2 == 0 :
     print((i**2)-2)


# In[15]:


#Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that number is divided 2.
a = range(100,111) 

k = 7
  
for i in a : 
    print(i)
    d = i / 2
    if d >= k : 
        print("   ",int(d))

