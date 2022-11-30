from flask import Flask, render_template, url_for
app = Flask(__name__)

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