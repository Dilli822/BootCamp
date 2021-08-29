

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQALCHEMY_DATABASE_URL'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)

class Mydb(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(25), nullable=False)
   email = db.Column(db.String(25), nullable=False)
   message = db.Column(db.String(120), nullable=False)


   def __init__(self, name, email, message):
       self.name = name
       self.email = email
       self.message = message

   def __str__(self):
       return f'user is {self.name}'


@app.route('/')
def home():
    return render_template('form.html', Mydb = Mydb.query.all())


if __name__ == '__main__':
    db.create_all()
    app.run()    