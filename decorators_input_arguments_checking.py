import math

def non_negative_arguments(decorated_func):
    def check_non_negative(*args):
        try:
            for arg in args:
                if arg < 0:
                    raise ValueError(f"Argument {arg} is negative. All arguments must be non-negative.")
        except ValueError as e:
            print(e)
            return None
        return decorated_func(*args)
    return check_non_negative

@non_negative_arguments
def compute_circle_area(radius):
    return math.pi * radius ** 2

@non_negative_arguments
def compute_circle_perimeter(radius):
    return 2 * math.pi * radius

print(compute_circle_area(5))  # Valid input
print(compute_circle_area(-5))  # Invalid input, will raise ValueError

print(compute_circle_perimeter(15))  # Valid input
# print(compute_circle_perimeter(-15))  # Invalid input, will raise ValueError


@non_negative_arguments
def compute_square_area(side_length):
    return side_length ** 2
print(compute_square_area(5))
print(compute_square_area(-5))


@non_negative_arguments
def compute_rectangle_area(length, width):
    return length * width
print(compute_rectangle_area(5, 10))
print(compute_rectangle_area(-5, 10))
