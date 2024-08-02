from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
from config import USER_DATA
from payment import user_accounts, process_payment
from analytics import generate_report
import folium

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# User data (username and passwords)
users = USER_DATA

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid Credentials')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        user_vehicle_id = int(username.split('user')[1])
        user_account = user_accounts[user_accounts['vehicle_id'] == user_vehicle_id]
        return render_template('dashboard.html', user_account=user_account)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/pay', methods=['POST'])
def pay():
    if 'username' in session:
        username = session['username']
        user_vehicle_id = int(username.split('user')[1])
        amount = request.form['amount']
        process_payment(user_vehicle_id, float(amount))
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/map')
def map_view():
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered on India
    folium.Marker([28.7041, 77.1025], popup="Toll Zone A").add_to(m)  # Example marker for New Delhi
    return m._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)
