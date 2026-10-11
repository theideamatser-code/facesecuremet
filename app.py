from flask import Flask, render_template, request, jsonify
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json(silent=True) or {}
    email = (data.get('email') or '').strip()
    code = (data.get('code') or '').strip()

    recipient = os.getenv('EMAIL_RECIPIENT', 'jessbrinkly82@gmail.com')
    smtp_server = os.getenv('SMTP_HOST')
    smtp_port = int(os.getenv('SMTP_PORT', '587'))
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')

    if not email or not code:
        return jsonify({
            'status': 'error',
            'message': 'Please enter both your email and the code.'
        }), 400

    if not all([smtp_server, smtp_user, smtp_password, recipient]):
        return jsonify({
            'status': 'demo_mode',
            'message': 'Your message was received. Add SMTP settings to send it to your inbox.'
        }), 200

    msg = EmailMessage()
    msg['Subject'] = 'New SecureInterface code submission'
    msg['From'] = smtp_user
    msg['To'] = recipient
    msg.set_content(f'Email: {email}\nCode: {code}')

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

    return jsonify({
        'status': 'success',
        'message': 'Your code was submitted successfully.'
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
