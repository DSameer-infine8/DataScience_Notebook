from flask import Flask, session, render_template, request, Response

app = Flask(__name__)

@app.route("/")
def student_profile():
    return render_template("profile.html", 
                           name = "Sameer",
                           is_topper= False,
                           subjects=['Maths', 'Science', 'CS'])
    
    
#Inherintence (Uses- Jinja )

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')