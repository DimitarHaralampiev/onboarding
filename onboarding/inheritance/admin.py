from classes.users import User
from inheritance.privileges import Privileges


class Admin(User):
    """Inherit class User from classes users"""

    def __init__(self, first_name, last_name, age, gender):
        """Inherit attributes from parent class and initialize attribute"""
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


admin = Admin('pesho', 'peshov', '24', 'male')
print(admin.describe_user())
print(admin.privileges.show_privileges())
