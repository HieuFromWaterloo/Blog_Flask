from flask import Flask, escape, request, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm
"""
In terminal, go to flask_blog:

- export FLASK_APP=flaskblog.py
- set FLASK_APP=flaskblog.py (for windows)
- flask run
"""

app = Flask(__name__)

# Set Secret Keys:
"""
>>> import secrets
>>> secrets.token_hex(16)
'b68fa0df2acd5d395596950f0d00c951'
"""
app.config["SECRET_KEY"] = 'b68fa0df2acd5d395596950f0d00c951'

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

# Create Register Route


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # Need to validate the forms before submitting
    if form.validate_on_submit():  # if the form is validated
        # send a message in flask, with the 2nd arg as the format of the message "success"
        flash(f"Account created for {form.username.data}!", "success")
        # after the form has been validated, we redirect the user to the home page
        return redirect(url_for('home'))
        # NOTE: we need to update the template the show the flash message
        # Go to layout.html to update this
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
