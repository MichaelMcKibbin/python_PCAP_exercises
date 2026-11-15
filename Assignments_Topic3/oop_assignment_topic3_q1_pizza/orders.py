from pizza import Pizza

print('********************Welcome to PizzaLand********************'.center(100))

print('Pizza sizes available: ', str(Pizza.display_pizza_sizes()))
print()
print('Pizza toppings available: ', str(Pizza.display_toppings_available()))
print()

order_no = 1
print('Order No: ',order_no)
pizza1 = Pizza(10,'Large',['Parsley','Sweetcorn'])
print()

order_no += 1
print('Order No: ',order_no)
pizza2 = Pizza(10,'Large',['Turnip','Sweetcorn'])
print()

order_no += 1
print('Order No: ',order_no)
pizza3 = Pizza(5,'Small',['Ham','Pineapple'])
print()

order_no += 1
print('Order No: ',order_no)
pizza4 = Pizza(5,'Tiny',['Ham','Pineapple'])
print()

order_no += 1
print('Order No: ',order_no)
pizza5 = Pizza(10,'Large',['Spinach','Black Olives'])
print()

print('**********Summary Statistics**********')
print(f'No. of Pizzas Sold: {Pizza.get_no_of_pizzas_sold()}\n',f'Average Price of a Pizza: {Pizza.get_average_pizza_price()}\n', f'Total Price of Pizzas Sold: {Pizza._sum_of_sold_pizza_prices}\n')
print()
print('***********Have a nice day!***********')

