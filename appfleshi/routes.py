from flask import render_template
from flask_login import login_required

from appfleshi import app

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route("/profile/<username>")
@login_required
def perfil(username):

    return render_template('profile.html', username=username)