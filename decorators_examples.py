def emphasise(display_message_func):
    def wrapper():
        print("*************************!***************************")
        display_message_func()
        print("*************************!***************************")
    return wrapper


@emphasise
def display_important_message():
    print("This is an important message.")
display_important_message()

@emphasise
def display_boring_message():
    print("This is a boring message.")
display_boring_message()

@emphasise
def display_entertaining_message():
    print("This is an entertaining message.")
display_entertaining_message()



def emphasise_message(display_message_func):
        print("***********************000*****************************")
        display_message_func()
        print("***********************000*****************************")

emphasise_message(display_important_message)



emphasise_and_display_important_message= emphasise(display_important_message)
emphasise_and_display_important_message()

emphasise_and_display_important_message= emphasise(display_boring_message)
emphasise_and_display_important_message()

print("================================")

display_important_message()
display_boring_message()
