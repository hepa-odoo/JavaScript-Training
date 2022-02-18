def get_customers_func():
    import psycopg2
    conn = psycopg2.connect(database="hetpatel", user='hetpatel', password='', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    cursor.execute("SELECT fname,lname,email from customers0;")
    result = cursor.fetchall()
    print(result)
    conn.commit()
    conn.close()
    html="<h3>List of customers</h3><br/><table class='table col-sm-8'><tr><th scope='col'>First Name</th><th scope='col'>Last Name</th><th scope='col'>Email-id</th></tr>"
    for row in result:
        html+="<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(row[0],row[1],row[2])
    html+="</table>"
    print(html)
    return html