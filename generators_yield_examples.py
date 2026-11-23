# In Python, the yield statement is used in a function to make it a generator.
# A generator is a special type of iterator that allows you to iterate over a sequence of values without storing them all in memory at once.
# When a generator function is called, it returns a generator object, which can be used to iterate over the values produced by the function.

def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)




def myGenerator():
    print("First item")
    yield 10

    print("Second item")
    yield 20

    print("Third item")
    yield 30

gen = myGenerator()
print(next(gen))
print(next(gen))
print(next(gen))



def generate_sequence(n):
    for i in range(n):
        yield i

print(list(generate_sequence(10)))


def generate_cubes(n):
    for i in range(n):
        yield i ** 3

print(list(generate_cubes(10)))

gen_tuple_cubes = generate_cubes(10)
cubes_tuple = tuple(gen_tuple_cubes)
print(cubes_tuple)

print("===")

for item in generate_cubes(10):
    print(item)


def generate_powers_of_two(limit):
    num = 1
    while num <= limit:
        yield 2**num
        num += 1

print(list(generate_powers_of_two(10)))

print("===")

# risks of an infinite generator
def infinite_generator():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_generator():
    if i > 10:
        break # prevent infinite loop
    print(i)


def arithmetic_progression(start, step, limit):
    count=1
    while count <= limit:
        yield start
        start += step
        count += 1


print(list(arithmetic_progression(1, 2, 10)))


def message_receiver():
    while True:
        message = yield
        print(f"Received message: {message}")

receiver = message_receiver()
next(receiver)

receiver.send(None)
receiver.send("Hello")
receiver.send("How are you?")


print("==============")

def my_generator2():

    yield 10
    yield 20
    yield 30

gen2 = my_generator2()
print(list(gen2))
print("==============")