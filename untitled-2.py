from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))