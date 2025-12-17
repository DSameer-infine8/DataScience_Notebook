from flask import Flask, session, render_template, request 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("form.html")

@app.route('/submit', methods = ['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    '''
    if username == "sameer8" and password=="888":
        return render_template("welcome.html",name= username)
    '''
    
    valid_users = {
        'admin':'123',
        'sameer8':'888',
        'okok':'098',
        'don': 'not_possible'
    }
    
    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html",name= username)
    else:
        return "In-valid User..."