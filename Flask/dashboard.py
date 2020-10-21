

@app.route("/admin/", methods=["GET"])
def mainDash():
    if session:
        if session['isAdmin']==True:
            cursor.execute("select Job.Id, Job.Title, Content, Company.Name, Category.Title from Job, Company, Category Where Job.Id_Company=Company.Id and Job.Id_Category=Category.Id ")
            data = cursor.fetchall()
            return render_template('dashboard/index.html', value=data)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/dashCategory/", methods=["GET"])
def dashCategory():
    if session:
        if session['isAdmin']==True:
            cursor.execute("select * from Category")
            data = cursor.fetchall()
            # render templates
            return render_template('dashboard/category.html', value=data)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/dashAdvertisement/", methods=["GET"])
def dashAdvertisement():
    if session:
        if session['isAdmin']==True:
            cursor.execute("SELECT Advertisements.Id, Advertisements.Id_User, User.Email, Advertisements.Id_Job, Job.Title FROM `Advertisements`, Job, User WHERE Job.Id=Advertisements.Id_Job and User.Id=Advertisements.Id_User Order by Id")
            data = cursor.fetchall()
            return render_template('dashboard/advertisement.html', value = data)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/dashCompany/", methods=["GET"])
def dashCompany():
    if session:
        if session['isAdmin']==True:
            cursor.execute("SELECT * from Company")
            data = cursor.fetchall()
            return render_template('dashboard/company.html', value=data)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/dashMail", methods=["GET"])
def dashMail():
    if session:
        if session['isAdmin']==True:
            cursor.execute("SELECT * from Mail")
            data = cursor.fetchall()
            return render_template('dashboard/mail.html', value = data)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/dashUser", methods=["GET"])
def dashUser():
    if session:
        if session['isAdmin']==True:
            cursor.execute("SELECT * from `User`")
            data = cursor.fetchall()
            return render_template('dashboard/user.html', value = data)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/removeAdv", methods=["POST"])
def removeAdv():
    if session:
        if session['isAdmin']==True:
            idA = request.json['id']
            if idA:
                cursor.execute('DELETE FROM Advertisements where id='+str(idA))
                data = cursor.fetchall()
                if len(data) == 0:
                    conn.commit()
                    return json.dumps({'message': 'Advertisement deleted successfully !'})
                else:
                    return json.dumps({'error': str(data[0])})
            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/removeUser", methods=["POST"])
def removeUser():
    if session:
        if session['isAdmin']==True:
            idU = request.json['id']
            if idU:
                cursor.execute("DELETE FROM User where Id="+str(idU))
                data = cursor.fetchall()
                if len(data)==0:
                    conn.commit()
                    return json.dumps({'message': 'User deleted successfully !'})
                else:
                    return json.dumps({'error': str(data[0])})
            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/removeCategory", methods=["POST"])
def removeCategory():
    if session:
        if session['isAdmin']==True:
            idC = request.json['id']
            if idC:
                cursor.execute("DELETE FROM Category where Id="+str(idC))
                data = cursor.fetchall()
                if len(data)==0:
                    conn.commit()
                    return json.dumps({'message': 'Category deleted successfully !'})
                else:
                    return json.dumps({'error': str(data[0])})
            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/removeCompany", methods=["POST"])
def removeCompany():
    if session:
        if session['isAdmin']==True:
            idC = request.json['id']
            if idC:
                cursor.execute("DELETE FROM Company where Id="+str(idC))
                data = cursor.fetchall()
                if len(data)==0:
                    conn.commit()
                    return json.dumps({'message': 'Company deleted successfully !'})
                else:
                    return json.dumps({'error': str(data[0])})
            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/removeMail", methods=["POST"])
def removeMail():
    if session:
        if session['isAdmin']==True:
            idM = request.json['id']
            if idM:
                cursor.execute("DELETE FROM Mail where Id="+str(idM))
                data = cursor.fetchall()
                if len(data)==0:
                    conn.commit()
                    return json.dumps({'message': 'Mail deleted successfully !'})
                else:
                    return json.dumps({'error': str(data[0])})
            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/removeJob", methods=["POST"])
