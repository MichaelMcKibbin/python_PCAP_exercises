# PEP 8, the Style Guide for Python Code, recommends that lambdas should not be assigned to variables, but rather they should be defined as functions.
# It is generally better to use a regular function definition (using def) instead of a lambda function when you want to assign it to a variable, as it improves code readability and maintainability.

# Recommended:
def f(x): return 3*x

# Not recommended:
f = lambda x: 3*x