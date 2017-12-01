import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(256))
    title = db.Column(db.String(256))
    desc = db.Column(db.String(256))
    prof_id = db.Column(db.Integer, db.ForeignKey('prof.id'))


class Prof(db.Model):
    __tablename__ = 'prof'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    department = db.Column(db.Text)
    courses = db.relationship('Courses', backref='prof', cascade="delete")


@app.route('/')
def home():
    # return '<h1>hello world!</h1>'
    return render_template('index.html')


@app.route('/courses')
def get_courses():
    courses = Courses.query.all()
    return render_template('courses.html', courses=courses)

@app.route('/profs')
def get_prof():
    prof = Prof.query.all()
    return render_template('profs.html', prof=prof)


@app.route('/about')
def get_about():
    # return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('about.html')


@app.route('/profs/add', methods=['GET', 'POST'])
def add_prof():
    if request.method == 'GET':
        return render_template('profs-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        department = request.form['department']

        # insert the data into the database
        prof = Prof(name=name, department=department)
        db.session.add(prof)
        db.session.commit()
        return redirect(url_for('get_prof'))


@app.route('/profs/edit/<int:id>', methods=['GET', 'POST'])
def edit_prof(id):
    prof = Prof.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('profs-edit.html', prof=prof)
    if request.method == 'POST':
        # update data based on the form data
        prof.name = request.form['name']
        prof.department = request.form['department']
        # update the database
        db.session.commit()
        return redirect(url_for('get_prof'))


@app.route('/courses/add', methods=['GET', 'POST'])
def add_courses():
    prof = Prof.query.all()
    if request.method == 'GET':
        prof = Prof.query.all()
        return render_template('courses-add.html', prof=prof)
    if request.method == 'POST':
        # get data from the form
        number = request.form['number']
        title = request.form['title']
        desc = request.form['desc']
        prof_name = request.form['prof']
        prof = Prof.query.filter_by(name=prof_name).first()
        courses = Courses(number=number, title=title, desc=desc, prof=prof)

        # insert the data into the database
        db.session.add(courses)
        db.session.commit()
        return redirect(url_for('get_courses'))


@app.route('/courses/edit/<int:id>', methods=['GET', 'POST'])
def edit_courses(id):
    courses = Courses.query.filter_by(id=id).first()
    prof = Prof.query.all()
    if request.method == 'GET':
        return render_template('courses-edit.html', courses=courses, prof=prof)
    if request.method == 'POST':
        # update data based on the form data
        courses.number = request.form['number']
        courses.title = request.form['title']
        courses.desc = request.form['desc']
        prof_name = request.form['prof']
        prof = Prof.query.filter_by(name=prof_name).first()
        courses.prof = prof
        # update the database
        db.session.commit()
        return redirect(url_for('get_courses'))


if __name__ == '__main__':
    app.run(debug=True)
