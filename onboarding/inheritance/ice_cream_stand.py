class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize variables"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Return restaurant info"""
        return f'Restaurant name: {self.restaurant_name.title()} with ' \
               f'Cuisine: {self.cuisine_type.title()}'


class IceCreamStand(Restaurant):
    """Inherit class Restaurant from classes number_served"""

    def __init__(self, restaurant_name, cuisine_type):
        """Inherit attributes from parent class and initialize attributes"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = \
            ['cherry', 'vanilla', 'chocolate']

    def display_flavours(self):
        """Print flavours"""
        print('You have available:')
        for flavour in self.flavours:
            print(f'- {flavour.title()}')


ice_cream = IceCreamStand('raffy', 'ice cream')
print(ice_cream.describe_restaurant())
ice_cream.display_flavours()

