from flask import request, Flask, abort, redirect, url_for, render_template


app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    if request.method == 'POST':
        return render_template('%s.html')
    else:
        return render_template('qwerty.html')