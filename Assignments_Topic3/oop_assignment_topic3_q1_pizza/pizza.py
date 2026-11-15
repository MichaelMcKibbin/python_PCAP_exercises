# Define the Pizza class

class Pizza:
    # class variables
    # single underscore is used to indicate that these variables are intended for internal use within the class
    _no_of_pizzas_sold = 0
    _sum_of_sold_pizza_prices = 0
    _toppings = ['Artichokes', 'Black Olives', 'Cheese', 'Chicken', 'Ham', 'Mushrooms', 'Pepperoni', 'Pineapple', 'Red Onion','Spinach', 'Sweetcorn', 'Tomato']
    _sizes = ['Small', 'Medium', 'Large']

    def __init__(self, price, size, toppings_requested):
        self._price = price

        try:
            if size not in Pizza._sizes:
                raise InvalidPizzaSizeException(
                    'Alert - Order Not Processed! A correct pizza size has not been specified: ' + size)
            else:
                self._size = size

            toppings_not_available = ''
            for i in range(0, len(toppings_requested)):
                if toppings_requested[i] not in Pizza._toppings:
                    toppings_not_available = toppings_not_available + '\n' + toppings_requested[i]

            if len(toppings_not_available) != 0:
                # raise an exception if any of the requested toppings are not available
                raise ToppingNotAvailableException(
                    'Alert - Order Not Processed! The following pizza toppings are not available. ' + toppings_not_available)
            else:
                self._toppings = toppings_requested

        except (InvalidPizzaSizeException, ToppingNotAvailableException) as e:
            print(e.get_error_message())

        else:
            # Update summary statistics
            Pizza._no_of_pizzas_sold += 1
            Pizza._sum_of_sold_pizza_prices += self._price
            print('Pizza Up! ' + self.__str__())

    def get_price(self):
        return self._price

    def get_size(self):
        return self._size

    def eat(self):
        return 'Eating a pizza.'

    def slice(self):
        return 'Slicing a pizza.'

    def take_out_of_box(self):
        return 'Take pizza out of box.'

    @staticmethod
    def display_toppings_available():
        return Pizza._toppings

    @staticmethod
    def display_pizza_sizes():
        return Pizza._sizes

    def __str__(self):
        return (' Size: ' + self._size + ' - ' 'Price: ' + str(self._price) + ' - ' + 'Toppings: ' + str(self._toppings))

    @staticmethod
    def get_no_of_pizzas_sold():
        return Pizza._no_of_pizzas_sold

    @staticmethod
    def get_average_pizza_price():
        average_price = 0
        try:
            average_price = Pizza._sum_of_sold_pizza_prices / Pizza._no_of_pizzas_sold
        except ZeroDivisionError:
            return 0
        else:
            return average_price


class ToppingNotAvailableException(Exception):
    def __init__(self, message):
        self._message = message;

    def get_error_message(self):
        return self._message


class InvalidPizzaSizeException(Exception):
    def __init__(self, message):
        self._message = message

    def get_error_message(self):
        return self._message


