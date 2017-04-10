import sqlite3

class pysqlite3(object):
        def __init__(self):
                self.conn = sqlite3.connect('../data/database.sqlite3.db')

        def get_db(self):
                conn = sqlite3.connect(self.dbname)
                self.conn = conn

        def query_db(self, query): #Lancia query
                #print 'esecuzione query'
                cursor = self.conn.execute(query)
                self.conn.commit()
                result = cursor.fetchall()
                if len(result)==0:
                        return None
                else:
                        return result

        def close_db(self):
                self.conn.close()

'''
ESEMPI:

QUERY generica

db = pysqlite3()

query = """
SELECT *
FROM event
"""

result = db.query_db(query)
print result  # ritorna una lista (Matrice a due dimensioni)

db.close_db()
'''
