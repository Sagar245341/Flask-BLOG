from flask import Flask, render_template, url_for
from form import RegistrationForm,LoginForm
app = Flask(__name__)
 
app.config['SECRET_KEY']="b95de7e5f867373d968343ffcc910958"
posts = [
    {
        'author': 'Sagar',
        'title': 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'Jan 31,2026'
    },
    {
        'author': 'Priyanshy',
        'title': 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'Feb 31,2026'
    }
]

@app.route('/')
@app.route('/home')
def home():
    # Added quotes around 'home.html'
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
   form = LoginForm()
   return render_template('login.html',title='Register',form=form)

@app.route('/register')
def register():
   form = RegistrationForm()
   return render_template('register.html',title='Register',form=form)
   

if __name__ == '__main__':
    app.run(debug=True)