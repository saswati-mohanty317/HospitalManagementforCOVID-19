
from flask_sqlalchemy import SQLAlchemy
import os
from forms import SearchForm
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)



app.config['SECRET_KEY'] = 'mysecretkey'

#SQL MODEL
basedir=os.path.abspath(os.path.dirname(__file__))
print(basedir)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Covid_Patient(db.Model):
    __tablename__='covid_patient'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    status = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )
class Doctor(db.Model):
    __tablename__ = 'flasksqlalchemy-doctors'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    department = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )

    timing = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    available = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )


    def __repr__(self):
        return '<User {}>'.format(self.username)

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    age = db.Column(
        db.String(80),
        index=True,
        unique=True,
        nullable=False
    )

    location_room= db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    location_bed = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )
    status = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )
    visting_time = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )
    Num_vistors = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/list', methods=['GET', 'POST'])
def show_all():
    # Grab a list of doctors from database.
    doctors = Doctor.query.all()
    return render_template('appointment.html', users=doctors)


@app.route('/search', methods=['GET'])
def doc_records():
    """Create a user via query string parameters."""
    form = SearchForm()

    if form.validate_on_submit():
        department1=form.department.data
        existing_user = Doctor.query.filter(
            User.department == department
        ).first()
        return redirect(url_for('display_doc'))
    return render_template('search_doc.html',form=form)

@app.route('/pat',methods=['GET'])
def show_pat():
        # Grab a list of doctors from database.
    patients = Patient.query.all()
    return render_template('patient_list.html', users=patients)

@app.route('/covid',methods=['GET'])
def covid_pat():
    covid=Covid_Patient.query.all()
    return render_template('covid_pat.html',users=covid)

if __name__ == '__main__':
    app.run()
