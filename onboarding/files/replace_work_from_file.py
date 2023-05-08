python_learning = 'python_learning.txt'

with open(python_learning) as file_object:
    contains = file_object.read()
    content = contains.replace('API', 'WEB')
    print(content)