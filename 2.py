# Question 2: Calculate sum of all numbers from 1 to a given number.
# *Hint* :- Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number.
# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10).

#code:- 

num = int(input("enter a number : "))
Sum = 0
for i in range(1, num+1):
    Sum += i

print("Total Sum = ",Sum)
