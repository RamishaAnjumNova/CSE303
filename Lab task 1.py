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

x = int(input("Enter x: "))
y = int(input("Enter y: "))

product = x * y
sum = x + y

if (product > 1000):
    print ("\nSum of %d and %d is %d" % (x, y, sum))
else:
    print ("\nProduct of %d and %d is %d" % (x, y, product))
    
#%%
# Problem - 02
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

r = float(input("Enter Radius : "))

area = 3.1416 * r * r
perimeter = 2 * 3.1416 * r

print ("\nArea of the Circle is: ", area)
print ("\nPerimeter of the Circle is: ", perimeter)

#%%
# Problem - 03
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

def compound_interest_2018_3_60_006 (P, R, T):
    A = P * (1 + R / 100) ** T
    return A
    
p = float(input("Enter Principle Amount: "))
r = float(input("Enter Interest Rate: "))
t = float(input("Enter Time (in years): "))

a = compound_interest_2018_3_60_006 (p, r, t)

print ("\nThe Compound Interest is: ", a)

#%%
# Problem - 04
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

n = int(input("Enter A Positive Integer N: "))

sum = (n * (n + 1) * (2 * n + 1 )) / 6

print ("\nSum of The Series: ", sum)

#%%
# Problem - 05
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

def prime_find_2018_3_60_006 (n):
    if n > 1:
        for i in range(1, int(n / 2) + 1):
            if (n % i) == 0:
                return ("is not Prime.")
                break
            else:
                return ("is Prime.")
 
    else:
        return ("is not Prime.")

n = int(input("Enter Positive Integer N: "))

res = prime_find_2018_3_60_006 (n)

print ("\n%d " %n, res)

#%%
# Problem - 06
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

def fibonacci (n):
    if n <= 0:
        print ("\nInvalid!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)

n = int(input("Integer N Must Be Greater Than 0.\n\nEnter Integer N: "))

f = fibonacci (n)

if n <= 0:
    print ("\nInteger N Must Be Greater Than 0!")
elif n == 1:
    print ("\nThe 1st Fibonacci Number is: ", f)
elif n == 2:
    print  ("\nThe 2nd Fibonacci Number is: ", f)
elif n == 3:
    print  ("\nThe 3rd Fibonacci Number is: ", f)
else:
    print ("\nThe %dth Fibonacci Number is: " %n, f)

#%%
# Problem - 07
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

def sum_of_list (numbers):
      
  sum = 0
 
  for n in numbers:
     sum = sum + n
  return sum
    
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
print("\nSum of the List is: ", sum_of_list (list))

#%%
# Problem - 08
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = odd = 0

for n in range (len(list)) :
    if n % 2 == 0 :
        even += list [n]
        
print("\nSum of the Even-indexed Elements of the List is: ", even)

#%%
# Problem - 09
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

def largest_number_2018_3_60_006 (list):
  
    largest_number = list [0]
    
    for n in list:
        if n > largest_number :
             largest_number = n
    return largest_number

def smallest_number_2018_3_60_006 (list):
  
    smallest_number = list [0]
    
    for n in list:
        if n < smallest_number :
             smallest_number = n
    return smallest_number  

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print ("\nLargest Element of the List is:", largest_number_2018_3_60_006 (list))
print ("\nSmallest Element of the List is:", smallest_number_2018_3_60_006 (list))

#%%
# Problem - 10
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list.sort()
 
print("\nSecond Largest Element of the List is:", list [-2])

#%%
# Problem - 11
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

def even_index_char (str):
  for i in range (0, len(str)-1, 2):
    print("Index[",i,"]", str[i] )
    
input = input ("Enter a String: ")

print("Even-indexed Characters:")
even_index_char (input)
#%%
# Problem - 12
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

string = input("Enter a string: ")
print(string)
  
n = int(input("Enter a number: "))
  
print ("Initial String", string)
  
res = ''

for i in range(0, len(string)):
    if i >= n:
        res = res + string [i]
          
print ("Resultant String", res)

#%%
# Problem - 13
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

string = "CSE303 is a subject code. CSE303 is the code of python programming.(CSE303, CSE303, CSE303)"
substring = "CSE303"
count = 0
es = ''
count = 0

for i in range (len(string)):
    if string [i: i + len (substring)] == substring:
        count += 1

print("CSE303 appeared ", count, "times")

#%%
# Problem - 14
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

def palindrome_checker_2018_3_60_006 (s):
    return s == s[::-1]
 
s = "madam"

res = palindrome_checker_2018_3_60_006 (s)
 
if res:
    print("\nPalindrome")
else:
    print("\nNot Palindrome")

#%%
# Problem - 15
# Student ID: 2018-3-60-006
# Student Name: Ramisha Anjum Nova

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = [n for n in list1 if n%2] + [n for n in list2 if not n%2]

print (list3)

#%%