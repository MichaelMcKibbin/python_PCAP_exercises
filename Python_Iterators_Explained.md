# Python iterators explained

The key point is that **`__iter__()` doesn’t calculate the next value,   
and `__next__()` doesn’t call `__iter__()`.  
** Python’s `for` loop calls them separately.

## The `generator_fibonacci_example.py` example file works like this:

```python
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
```

## What `__iter__` does

`__iter__()` contains only two lines:

```python
def __iter__(self):
    print("__iter__")
    return self
```

The important line is **`return self`**.  
It tells Python: “Use this same `Fib` object as the iterator.  
It has a `__next__()` method that supplies values.”

## What the `for` loop does

The loop:

```python
for i in Fib(10):
    print(i)
```

works roughly like this:

```python
fib = Fib(10)          # Calls __init__(10)
iterator = iter(fib)   # Calls fib.__iter__(), which returns fib itself

while True:
    try:
        i = next(iterator)  # Calls fib.__next__()
    except StopIteration:
        break

    print(i)
```

Here, `fib` and `iterator` refer to **the same object**, because `__iter__()` returned `self`.

The names are connected like this:

| Python operation | Method Python calls | Purpose |
|---|---|---|
| `Fib(10)` | `__init__(self, 10)` | Sets up the object’s state |
| `iter(fib)` | `__iter__(self)` | Returns the iterator object |
| `next(iterator)` | `__next__(self)` | Returns one value or raises `StopIteration` |

## Where the values come from

The object remembers its progress through these instance variables:

```python
self.__n = nn                 # How many values to produce: 10
self.__i = 0                  # How many have been requested
self.__p1 = self.__p2 = 1     # The previous two Fibonacci values
```

Every call to `__next__()` increments the counter:

```python
self.__i += 1
```

It then follows these rules:

1. If the counter exceeds `10`, raise `StopIteration`.
2. For the first two calls, return `1`.
3. Otherwise, add the previous two values, update them, and return the result.

Here are the first few calls:

| Call to `next()` | `self.__i` | What happens | Returned value |
|---|---:|---|---:|
| First | 1 | First two values are handled specially | 1 |
| Second | 2 | First two values are handled specially | 1 |
| Third | 3 | Add `1 + 1`; previous values become `1, 2` | 2 |
| Fourth | 4 | Add `1 + 2`; previous values become `2, 3` | 3 |
| Fifth | 5 | Add `2 + 3`; previous values become `3, 5` | 5 |
| … | … | Continue using the stored values | … |
| Tenth | 10 | Add `21 + 34` | 55 |
| Eleventh | 11 | Raise `StopIteration`; the loop ends | — |

This line updates both previous values together:

```python
self.__p1, self.__p2 = self.__p2, ret
```

Python evaluates the right-hand side first, so `self.__p1` receives the **old** value of `self.__p2`, and `self.__p2` receives the newly calculated value.

## Why it keeps working after return

A `return` ends that particular method call, but **the object still exists and retains its instance variables**.

The next call starts `__next__()` from the top again, using the updated values stored in `self`.

The output therefore begins:

```
__init__
__iter__
__next__
1
__next__
1
__next__
2
__next__
3
```

The Fibonacci values produced are:

```
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
```

There is one final `__next__` printed after `55`, because Python must request another value to discover that the iterator has finished.

**`__iter__()` answers “Which object supplies the values?”;**  
**`__next__()` answers “What is the next value?”**
