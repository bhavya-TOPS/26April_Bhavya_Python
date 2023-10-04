# How will you randomizes the items of a list in place
import random
 
items = ['here', 'are', 'some', 'strings', 'of',
         'which', 'we', 'will', 'select', 'one']
 
rand_item = items[random.randrange(len(items))]