import shelve

db = shelve.open('data')

name = db['db_names']

print(name)

db.close()
