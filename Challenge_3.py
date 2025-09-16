#3: Write a function that calculates the factorial of an input integer using recursion.
#Factorial: n! = n * (n-1) * (n-2) * ... * 1, so 3! = 3 * 2 * 1 = 6
#For Example: function(3) = 6

#I am not sure what recursion is but I am going to try to solve it two ways and hope one of them is what was intended.

"""
def fact_1(num):
    num_2 = num
    num_down = num -1 
    for _ in range(num-1):
        num_2 *= num_down
        num_down -= 1
    return num_2
    
print(fact_1(3))
"""

def factorial(num) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        num *= factorial(num - 1)
        return num

print(factorial(15))