from collections import OrderedDict

words_and_description = OrderedDict()

words_and_description['variable'] = 'correct name with value'
words_and_description['statement'] = 'block code'
words_and_description['loop'] = 'item traversal'
words_and_description['list'] = 'mutable ordered list'
words_and_description['tuple'] = 'immutable ordered list'

for key, value in words_and_description.items():
    print(f'{key.title()}: {value.title()}')
