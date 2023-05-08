def make_album(name, title):
    """Make a dictionary album"""
    album = {
        name: title
    }
    return album


while True:
    name = input()
    if name == 'quit':
        break
    title = input()
    print(make_album(name, title))
