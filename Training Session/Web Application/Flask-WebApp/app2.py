
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# db path and configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.sqlite3'


db = SQLAlchemy(app)
class Contact(db.Model):
    # making columns in the db
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(25), nullable=False)
   email = db.Column(db.String(25), nullable=False)
   message = db.Column(db.String(120), nullable=False)
   
   db.create_all()

   #user string representation
   def __str__(self):
       return f'user is {self.name}'


# For post method
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('your_name')
        email = request.form.get('email')
        message = request.form.get('message')

        # inserting the datas in the db contact
        contact = Contact(name=name, email=email, message=message)

        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('success'))
        # return redirect(url_for('contact_list'))

    return render_template('form.html')


# routing for successfully registering the form
@app.route('/success/')
def success():
    return render_template('success.html')


# bring contact data from db
@app.route('/contact-list/')
def contact_list():
    # we hitting query and extracting all data from db
    contacts = Contact.query.all()
    return render_template('contact_list.html', contacts=contacts)


# running our app
if __name__ == '__main__':
    app.run(debug = True)
