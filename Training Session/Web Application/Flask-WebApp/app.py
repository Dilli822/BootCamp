

# import sqlite3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///contact.db'
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    # password = db.Column(db.String(25), nullable=False)
    # repeat_password = db.Column(db.String(25), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    
    # string representation
    def __str__(self):
        return f'user is {self.name}'


@app.route('/')
def home():
    return render_template('form.html')


if __name__ == '__main__':
    app.run()



