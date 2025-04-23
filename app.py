from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key = 'secretkey'
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login', methods=['POST'])
def login():
    if request.form['password']=='bestpasswordever':
        session['logged_in']=True
        return redirect('/secret')
    return 'Wrong password buddy, <a href="/">Try again</a>'
@app.route('/secret')
def secret():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('secret.html')
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)