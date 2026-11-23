# a basic generator that yields powers of 2 up to 2**(n-1)

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

#==========================

# Using a list comprehension to create a list of powers of 2

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = [x for x in powers_of_2(5)]
print(t)


#========================

# The list() function
#
# The list() function can transform a series of subsequent generator invocations into a real list

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = list(powers_of_2(3))
print(t)

#========================

# The in operator can be used to check if a value is in the generator's output

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for i in range(20):
    if i in powers_of_2(4):
        print(i)


#========================


