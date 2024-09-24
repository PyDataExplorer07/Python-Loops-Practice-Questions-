# Question 15: Find the sum of the series up to n terms.
# *Hint* :- Write a program to calculate the sum of series up to n terms. For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

# code :-

n = 5
start = 4

sum_seq = 0

for i in range(0, n):
    print(start, end='+')

    sum_seq += start
    start = start * 10 + 4

print("\nSum Sequence is :", sum_seq)
