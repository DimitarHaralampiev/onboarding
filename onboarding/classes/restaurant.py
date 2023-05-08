class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize variables"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Return restaurant info"""
        return f'Restaurant name: {self.restaurant_name.title()} with ' \
               f'Cuisine: {self.cuisine_type.title()}'

    def open_restaurant(self):
        """Return state restaurant"""
        return 'Restaurant is open'


restaurant = Restaurant('sasa', 'sushi')
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
