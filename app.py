from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify
import random, smtplib, ssl, time
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'cybersecurity'  # secret key for session management

otp_db = {}  # store otp data

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_SENDER = 'vptaa.authorize@gmail.com'
EMAIL_PASSWORD = 'wskh volh ttsd lyhu'

def send_otp(email, otp):
    msg = MIMEText(f"""
    Dear User,

    Thank you for using VPTAA Authorization, your trusted cybersecurity partner.

    Your One-Time Password (OTP) for secure access is: {otp}

    This OTP is valid for 5 minutes. Please do not share this code with anyone.

    If you did not request this OTP, please contact our support team immediately.

    Stay secure,
    The VPTAA Authorization Team
    """)
    msg['Subject'] = 'Your Verification Code'
    msg['From'] = EMAIL_SENDER
    msg['To'] = email

    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/send_otp', methods=['POST'])
def send_otp_route():
    email = request.form.get('email')
    if not email:
        flash('Email field is required.')
        return redirect(url_for('index'))
    
    otp = str(random.randint(100000, 999999))
    otp_db[email] = (otp, time.time())
    send_otp(email, otp)
    session['email'] = email
    return redirect(url_for('verify'))

@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/verify_code', methods=['POST'])
def verify_code():
    entered_otp = request.form['otp']
    email = session.get('email')
    if not email or email not in otp_db:
        return redirect(url_for('index'))

    real_otp, timestamp = otp_db[email]
    if time.time() - timestamp > 300:  # otp expires in 5 minutes
        return render_template('expired.html')

    if entered_otp == real_otp:
        return redirect(url_for('secret'))
    else:
        return render_template('verify.html', error="Wrong OTP")  # Pass error message

@app.route('/secret')
def secret():
    return render_template('secret.html')

@app.route('/resend_otp', methods=['POST'])
def resend_otp():
    email = session.get('email')
    if not email:
        return redirect(url_for('index'))

    otp = str(random.randint(100000, 999999))
    otp_db[email] = (otp, time.time())
    send_otp(email, otp)
    return redirect(url_for('verify'))

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()  # clear session data
    return render_template('login.html')  # return to login page

if __name__ == '__main__':
    app.run(debug=True)