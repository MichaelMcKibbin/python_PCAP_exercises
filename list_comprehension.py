list_1 = []

for exp in range(6):
    list_1.append(10 ** exp)

# list comprehension version of the above for loop
list_2 = [10 ** exp for exp in range(6)]


print(list_1)
print(list_2)

#===============================

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

# list comprehension version of the above for loop
the_list_2 = [1 if x % 2 == 0 else 0 for x in range(10)]
print(the_list_2)

#==============================

#  The brackets make a comprehension, the parentheses make a generator

the_list3 = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator3 = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list3:
    print(v, end=" ")
print()

for v in the_generator3:
    print(v, end=" ")
print()

#==============================

