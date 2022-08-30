import pymysql


def insertLogin():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345678',
        db='gopal'
    )
    cursor1 = connection.cursor()
    try:
        query = '''SELECT * FROM gopal.shop'''
        cursor1.execute(query)
        print(cursor1.fetchall())
        print(type(cursor1.fetchall()))
        connection.commit()
    finally:
        cursor1.close()
        connection.close()


insertLogin()
