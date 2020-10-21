
def getAdvertisements():
    cursor.execute('Select * from company')
    data = cursor.fetchall()
    return jsonify(data)

def insertCompany():
    name = int(request.json['name'])
    siret = int(request.json['siret'])
    if name and siret:
        cursor.callproc('sp_insertCompany', (name, siret))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Company created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

def updateCompany():
    idComp = int(request.json['idComp'])
    name = int(request.json['name'])
    siret = int(request.json['siret'])
    if name and siret:
        cursor.callproc('sp_insertCompany', (idComp, name, siret))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Company updated successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

def deleteCompany():
    IdComp = request.json['IdComp']
    if IdComp:
        cursor.execute('DELETE FROM Company where Id='+str(IdComp))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Company deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})