def dashRemoveJob():
    if session:
        if session['isAdmin']==True:
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
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/getUserUpdate<idU>", methods=["GET"])
def getUserUpdate(idU):
    if session:
        if session['isAdmin']==True:
            cursor.execute("SELECT * from `User` where Id="+idU)
            data = cursor.fetchall()
            return render_template('dashboard/update/updateUser.html', value = data)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/updateUser", methods=["POST"])
def updateUser():
    if session:
        if session['isAdmin']==True:
            id = request.json['id']
            name = request.json['name']
            lastname = request.json['lastname']
            age = int(request.json['age'])
            email = request.json['email']
            password = request.json['password']
            category = 0
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
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/getCategoryUpdate<idCat>", methods=["GET"])
def getCategoryUpdate(idCat):
    if session:
        if session['isAdmin']==True:
            cursor.execute("SELECT * from `Category` where Id="+idCat)
            data = cursor.fetchall()
            return render_template('dashboard/update/updateCategory.html', value = data)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/updateCategory", methods=["POST"])
def updateCategory():
    if session:
        if session['isAdmin']==True:
            id = int(request.json['id'])
            title = request.json['title']
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
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/getCompanyUpdate<idComp>", methods=["GET"])
def getCompanyUpdate(idComp):
    if session:
        if session['isAdmin']==True:
            cursor.execute("SELECT * from `Company` where Id="+idComp)
            data = cursor.fetchall()
            return render_template('dashboard/update/updateCompany.html', value = data)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/updateCompany", methods=["POST"])
def updateCompany():
    if session:
        if session['isAdmin']==True:
            idComp = int(request.json['id'])
            name = request.json['name']
            siret = int(request.json['siret'])
            if name and siret:
                cursor.callproc('sp_updateCompany', (idComp, name, siret))
                data = cursor.fetchall()
                if len(data) == 0:
                    conn.commit()
                    return json.dumps({'message': 'Company updated successfully !'})
                else:
                    return json.dumps({'error': str(data[0])})
            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/getJobUpdate<idJ>", methods=["GET"])
def getJobUpdate(idJ):
    if session:
        if session['isAdmin']==True:
            cursor.execute("SELECT * from `Job` where Id="+idJ)
            data = cursor.fetchall()
            cursor.execute("SELECT * FROM Company")
            selectComp = cursor.fetchall()
            cursor.execute("SELECT * From Category")
            selectCat = cursor.fetchall()
            return render_template('dashboard/update/updateJob.html', value = data, selectComp= selectComp, selectCat= selectCat)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/updateJob", methods=["POST"])
def updateJob():
    if session:
        if session['isAdmin']==True:
            id = int(request.json['id'])
            title = request.json['title']
            content = request.json['content']
            id_company = int(request.json['company'])
            id_category = int(request.json['category'])

            if title and content and id_company and id_category:
                cursor.callproc('sp_updateJob', (id, title,
                                                content, id_company, id_category))
                data = cursor.fetchall()
                if len(data) == 0:
                    conn.commit()
                    return json.dumps({'message': 'Job updated successfully !'})
                else:
                    return json.dumps({'error': str(data[0])})
            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/getMailUpdate<idM>", methods=["GET"])
def getMailUpdate(idM):
    if session:
        if session['isAdmin']==True:
            cursor.execute("SELECT * from `Mail` where Id="+idM)
            data = cursor.fetchall()
            return render_template('dashboard/update/updateMail.html', value = data)
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/updateMail", methods=["POST"])
def updateMail():
    if session:
        if session['isAdmin']==True:
            id = int(request.json['id'])
            content = request.json['content']
            if content:
                cursor.callproc('sp_updateMail', (id, content))
                data = cursor.fetchall()
                if len(data) == 0:
                    conn.commit()
                    return json.dumps({'message': 'Mail updated successfully !'})
                else:
                    return json.dumps({'error': str(data[0])})
            else:
                return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/addAdvertisement", methods=["GET", "POST"])
