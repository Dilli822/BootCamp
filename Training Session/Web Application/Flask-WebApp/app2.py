
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.sqlite3'



db = SQLAlchemy(app)
class Contact(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(25), nullable=False)
   email = db.Column(db.String(25), nullable=False)
   message = db.Column(db.String(120), nullable=False)
   
   db.create_all()

   def __str__(self):
       return f'user is {self.name}'

@app.route('/success/')
def success():
    return render_template('success.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('your_name')
        email = request.form.get('email')
        message = request.form.get('message')
        contact = Contact(name=name, email=email, message=message)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug = True)
