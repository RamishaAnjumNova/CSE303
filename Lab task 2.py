# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

@author: Ramisha Anjum Nova

"""

#%%

# Problem - 01
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

nums = [i for i in range (1,1001) if i % 8 == 0]

print (nums)

#%%

# Problem - 02
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

nums = [i for i in range (1, 1001) if "6" in str (i)]
    
print (nums)

#%%

# Problem - 03
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

string = "Practice Problems to Drill List Comprehension in Your Head."

count = len ([i for i in string if i == " "])

print ("The Number of Space is: ", count)

#%%

# Problem - 04
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

string = "Practice Problems to Drill List Comprehension in Your Head."

newstring = "".join ([i for i in string if i not in ["a","e","i","o","u"]])

print (newstring)

#%%

# Problem - 05
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

string = "Practice Problems to Drill List Comprehension in Your Head."

words = string.split (" ")

count = [i for i in words if len (i) < 5]

print(count)

#%%

# Problem - 06
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

string = "Practice Problems to Drill List Comprehension in Your Head."

words = string.split (" ")

count = {i: len (i) for i in words}

print (count)

#%%

# Problem - 07
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

nums = [i for i in range (1,1001) if True in [True for divisor in range (2,10) if i % divisor == 0]]

print (nums)

#%%

# Problem - 08
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

nums = [i for i in range (1,1001)]

digit = {i: max ([divisor for divisor in range (1,10) if i % divisor == 0]) for i in nums}

print (digit)
