
@app.route("/category/", methods=["GET"])
def category():
    cursor.execute("SELECT * FROM Category ")
    # Select all data in database
    data = cursor.fetchall()
    # render templates
    return jsonify(data)


def postCategory():
    title = request.json['Title']
    if title:
        cursor.callproc('sp_insertCategory', (title))

        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Category created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


def updateCategory():
    id = int(request.json['Id'])
    title = request.json['Title']

    if title:
        cursor.callproc('sp_updateCategory', (id, title))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Category updated successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


def deleteCategory():
    idd = request.json['Id']
    if idd:
        cursor.execute('DELETE FROM Category where id='+str(idd))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Category deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

