import sqlite3

conn = sqlite3.connect("fb.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()



#cursor.execute("""CREATE TABLE feedbackdb(name text, company text, improve text)""")

class Dboperator:

    def __init__(self):

        pass