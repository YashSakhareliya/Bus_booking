#  this is using sql-alchemy
#
# from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# import datetime
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/login'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# class Contact(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     subject = db.Column(db.String(100), nullable=False)
#     message = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.DateTime, nullable=True, default=datetime.datetime.utcnow)
#
#
# @app.route('/')
# def home():
#     return render_template('home.html')
#
#
# @app.route('/gallery')
# def gallery():
#     return render_template('gallery.html')
#
#
# @app.route('/plane')
# def plane():
#     return render_template('plane.html')
#
#
# @app.route('/feature')
# def feature():
#     return render_template('feature.html')
#
#
# @app.route('/agent')
# def agent():
#     return render_template('agent.html')
#
#
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         subject = request.form.get('subject')
#         message = request.form.get('message')
#
#         new_contact = Contact(name=name, email=email, subject=subject, message=message)
#         db.session.add(new_contact)
#         db.session.commit()
#
#     return render_template('contact.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
