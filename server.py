from flask import Flask, render_template, redirect, session, flash
app=Flask(__name__)
app.secret_key="1234"
@app.route('/')
def index():
    print "Hello"
    return render_template('index.html')
app.run(debug=True)
