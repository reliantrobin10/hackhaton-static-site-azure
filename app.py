from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/subject')
def subject():
    return render_template('Subject.html')

@app.route('/AI_assist.html')
def ai_assist():
    return render_template('AI_assist.html')

@app.route('/quiz.html')
def quiz():
    return render_template('quiz.html')

@app.route('/assignment.html')
def assignment():
    return render_template('assignment.html')

@app.route('/teaching.html')
def teaching():
    return render_template('teaching.html')
