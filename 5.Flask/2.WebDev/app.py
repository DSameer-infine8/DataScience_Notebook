from flask import Flask, session, render_template, request, Response

app = Flask(__name__)

@app.route("/")
def student_profile():
    return render_template("profile.html", 
                           name = "Sameer",
                           is_topper= False,
                           subjects=['Maths', 'Science', 'CS'])