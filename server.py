from flask import Flask, render_template, redirect, session,request,flash
import re
app=Flask(__name__)
app.secret_key="1234"
@app.route('/')
def index():
    session.clear()
    print "Hello"
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
    error_count=0
    error_message="The {} field can't be empty"
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    name_regex=re.compile('\d+')
    password=request.form['password']
    confirmation_password=request.form['confirm']
    email=request.form['email']
    def empty_input(arg):
        print "in"
        return len(arg)<1
    #check if empty
    keys=['email','first_name','last_name','password']
    for k in keys:
        if empty_input(request.form[k]):
            error_count+=1
            print error_message.format(k)
            flash(error_message.format(k))
    #email check
    if not EMAIL_REGEX.match(email):
        error_count+=1
        flash('Please correct the error in the email field before you submit')
    #check for password length
    if len(password) < 8:
        error_count+=1
        flash('A password has to be at least 8 characters in length ')
    #check if password==confirm_password
    if password != confirmation_password:
        error_count+=1
        flash('Password and password confirmation should match')
    #check if first_name or last_name contain numbers
    for i in ['first_name','last_name']:
        if name_regex.search(request.form[i]):
            error_count+=1
            print("heeeee")
            flash("Names can't have numbers in them")
    print error_count
    if error_count==0:
        flash('The form was submitted succesfully!')
        session['email']=email
        session['first_name']=request.form['first_name']
        session['last_name']=request.form['last_name']
        session['password']=password
        return render_template('show.html')
    return render_template('index.html')
app.run(debug=True)
