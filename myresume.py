from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    # return '<h1>hello world!</h1>'
    return render_template('index.html')


@app.route('/courses')
def get_courses():
    courses = {
        'MISY350',
        'BUAD345',
        'ACCT352'
    }
    message = {
        'Business Application Development II',
        'Decision Analytics and Visualization',
        'Law and Social Issues in Business'
    }
    return render_template('courses.html', courses=courses)
    return render_template('courses.html', message=message)



@app.route('/about')
def get_about():
    # return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
