# some example math functions as lambda functions
add_fn = lambda x, y: x + y
subtract_fn = lambda x, y: x - y
square_fn = lambda x: x * x
cube_fn = lambda x: x * x * x


numbers = [1, 2, 66, -56, 33, -47, 3, 4, 5]
positive_numbers = filter(lambda x: x > 0, numbers)
print(list(positive_numbers))
even_numbers = filter(lambda x: x % 2 == 0, numbers)
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
print(list(even_numbers))
print(list(odd_numbers))

