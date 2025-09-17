#Complete the tasks in any order and in any language. You may use helper functions
#if desired.

#1: Write a function that will reverse the given input string.
#For Example: function("string") -> "gnirts"


def reverse(string_1):
     new_string = ""
     list_1 = list(string_1)
     length = len(string_1)
     
     for _ in range(length):
        new_string += list_1.pop()
        
     return new_string


print(reverse("SAD"))