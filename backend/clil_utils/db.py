import sqlite3
import os


class pysqlite3(object):
        def __init__(self):
                dir = os.path.dirname(__file__)
                db_path = os.path.join(dir, '../../data/database.sqlite3.db')
                print db_path
                self.conn = sqlite3.connect(db_path)
        '''
        def get_db(self):
                conn = sqlite3.connect(self.dbname)
                self.conn = conn
        '''

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
FROM user
"""
result = db.query_db(query)
print result  # ritorna una lista (Matrice a due dimensioni)
db.close_db()
'''
