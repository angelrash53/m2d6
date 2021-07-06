from flask import Flask, render_template, redirect,request,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/login',methods= ['POST'])
def login():
    user = {
        'username': 'Tomashi',
        'password': '12345'
    }

    username = request.args.get('username')
    password = request.args.get('password')

    if username == user['username'] and password == user['password']:
        return redirect(url_for('scores', username = username))

@app.route('/scores', methods = ['POST'])
def scores():
    exams = [
        {
            'subjectname': 'python',
            'marks': '20/25',
            'date': '13-apr-2021'
        },
        {
            'subjectname': 'english',
            'marks': '20/25',
            'date': '13-apr-2021'

        },
        {
            'subjectname': 'Geography',
            'marks': '20/25',
            'date': '13-apr-2021'
        }
    ]

if __name__ == '__main__':
    app.run(debug = True)