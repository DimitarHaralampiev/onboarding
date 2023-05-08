favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python'
}

poll_names = ['phill', 'john', 'jen', 'tom', 'angelina']

for name in favorite_languages.keys():
    if name in poll_names:
        print(f'Thanks for your responding {name}')
    else:
        print(f'Please give your vote {name}')
