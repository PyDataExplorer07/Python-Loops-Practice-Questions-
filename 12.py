# Question 12: Reverse a integer number.
# code :-

number = int(input("enter a number : "))

reverse_num = 0

print("Given Number : ", number)

while number > 0:
    remainder = number % 10
    reverse_num = (reverse_num * 10) + remainder
    number = number // 10

print("Reverse_num : ", reverse_num)


