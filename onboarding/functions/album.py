def make_album():
    """Make a dictionary with albums"""
    album = {
        'name': 'Album'
    }
    album_one = {
        'name_one': 'Album One'
    }
    album_two = {
        'name_two': 'Album Two'
    }
    return album, album_one, album_two


print(make_album())