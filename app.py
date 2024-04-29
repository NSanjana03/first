# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:33:27 2024

@author: user
"""

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def show_students():
        #Example list of names and ages
        students=[
            {"name" :"mithal","grade": 88},
            {"name" :"suprithi","grade": 89},
            {"name" :"prajna","grade": 90},
            {"name" :"sanjana","grade":91},
            {"name":"noothan","grade":92},
        ]
        passing_grade=80
        return render_template('grade.html', students=students,passing_grade=passing_grade)
app.run(debug=True)
