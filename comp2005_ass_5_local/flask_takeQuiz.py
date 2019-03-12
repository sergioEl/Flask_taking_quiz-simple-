#!/usr/bin/env python3
## COMP2005 assignment5
## Seokho Han 201761541
## Programmer_3_take_quiz
'''
flask module for takeQuiz.py
'''

import os
import sys
import datetime
from takeQuiz import TakeQuiz
#import persist

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

# Load default config and override config from an environment variable

app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    KEY='0'
))
t = TakeQuiz()

@app.route('/')
def check():
    return str(t.checkAccess())

@app.route('/questions')
def question():
    q = t.navigateQuestions()
    return render_template('show_entries.html', entries=q)

@app.route('/record')
def record():
    return t.recordAnswers()    

@app.route('/sus')
def sus():
    return str(t.suspendAttempts())

@app.route('/modi')
def modi():
    return t.modifyAnswers()

@app.route('/recordAttempt')
def recordAt():
    return str(t.recordAttempts())

@app.route('/submit')
def submit():
    return t.submitQuiz()
    
