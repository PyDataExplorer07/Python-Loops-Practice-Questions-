# Question 4: Display numbers from a list using a loop.
# *Hint* :- Write a Python program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

# here is List,

# numbers = [12, 75, 150, 180, 145, 525, 50]


# code :-

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    elif num % 5 == 0:
        print(num)

