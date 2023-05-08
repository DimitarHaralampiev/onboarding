class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize variables"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Return restaurant info"""
        return f'Restaurant name: {self.restaurant_name.title()} with ' \
               f'Cuisine: {self.cuisine_type.title()}\nNumber served: {self.number_served}'

    def open_restaurant(self):
        """Return state restaurant"""
        return 'Restaurant is open'

    def set_number_served(self, number):
        """Increment number served"""
        self.number_served += number


restaurant = Restaurant('sasa', 'sushi')
restaurant.set_number_served(10)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

