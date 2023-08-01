from flask import render_template
from backend.db import cursor


def home_view():
    sql_query = 'SELECT course_name FROM course_info;'
    cursor.execute(sql_query)
    course_name = cursor.fetchall()
    return render_template('homepage.html', **locals())