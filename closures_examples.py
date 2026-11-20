def outer_fn():
    def display_favorite_programming_language():
        favorite_language = 'Python'
        print('The outer function has access to the inner function and can call it.')
        print('My favorite programming language is:', favorite_language)

    print("Executing the outer function...")
    return display_favorite_programming_language


my_closure = outer_fn()
my_closure()

print("================================")

def get_favorite_programming_language():
    favorite_language = '*Python*'
    def display_favorite_programming_language():

        print('The outer function has access to the inner function and can call it.')
        print(f'My favorite programming language is: {favorite_language}')

    print("Executing the outer function...")
    return display_favorite_programming_language

display_fn2=get_favorite_programming_language()
display_fn2()

print("================================")

def get_fav_programming_language(favorite_language):

    def display_favorite_programming_language():
        print(f'My favorite programming language is: {favorite_language}')

    print("Executing the outer function...")

    return display_favorite_programming_language

display_fn_java = get_fav_programming_language("Java")
display_fn_java()


display_fn_c_sharp = get_fav_programming_language("C#")
display_fn_c_sharp()


print("================================")
# # deleting the outer function reference to demonstrate that the inner function still works
# del get_fav_programming_language
# display_fn_java()
# display_fn_c_sharp()

print("================================")

def add_employee_to_department(department_name): # outer function

    employee_list = []
    def add_employee(employee_name): # inner function (closure)
        employee_list.append(employee_name)
        print(f'Employee {employee_name} has been added to the {department_name} department.')
        print(f'Current employees in {department_name}: {employee_list}')
    return add_employee


add_to_engineering = add_employee_to_department("Engineering")
print("Adding employees to the Engineering department...")
add_to_engineering("Alice")
add_to_engineering("Bob")

print("================================")

def formal_greeting():
    greeting = "Good morning. How are you?"
    def informal_greeting():
        greeting= "Hey! What's up?"
        print("Greeting in the inner function: ", greeting)

    informal_greeting()
    print("Greeting in the outer function: ", greeting)

formal_greeting()

print("================================")

def formal_greeting2():
    greeting = "Good morning. How are you?"
    def informal_greeting():
        nonlocal greeting
        greeting= "Hey! What's up?" # modifies the greeting variable in the outer function's scope
        print("Greeting in the inner function: ", greeting)

    informal_greeting()
    print("Greeting in the outer function: ", greeting)

formal_greeting2()



print("================================")



print("================================")



print("================================")
