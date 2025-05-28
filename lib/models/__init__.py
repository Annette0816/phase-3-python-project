import sqlite3

CONN = sqlite3.connect('recordlabel.db')
CONN.row_factory = sqlite3.Row
CURSOR = CONN.cursor()