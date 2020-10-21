
def getUser():
    cursor.execute('Select * from User')
    data = cursor.fetchall()
    return jsonify(data)


def PostUsers():
    name = request.json['Name']
    lastname = request.json['Lastname']
    age = int(request.json['Age'])
    email = request.json['Email']
    password = request.json['Password']
    category = int(request.json['Category'])
    if name and email and password and lastname and age:
        cursor.callproc('sp_insertUser', (name, lastname,
                                          age, email, password, category))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route("/updateUser/", methods=['POST'])
def updateUser():
    id = int(request.json['Id'])
    name = request.json['Name']
    lastname = request.json['Lastname']
    age = int(request.json['Age'])
    email = request.json['Email']
    password = request.json['Password']
    category = int(request.json['Category'])
    if name and email and password and lastname and age:
        cursor.callproc('sp_updateUser', (id, name, lastname,
                                          age, email, password, category))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User updated successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route("/removeUser/", methods=['DELETE'])
def deleteUser():
    idd = request.json['Id']
    if idd:
        cursor.execute('DELETE FROM User where id='+str(idd))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})
