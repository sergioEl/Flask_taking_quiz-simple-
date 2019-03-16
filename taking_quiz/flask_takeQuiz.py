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
import takeQuiz 
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


@app.route('/')
def check():
    flash("Accessibility : " + str(takeQuiz.checkAccess()))
    return redirect(url_for('question'))
    #return str(t.checkAccess())

@app.route('/questions')
def question():
    q = takeQuiz.navigateQuestions()
    return render_template('show_entries.html', entries=q)

@app.route('/record')
def record():
    flash("Record : " + str(takeQuiz.recordAnswers()))
    return redirect(url_for('question'))
 #   return t.recordAnswers()    

@app.route('/sus')
def sus():
    flash("suspend : " + str(takeQuiz.suspendAttempts()))
    return redirect(url_for('question'))
 #   return str(t.suspendAttempts())

@app.route('/modi')
def modi():
    flash("modify : " + str(takeQuiz.modifyAnswers("1", 0)))
    return redirect(url_for('question'))
    #return t.modifyAnswers()

@app.route('/recordAttempt')
def recordAt():
    flash("attempt recorded : " + str(takeQuiz.recordAttempts()))
    return redirect(url_for('question'))
 #   return str(t.recordAttempts())

@app.route('/submit')
def submit():
    flash("submission : " + str(takeQuiz.submitQuiz()))
    return render_template('show_entries.html', entries=[])
 #   return redirect(url_for('question'))
    #return t.submitQuiz()
    
