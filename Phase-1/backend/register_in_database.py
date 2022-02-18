import psycopg2
def register_in_database_func(fname,lname,email,password):
    conn = psycopg2.connect(database="hetpatel", user='hetpatel', password='', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    result=cursor.execute("INSERT INTO customers0(fname, lname, email, password) VALUES('{}','{}','{}','{}')".format(fname,lname,email,password))
    print(result,", record created !!!")
    conn.commit()
    conn.close()
    return result