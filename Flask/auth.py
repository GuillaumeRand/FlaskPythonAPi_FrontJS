
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        cursor.execute("SELECT * FROM User WHERE Email ='"+str(email)+"'")
        user = cursor.fetchone()
        if not user or not check_password_hash(user[5], password):
            flash('Please check your login details and try again.')
            return render_template('/login/')
        session['loggedin'] = True
        session['id'] = user[0]
        session['email'] = user[4]
        session['category'] = user[6]
        session['isAdmin'] = False
        return jsonify({"redirect": "/"})   

@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('email', None)
   session.pop('category', None)
   session.pop('isAdmin', None)
   # Redirect to login page
   return redirect('/')

