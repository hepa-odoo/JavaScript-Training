def odooGetData():
    import xmlrpc.client
    import json
    db = "odoo_enterprise"
    username = "admin"
    password = "admin"

    common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})

    if uid:
        print ("Connection Successful")

    models = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/object')

    #models.execute_kw(db, uid, password, 'estate.property', 'create', [{'name': 'Avsar party plot', 'expected_price':108000000,'state': 'new'}])
    #print("record created :-)")

    results = models.execute_kw(db, uid, password, 'estate.property', 'search_read', [[],['name']])
    print(results)
    results = {k:v for (k,v) in zip([str(x) for x in range(0,len(results))],results)}
    print(results)
    return json.dumps(results)