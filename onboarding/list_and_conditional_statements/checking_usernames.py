current_usernames = ['admin', 'dimo', 'dimitar', 'ivailo10', 'five']
new_usernames = ['pesho1', 'dimo', 'stamat40', 'pesho10', 'ivailo10']

for new_username in new_usernames:
    if new_username in current_usernames:
        print('Username has already been used')
    else:
        print('Username is available')