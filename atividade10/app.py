from flask import Flask, render_template, request, make_response, redirect, session
from datetime import datetime, timedelta, timezone

app = Flask(__name__, template_folder='templates')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)
app.secret_key = 'EXA844'

@app.route('/home')
def counter():
    # Variável oculta
    counter_value = request.args.get('counter',default=0, type=int) + 1    
    # Cookies
    if 'count_cookie' in request.cookies:
        count_cookie = int(request.cookies.get('count_cookie'))
    else:
        count_cookie = 1
    # Sessão
    if 'username' in session:
        username = session['username']
        running_time = (datetime.now(timezone.utc) - session.get('_creation_time'))
        remaining_time = app.permanent_session_lifetime - running_time
    else:
        return redirect('/')

    resp = make_response(render_template('counter.html', count_cookie=count_cookie, counter=counter_value, username=username, remaining_time=remaining_time, running_time=running_time))
    resp.set_cookie('count_cookie', str(count_cookie + 1).encode('utf-8'), max_age=60*60, secure=True, samesite=None)
    return resp

@app.route('/', methods=["GET"])
def start():
    return render_template('login.html')

@app.route('/', methods=["POST"])
def login():
    username = request.form['username']
    session['username'] = username
    session['_creation_time'] = datetime.now(timezone.utc)
    return redirect('/home')

if __name__ == '__main__':
    app.run(debug=True)