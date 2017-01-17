from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Lasse'}
    posts = [
        {
            'author': {'nickname' : 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'nickname': 'Lasse'},
            'body': 'Not everyone is walking around dead!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)