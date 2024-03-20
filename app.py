from flask import Flask, render_template, request, redirect
import mysql.connector
import datetime

app = Flask(__name__)

# MySQL configurations
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'login'
}

conn = mysql.connector.connect(**mysql_config)

def create_contact_table():
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            subject VARCHAR(100) NOT NULL,
            message VARCHAR(100) NOT NULL,
            date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

create_contact_table()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/plane')
def plane():
    return render_template('plane.html')

@app.route('/feature')
def feature():
    return render_template('feature.html')

@app.route('/agent')
def agent():
    return render_template('agent.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contact (name, email, subject, message) VALUES (%s, %s, %s, %s)
        """, (name, email, subject, message))
        conn.commit()

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
