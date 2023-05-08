python_learning = 'python_learning.txt'

"""Print three times contains in .txt"""
for _ in range(3):
    with open(python_learning) as file_object:
        contents = file_object.read()
        print(contents.rstrip())

print(f'\n')

"""Print one time contains in .txt"""
with open(python_learning) as file_object:
    content = file_object.read()
print(content.rstrip())

print(f'\n')

"""Print with readlines"""
list_content = ''
with open(python_learning) as file_object:
    lines = file_object.readlines()
for line in lines:
    list_content += line
print(list_content.rstrip())
