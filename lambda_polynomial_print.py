# Before lambda functions, we can define a function and pass it as an argument to another function.
# For example, we can define a polynomial function and pass it to a print_function that prints the values of the polynomial for a range of x values.

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)


#===============================

# Now we can use a lambda function to define the polynomial function directly in the print_function call, without having to define a separate function.

def print_function2(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function2([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

