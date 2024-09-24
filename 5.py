# Question 5: Count the total number of digits in a number.
# code :-

Number = int(input("enter a number : "))

cout = 0

while Number != 0:
    Number = Number // 10
    cout += 1

print("Total digits are = ",cout)

