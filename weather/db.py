from tinydb import TinyDB, Query
from tinydb.table import Document

db = TinyDB('users_db.json')

users_table = db.table('users')


