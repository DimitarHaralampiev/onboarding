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


sushi_restaurant = Restaurant('sasa', 'sushi')
print(sushi_restaurant.describe_restaurant())

turkish_restaurant = Restaurant('drujba', 'turku')
print(turkish_restaurant.describe_restaurant())

wish_restaurant = Restaurant('merak', 'wish')
print(wish_restaurant.describe_restaurant())
