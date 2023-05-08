class Privileges:

    def __init__(self):
        self.privileges = ['can delete post', 'can add post', 'can be user']

    def show_privileges(self):
        return ', '.join([privilege for privilege in self.privileges])