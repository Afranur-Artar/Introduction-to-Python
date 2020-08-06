#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Assign the correct value to sum_result and subtract_result variables
number_1 = 22
number_2 = 15

# Addition
sum_result = number_1+number_2 #change this line
print("Sum of 15 and 22       : ", sum_result)
print("Sum of {} and {}       :  {}". format(number_1,number_2,sum_result))

# Subtraction
subtract_result = number_1-number_2 #change this line
print("Subtraction 15 from 22 : ", subtract_result)


# In[4]:


# Multiplication
Multiplication = 15*22 #change this line 
print("Multiplication of 15 and 22 : ", Multiplication)

# Square
square = 9**2 #change this line 
print("Square of 9                 : ", square)

# Exponent

exp =  4**3 #change this line  
print("4 to the power 3            : ", exp)


# Mod işlemi için yani bölümden kalanı bulmak için % işareti kullanılır.

# In[5]:


word1="orange"
word2="apple"
print(word1,"&",word2)


# # Soru1:
# 
# Suppose you invested in Bitcoin at the end of 2017 when Bitcoin gained a lot of value. What would be your money at the end of a week if you had invested $1000 with an average daily increase of 12\% ? You can solve the problem using Python.
# 
#  ##### Help
# 
#  #Create a variable capital ($1000)
# 
#  #Create a variable for daily growth (12%)
# 
#  #Create a variable for period (7)
# 
#  #Calculate the final growth rate
# 
#  #Calculate result
# 
#  #Print result

# In[20]:


#Cevap 1:

capital=1000
daily_growth=0.12
period=7
final_growth=period*daily_growth
result=capital*final_growth
print("Your money is {} in Bitcoin at the end of 2017".format(result))


# In[ ]:





# # Soru 2:
# 
# Print the text in quotes with Python. However, you must get the numbers from variables using .format() notation.
# Because the text is long, you might consider writing in two lines:
# 
#  `"When we buy bitcoin with 1000 USD at the beginning of the week, we would earn 1210.68 USD at the end of the week, with an average gain of 12\%."`

# In[7]:


#Cevap 2:

word1=1000
word2=1210.68
word3=12

print("When we buy bitcoin with {} USD at the beginning of the week, we would earn {} USD at the end of the week, with an average gain of {}%".format(word1,word2,word3))


# 

# # Soru 3:
# 
# Get the temperature in Fahrenheit from user and write a code to convert it to Celcius. For conversion, you can use this formula: C = (5/9) * (F - 32)
# 
#  Enter the temperature in Fahrenheit: 
#  user --> 26
#  output --> Temperature (C) : -3.33

# In[14]:


#Cevap 3:

temperature=int(input("Temperature="))
convert=(5/9)*(temperature-32)

print("Temperature (C): {:0.2f}".format(convert))


# 

# # Soru 4:
# 
# Get a three digit number the from user and calculate the sum of the digits in the integer.
# 
#  user --> 365
#  output --> "The sum of digits in the number is 14

# In[13]:


# Cevap 4:

digit1=int(input("Digit1="))
digit2=int(input("Digit2="))
digit3=int(input("Digit3="))

sum=digit1+digit2+digit3
print("The sum of digits in the number is {}".format(sum))


# In[ ]:





# # Soru 5:
# 
# Write some code to calculate the hypotenuse of a right angled triangle. Get the side lengths from the user.
# 
#  user --> first side lenth : 6
#  user --> first side lenth : 8
#  output --> "The length of the hypotenuse is 10

# In[18]:


# Cevap 5:

side1=int(input("First side length:"))
side2=int(input("First side length:"))

hypotenuse=((side1**2)+(side2**2))**0.5
print("The length of the hypotenuse is {}".format(hypotenuse))

