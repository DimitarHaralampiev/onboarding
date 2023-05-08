def build_profile(first, last, **user_info):
    """Make a dictionary for person info"""
    profile = {
        'first_name': first.title(),
        'last_name': last.title()
    }
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile


user_profile = build_profile('dimitar', 'haralampiev',
                             location='sofia',
                             field='programmer')

print(user_profile)

