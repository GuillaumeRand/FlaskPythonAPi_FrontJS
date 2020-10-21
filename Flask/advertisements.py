
def getAdvertisements():
    cursor.execute('Select * from Advertisements')
    data = cursor.fetchall()
    return jsonify(data)

@app.route("/insertAdv", methods=["POST"])
def insertAdvertisement():
    IdUser = int(request.json['IdUser'])
    IdJob = int(request.json['IdJob'])
    if IdUser and IdJob:
        cursor.callproc('sp_insertAdvertisement', (IdUser, IdJob))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Advertisement created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


def deleteAdvertisement():
    IdAdv = request.json['IdAdv']
    if IdAdv:
        cursor.execute('DELETE FROM Advertisement where Id='+str(idAdv))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Advertisement deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})
