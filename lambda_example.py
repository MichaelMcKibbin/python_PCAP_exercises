from turtledemo import __main__

increment_fn = lambda x: x + 1

# show information about the lambda function
print('Type of __main__:', type(__main__))
print('Increment function:', increment_fn)
print('Increment function type:', type(increment_fn))
print('Increment function result:', increment_fn(5))

# # get user input
# user_input = input('Please enter a number: ')
# user_number = int(user_input)
# print('Incremented number:', increment_fn(user_number))


# some example math functions as lambda functions
add_fn = lambda x, y: x + y
subtract_fn = lambda x, y: x - y
square_fn = lambda x: x * x
cube_fn = lambda x: x * x * x


# creating a list of strings
create_list_fn = lambda some_string, times: [some_string for _ in range(times)]

create_list_fn('Hello', 5)
print(create_list_fn('Hello', 5))


lambda x,y: x % y
print('Modulus function:', (lambda x, y: x % y)(10, 3))


# student record creation using a lambda function
create_student_record_fn = \
    lambda name, age, subject, grade: {'name': name, 'age': age, 'subject': subject, 'grade': grade}
print(create_student_record_fn('Alice', 20, 'Math', 'A'))

# creating a list of student names using a lambda function
create_student_names_list_fn = \
    lambda *args: [name for name in args]

print(create_student_names_list_fn('Alice', 'Bob', 'Charlie'))

# creating a list of student records using a lambda function
create_student_records_list_fn = \
    lambda **kwargs: {key: value for key, value in kwargs.items()}
all_students=[]
all_students.append(create_student_record_fn(name='Alice', age=20, subject='Math', grade='A'))
all_students.append(create_student_record_fn(name='Bob', age=22, subject='Science', grade='B'))
all_students.append(create_student_record_fn(name='Charlie', age=21, subject='History', grade='C'))
print(all_students)

