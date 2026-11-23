any_list = [1, 2, 3, 4]
even_list = list(map(lambda n: n | 1, any_list))
# The map() function applies the lambda function to each element of any_list.
# The lambda function takes an integer n and performs a bitwise OR operation with 1 (n | 1).
# This operation sets the least significant (rightmost) binary bit of n to 1,
# effectively converting any even number to the next odd number while leaving odd numbers unchanged.
# The result is a new list, even_list, which contains the modified values.
# n | 1 produces the next odd number for even numbers and keeps odd numbers the same.
# For example, 2 | 1 results in 3, and 3 | 1 results in 3.
# The final even_list will be [1, 3, 3, 5].
print(even_list)