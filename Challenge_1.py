#Complete the tasks in any order and in any language. You may use helper functions
#if desired.

#1: Write a function that will reverse the given input string.
#For Example: function("string") -> "gnirts"


def reverse(string_1):
     new_list = []
     list_1 = list(string_1)
     length = len(list_1)
     
     for _ in range(length):
        last = len(list_1) - 1
        new_list.append(list_1[last])
        list_1.pop()
     return new_list


print(reverse("tacocat tacocat"))