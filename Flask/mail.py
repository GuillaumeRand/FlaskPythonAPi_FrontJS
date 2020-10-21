
@app.route("/mails/", methods=["GET"])
def mails():
    cursor.execute("SELECT * FROM Mail ")
    # Select all data in database
    data = cursor.fetchall()
    # render templates
    return jsonify(data)


def postMail():
    content = request.json['Content']
    id_advertissements = int(request.json['Id_Advertissements'])

    if content and id_advertissements:
        cursor.callproc('sp_insertUser', (content, id_advertissements))

        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Mail created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


def updateMail():
    id = int(request.json['Id'])
    content = request.json['Content']
    id_advertissements = int(request.json['Id_Advertissements'])

    if content and id_advertissements:
        cursor.callproc('sp_updateMail', (id, content, id_advertissements))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Mail updated successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


def deleteMail():
    idd = request.json['Id']
    if idd:
        cursor.execute('DELETE FROM User where id='+str(idd))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Mail deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

