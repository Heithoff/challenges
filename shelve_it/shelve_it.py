# From https://pybit.es/shelve-it.html

import shelve

db =shelve.open('data')

name = 'Marco'

db['db_names'] = name

db.close()

