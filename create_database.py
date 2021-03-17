# import psycopg2
#
#
# def create_base():
#     db = psycopg2.connect(user='postgres', password='postgres',
#                           host='localhost')
#     cursor = db.cursor()
#     cursor.execute('SHOW DATABASES')
#     print(cursor.fetchall())
#     return db
