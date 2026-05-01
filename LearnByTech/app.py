from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Course, Video
from models import Enrollment
from flask import session
app = Flask(__name__)
app.secret_key = "mysecretkey123"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2004@localhost/lms_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('home.html')


# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(
            username=request.form['username'],
            email=request.form['email'],
            password=request.form['password'],
            role=request.form['role'] 
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()

        if user:
            session['user_id'] = user.id
            session['role'] = user.role   

            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials"

    return render_template('login.html')


# ---------------- VIDEOS ----------------
@app.route('/videos')
def video_list():
    videos = Video.query.all()
    return render_template('video_list.html', videos=videos)


@app.route('/video/add', methods=['GET', 'POST'])
def video_form():
    courses = Course.query.all()   

    if request.method == 'POST':
        video = Video(
            title=request.form['title'],
            url=request.form['url'],
            course_id=request.form['course_id']
        )
        db.session.add(video)
        db.session.commit()

        return redirect(url_for('video_list'))

    return render_template('video_form.html', courses=courses)
#------------------COURSE----------------------------
@app.route('/course/<int:id>')
def course_detail(id):
    course = Course.query.get(id)
    return render_template('course_detail.html', course=course)
@app.route('/courses')
def course_list():
    courses = Course.query.all()
    return render_template('course_list.html', courses=courses)   
@app.route('/course/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course = Course(
            title=request.form['title'],
            description=request.form['description']
        )
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('course_list'))

    return render_template('course_form.html') 
#---------------ENROLLMENT--------------------
@app.route('/enroll/<int:course_id>')
def enroll(course_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    enrollment = Enrollment(
        user_id=session['user_id'],
        course_id=course_id
    )

    db.session.add(enrollment)
    db.session.commit()

    return redirect(url_for('dashboard'))

# ---------------- CREATE TABLES ----------------
@app.before_request
def create_tables():
    db.create_all()
#------------------------Dashboard-------------------
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if session['role'] == 'teacher':
        courses = Course.query.all()
        return render_template('teacher_dashboard.html', courses=courses)

    else:
        enrollments = Enrollment.query.filter_by(user_id=session['user_id']).all()
        return render_template('student_dashboard.html', enrollments=enrollments)

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)