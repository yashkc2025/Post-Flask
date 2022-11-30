from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ed4827fa24888390c248e8100c02654c48a3d22d6202981d8d520d909559c3fd5c6703b3049ffcb6a5eec601fb1225ecc1547087b21456bd047bc4d2f8ce5a24985e91e1ad3778814b91e1c47bdd13b9f3123383f863aeb0515172315ed8f0275238f0'

posts = [
    {
        'author': 'Yash',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '30 November, 2022'
    },
    {
        'author': 'Yash',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '31 November, 2022'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(debug=True)