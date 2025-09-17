#3: Write a function that calculates the factorial of an input integer using recursion.
#Factorial: n! = n * (n-1) * (n-2) * ... * 1, so 3! = 3 * 2 * 1 = 6
#For Example: function(3) = 6

def factorial(num) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num < 0:
        return "Number must be positive"
    elif type(num) != int:
        return "Number must be a whole number"
    else:
        num *= factorial(num - 1)
        return num

print(factorial(5))