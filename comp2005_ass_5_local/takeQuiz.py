## COMP2005 assignment5
## Seokho Han 201761541
## Programmer_3_take_quiz

'''
check access
- student and time
- limit number of attempts

navigate questions

record / modify answers untill submission

suspend attempt for later completion/submission

record all complete or incomplete attempts
'''

import os
import sys
import datetime
import persist

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

session = {'username' : None,
           'logged_in' : Flase,
           'attemp' : None}
attemptsLimitted = 3



# Load default config and override config from an environment variable
app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    KEY='0'
))

class TakeQuiz:

    def __init__(self):
        print('__init()__')
        quiz = storage.get_quiz("quiz ID")
        self.questions = quiz.questions()# list
        
        self.submit = quiz.isSubmitted()# should be added
        self.attempt = storage.getAttempts()
        
    @app.route('/checkAccess')
    def checkAccess(self):
        '''
        This will check accessibility of a user
        by checking if the user is lgged in,
        if the user is a student,
        if the time is within valid period, and
        if attempts of the user exceed the limitation which quiz creator set up.
        '''
        accessibility = False
        if 'logged_in' in session and session['logged_in']:
            print('User is logged in')
            if session['attemp'] > attemptsLimitted:
                print('no more than {} attempts allowed'.format(attemptsLimitted))
            else:
                if isStudent(session['username']):
                    print('You are good to proceed.')
                    accessibility = True
                    return accessibility
        else:
            print('Login first.')
            return accessibility

    def navigateQuestions(self):
        '''
        show the user all questions from the quiz that the user enterd 
        '''
        if self.submit:
            self.attempt += 1
        self.printQuestions()
       
        print("question---")


    def recordAnswers(self, questionNumber):
        '''
        record answers till submission
        '''
        if not self.checkAccess():
            print('login first!')
            return 'login first!'

        userAnswers = storage.addAnswers(questionNumber, answer)

    def modifyAnswers(self, questionNumber):
        '''
        get a new answer for the question and
        modify answers that have been saved in storage
        '''
        newAnswer = input("Answer : ")
        storage.editAnswers(questionNumber, newAnswer)
        
        
    def suspendAttempts(self):
        '''
        suspend attempt for later submission
        set self.submit False and
        update persist date to current status of submission 
        '''
        self.submit = False
        storage.updateSubmit(self.subimt)

    def recordAttempts(self):
        '''
        store numbers of attempts the persistence data
        '''
        storage.updateAttempt(self.attempt)

    def submitQuiz(self):
        '''
        submit function
        '''
        self.submit = True

if __name__ == "__main__":
    import sys

    storage = persist.Persist('Brown.dat')

    app = Flask(__name__)
