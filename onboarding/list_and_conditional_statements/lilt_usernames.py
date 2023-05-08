usernames = ['admin', 'dimo', 'dimitar', 'ivailo10', 'five']

if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would to like to see a status report')
        else:
            print(f'Hello {username}')
else:
    print('We need to find some user')