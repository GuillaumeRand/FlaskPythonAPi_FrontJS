exec(compile(source=open('config.py').read(), filename='config.py', mode='exec'))
# exec(compile(source=open('category.py').read(), filename='category.py', mode='exec'))
# exec(compile(source=open('advertisements.py').read(),
#              filename='advertisements.py', mode='exec'))
# exec(compile(source=open('company.py').read(), filename='company.py', mode='exec'))
# exec(compile(source=open('job.py').read(), filename='job.py', mode='exec'))
# exec(compile(source=open('mail.py').read(), filename='mail.py', mode='exec'))
# exec(compile(source=open('user.py').read(), filename='user.py', mode='exec'))
exec(compile(source=open('auth.py').read(), filename='auth.py', mode='exec'))
exec(compile(source=open('dashboard.py').read(), filename='dashboard.py', mode='exec'))


@app.route('/getInfoJob/', methods=['GET'])
def getInfoJob():
    param = request.args.get('param', 'null', type=str)
    cursor.execute("Select Company.Name, Category.Title from Job, Company, Category Where Job.Id_Company=Company.Id and Job.Id_Category=Category.Id and Job.Id="+param)
    data = cursor.fetchall()
    return jsonify(data)


@app.route("/", methods=["GET", "POST"])
def main():
    cursor.execute("select Job.Id, Job.Title, Content, Company.Name, Category.Title from Job, Company, Category Where Job.Id_Company=Company.Id and Job.Id_Category=Category.Id ")
    data = cursor.fetchall()
    # render templates
    return render_template('index.html', value=data)


@app.route("/users/<id>/", methods=['GET'])
def GetUsersId(id):
    cursor.execute("SELECT * FROM User WHERE Id="+id)
    data = cursor.fetchall()
    # render templates
    # return json.dumps(data)
    return json.dumps(data)


@app.route("/validate", methods=['POST'])
def validate():
    _name = request.json['name']
    _lastname = request.json['lastname']
    _age = request.json['age']
    _category = 0
    _email = request.json['email']
    _password = request.json['password']
    _job = request.json['job']
    _message = request.json['message']
    if _name and _email and _password and _lastname and _age:
        # _hashed_password = generate_password_hash(_password)
        # _hashed_password))
        # return copie of data and use sp_createUser -> create a new user in database with this information
        cursor.callproc('sp_insertUserMailAdv', (_name, _lastname,
                                                 _age, _email, _password, _category, _job, _message))
        data = cursor.fetchall()
# 0 is OK and 1 or 2 is erro
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User created successfully ! An Email was sent to the owner of this Job.'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/validateLog", methods=['POST'])
def validateLog():
    _user = request.json['user']
    _job = request.json['job']
    _message = request.json['message']
    print(_user + " " + _job + " " + _message)
    if _job and _user and _message:
        # _hashed_password = generate_password_hash(_password)
        # _hashed_password))
        # return copie of data and use sp_createUser -> create a new user in database with this information
        cursor.callproc('sp_insertAdMail', (_job, _user, _message))
        data = cursor.fetchall()
# 0 is OK and 1 or 2 is erro
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'An Email was sent to the owner of this Job.'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/showSignIn/', methods=['GET'])
def showSignUp():
    return render_template('registerForms.html')

@app.route("/getProfile", methods=["GET"])
def getProfile():
    cursor.execute("SELECT * FROM User WHERE Id="+str(session['id']))
    data = cursor.fetchone()
    if session['category']==0:
        cursor.execute('SELECT Job.Title, Job.Content from Advertisements, Job Where Advertisements.Id_Job = Job.Id AND Advertisements.Id_User ='+str(session['id']))
        adv = cursor.fetchall()
    else:
        cursor.execute('SELECT Job.Id, Job.Title, Job.Content From Job where Job.Id_RH ='+str(session['id']))
        adv = cursor.fetchall()
    # render templates
    return render_template('profile.html', value=data, adv =adv)


@app.route('/signIn/', methods=['POST'])
def signIn():
    _name = request.form["inputName"]
    _lastname = request.form['inputLastName']
    _age = int(request.form['inputAge'])
    _category = request.form['inputCategory']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    # validate the received values
    if _name and _email and _password and _lastname and _age:
        # _hashed_password = generate_password_hash(_password)
        # _hashed_password))
        # return copie of data and use sp_createUser -> create a new user in database with this information

        _password = generate_password_hash(_password, method='sha256')
        cursor.callproc('sp_insertUser', (_name, _lastname,
                                          _age, _email, _password, _category))
        data = cursor.fetchall()
# 0 is OK and 1 or 2 is erro
        if len(data) == 0:
            conn.commit()
            # flash('You were successfully created account')
            return redirect('/login/'), json.dumps({'message': 'User created successfully !'})
        else:
            return redirect('/login/'),json.dumps({'error': str(data[0])})

    else:
        return redirect('/showSignIn/'),json.dumps({'html': '<span>Enter the required fields</span>'})


def delete(id, table):
    if id and table:
        cursor.callproc('sp_delete'+table, (id))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': table+' removed successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route('/rhAddJob', methods=["GET", "POST"])
def rhAddJob():
    if request.method == 'GET':
        cursor.execute('SELECT * from Category')
        category = cursor.fetchall()
        cursor.execute('Select Id, Name from Company')
        company = cursor.fetchall()
        return render_template('rhAddJob.html', category = category, company = company)
    elif request.method == 'POST':
        title = request.json['title']
        content = request.json['content']
        company = request.json['company']
        category = request.json['category']
        rh = request.json['rh']
        if title and content:
            cursor.callproc('sp_insertJob', (title, content, company, category, rh))
            data = cursor.fetchall()
            if len(data) == 0:
                conn.commit()
                return json.dumps({'message': 'Job created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/removeJob", methods=["POST"])
def removeJob():
    idM = request.json['id']
    if idM:
        cursor.execute("DELETE FROM Job where Id="+str(idM))
        data = cursor.fetchall()
        if len(data)==0:
            conn.commit()
            return json.dumps({'message': 'Job deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run(debug=True)

