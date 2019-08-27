from flask import Flask, escape, request, render_template, url_for

"""
In terminal, go to flask_blog:

- export FLASK_APP=flaskblog.py
- set FLASK_APP=flaskblog.py (for windows)
- flask run
"""

app = Flask(__name__)

posts = [
    {
        'author': 'Hugh Nguyen',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'Misato Yoshimoto',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2019'
    }
]

# route is what we type into our browser to go to different pages


@app.route('/')
@app.route('/home')
def home():
    # name = request.args.get("name", "Hieu Q Nguyen")
    # return f'<h1>Home Page: Hello, {escape(name)}!</h1>'

    # Now using the "posts" arg to pass through the home.html
    return render_template('home.html', posts=posts)

# Navigate to the About page


@app.route('/about')
def about():
    return render_template('about.html', title='About')

# The below will allow to make changes to the browser without having to kill the session everytime
# there is an update. To run: instead of "flask run" we will use "python flaskblog.py"


if __name__ == '__main__':
    app.run(debug=True)
