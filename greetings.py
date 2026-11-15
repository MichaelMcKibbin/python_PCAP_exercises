'''
Provides random greetings

This text file can be used as a Python program, script, or, module
'''
import random
sayings=("Hello", "Hi", "Hey", "Greetings", "Salutations")

def greet():
    ''' Returns a random greeting from the sayings tuple '''
    return random.choice(sayings)

def test_greet():
    ''' Tests the greet function '''
    greeting = greet()
    assert greeting in sayings, f"greet() returned {greeting}, which is not in the sayings tuple"

def say_hello():
    ''' Prints a random greeting '''
    print(greet())

def random_greeting():
    ''' Returns a random greeting from the sayings tuple '''
    return random.choice(sayings)

def all_greetings():
    ''' Returns a list of all greetings in the sayings tuple '''
    return list(sayings)

def loop_greetings():
    ''' Returns a list of greetings from the sayings tuple '''
    print("all sayings: ")
    for loop in range(len(sayings)):
        print(sayings[loop % len(sayings)], end=' ')
    print('\ngreetings list complete')
    return all_greetings()

if __name__ == '__main__':
    print("__main__ : "+ random_greeting())
else:
    print("who am i?"+ random_greeting())

print("\n")
test_greet()
say_hello()
print("all greetings:", all_greetings())
print("loop greetings:", loop_greetings())
print("say hello:", say_hello())
print("random greeting:", random_greeting())
print("\n")
print("__name__:", __name__)
print("dir():", dir())