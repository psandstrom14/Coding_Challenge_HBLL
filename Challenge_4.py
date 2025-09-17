#4: Write a function that calculates the Nth entry of the Fibonacci sequence (Do not
#include 0 in the sequence).
#Fibonacci Sequence: 1, 1, 2, 3, 5, 8, ...
#The sequence is calculated by summing two numbers and adding the sum to the sequence.
#1 (the sequence starts with 1)
#1 + 0 = 1 (1 was the only element, so add 0, then put the result on the end of the sequence
#1, 1
#1 + 1 = 2
#, 1, 2
#1 + 2 = 3
#1, 1, 2, 3
#2 + 3 = 5
#1, 1, 2, 3, 5 etc.
#So your function should behave as
#function(1) -> 1
#function(2) -> 1
#function(3) -> 2
#function(4) -> 3
#function(5) -> 5 etc.


def fib_num(num):
    term = 1
    seq = [1, 1]
    while term < num:
        addend_1 = seq[term - 1 ] 
        addend_2 = seq[term]
        new = addend_1 + addend_2
        seq.append(new)
        term += 1
    entry = seq[num - 1]
    return entry

print(fib_num(1))
print(fib_num(2))
print(fib_num(3))
print(fib_num(4))
print(fib_num(5))
print(fib_num(6))
print(fib_num(7))
print(fib_num(8))
print(fib_num(9))