def addAdvertisement():
    if session:
        if session['isAdmin']==True:
            if request.method == 'GET':
                cursor.execute("Select Id, Email From User")
                user = cursor.fetchall()
                cursor.execute("Select Id, Title from Job")
                job = cursor.fetchall()
                return render_template('dashboard/add/addAdvertisement.html', user = user, job = job)
            elif request.method == "POST":
                IdUser = int(request.json['user'])
                IdJob = int(request.json['job'])
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
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/addCategory", methods=["GET", "POST"])
def addCategory():
    if session:
        if session['isAdmin']==True:
            if request.method == 'GET':
                return render_template('dashboard/add/addCategory.html')
            elif request.method == 'POST':
                title = request.json['title']
                param_list = [title]
                if title:
                    cursor.callproc('sp_insertCategory', (param_list))

                    data = cursor.fetchall()
                    if len(data) == 0:
                        conn.commit()
                        return json.dumps({'message': 'Category created successfully !'})
                    else:
                        return json.dumps({'error': str(data[0])})
                else:
                    return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/addCompany", methods=["GET", "POST"])
def addCompany():
    if session:
        if session['isAdmin']==True:
            if request.method == 'GET':
                return render_template('dashboard/add/addCompany.html')
            elif request.method == 'POST':
                name = request.json['name']
                siret = request.json['siret']
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
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/addJob", methods=["GET", "POST"])
def addJob():
    if session:
        if session['isAdmin']==True:
            if request.method == 'GET':
                cursor.execute('SELECT * from Category')
                category = cursor.fetchall()
                cursor.execute('Select Id, Name from Company')
                company = cursor.fetchall()
                cursor.execute('SELECT RH.Id_User, User.Email FROM User, RH where User.Id = RH.Id_User ')
                rh = cursor.fetchall()
                return render_template('dashboard/add/addJob.html', category = category, company = company, rh = rh)
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
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/addMail", methods=["GET", "POST"])
def addMail():
    if session:
        if session['isAdmin']==True:
            if request.method == 'GET':
                cursor.execute('SELECT Advertisements.Id, Concat(Job.Title, " - ", User.Email) FROM Advertisements, Job, User WHERE Advertisements.Id_User = User.Id AND Advertisements.Id_Job = Job.Id ')
                adv = cursor.fetchall()
                return render_template('dashboard/add/addMail.html', adv = adv)
            elif request.method == 'POST':
                content = request.json['content']
                adv = request.json['adv']
                if content and adv:
                    cursor.callproc('sp_insertMail', (content, adv))
                    data = cursor.fetchall()
                    if len(data) == 0:
                        conn.commit()
                        return json.dumps({'message': 'Mail created successfully !'})
                    else:
                        return json.dumps({'error': str(data[0])})
                else:
                    return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')

@app.route("/admin/addUser", methods=["GET", "POST"])
def addUser():
    if session:
        if session['isAdmin']==True:
            if request.method == "GET":
                return render_template('dashboard/add/addUser.html')
            elif request.method == 'POST':
                name = request.json['name']
                lastname = request.json['lastname']
                age = request.json['age']
                email = request.json['email']
                password = request.json['password']
                password = generate_password_hash(password, method='sha256')
                category = request.json['category']
                if name and lastname and age and email and password and category:
                    cursor.callproc('sp_insertUser', (name, lastname, age, email, password, category))
                    data = cursor.fetchall()
                    if len(data) == 0:
                        conn.commit()
                        return json.dumps({'message': 'User created successfully !'})
                    else:
                        return json.dumps({'error': str(data[0])})
                else:
                    return json.dumps({'html': '<span>Enter the required fields</span>'})
        else:
            return render_template('dashboard/dashLogin.html')
    else:
        return render_template('dashboard/dashLogin.html')


@app.route('/admin/login/', methods=['POST'])
def dashLogin():
        login = request.json['login']
        password = request.json['password']
        cursor.execute("SELECT * FROM IsAdmin WHERE login ='"+str(login)+"'")
        user = cursor.fetchone()
        if not user or not check_password_hash(user[1], password):
            return render_template('/admin/')
        session['isAdmin'] = True
        return jsonify({"redirect": "/admin/"})


@app.route('/admin/logout/', methods=["GET"])
def dashLogout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    session.pop('category', None)
    session.pop('isAdmin', None)
    return redirect('/')