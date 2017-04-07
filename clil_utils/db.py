import sqlite3

class pysqlite3(object):
        def __init__(self, dbname):
                self.dbname = dbname
                self.conn = sqlite3.connect(self.dbname + '.db')

        def get_db(self):
                conn = sqlite3.connect(self.dbname + '.db')
                self.conn = conn

        def query_db(self, query):
                print 'esecuzione query'
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
db = pysqlite3('garau')

query = """
SELECT *
FROM event
"""

result = db.query_db(query)
print result
db.close_db()
'''