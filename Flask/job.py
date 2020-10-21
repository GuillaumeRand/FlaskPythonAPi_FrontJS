
@app.route("/jobs/", methods=["GET"])
def jobs():
    cursor.execute("SELECT * FROM Job ")
    # Select all data in database
    data = cursor.fetchall()
    # render templates
    return jsonify(data)


def postJob():
    title = request.json['Title']
    content = request.json['Content']
    id_company = int(request.json['Id_Company'])
    id_category = int(request.json['Id_Category'])
    if title and content and id_company and id_category:
        cursor.callproc('sp_insertJob', (title,
                                         content, id_company, id_category))

        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'job created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


def updateJob():
    id = int(request.json['Id'])
    title = request.json['Title']
    dateadded = request.json['DateAdded']
    content = request.json['Content']
    id_company = int(request.json['Id_Category'])
    id_category = int(request.json['Id_Company'])

    if title and dateadded and content and id_company and id_category:
        cursor.callproc('sp_updateJob', (id, title, dateadded,
                                         content, id_company, id_category))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Job updated successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


def deleteJob():
    idd = request.json['Id']
    if idd:
        cursor.execute('DELETE FROM User where id='+str(idd))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Job deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

