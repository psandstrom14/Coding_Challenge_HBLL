#2: Write a function that accepts three integers as input and returns as output the
#largest of the three.
#For Example: function(1, 3, 2) -> 3


def find_max(num_1, num_2, num_3):
    list = [num_1, num_2, num_3]
    largest = max(list)
    return largest

print(find_max(1,3,2))