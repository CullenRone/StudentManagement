import math

from flask import render_template, request, redirect, session, jsonify
import dao
# import utils
from app import app, login
from flask_login import login_user, logout_user, login_required
@app.route('/')
def index():
    kw = request.args.get('kw')
    year_id = request.args.get('year_id')
    # class_id = request.args.get('class_id')
    # subject_id = request.args.get('subject_id')
    page = request.args.get('page')
    Years = dao.load_years()
    Grades = dao.load_grades()
    Subjects = dao.load_subjects()
    Scores = dao.load_scores()
    students = dao.load_students(kw, year_id)
    countstu = dao.count_students()

    return render_template('index.html', years=Years, students=students, grades=Grades, scores=Scores, pages=math.ceil(countstu / app.config['PAGE_SIZE']))

@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')

@app.route('/api/class', methods='post')
def add_to_class():
    pass

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)