# Question 9: Print all prime numbers within a range.
# *Hint* :- 6 is not a prime number because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply to make it.

#Note:- A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

# code :-

start = int(input("enter starting number : "))
end = int(input("enter ending number : "))

print("Prime Numbers between",start,"and",end,"are : ")

for num in range(start, end+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
