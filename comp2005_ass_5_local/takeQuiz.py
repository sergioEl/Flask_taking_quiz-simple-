#!/usr/bin/env python3
## COMP2005 assignment5
## Seokho Han 201761541
## Programmer_3_take_quiz
"""
    check access
    - student and time
    - limit number of attempts

    navigate questions

    record / modify answers untill submission

    suspend attempt for later completion/submission

    record all complete or incomplete attempts
"""

import os
import sys
import datetime
#import persist

#from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

session = {'username' : None,
           'logged_in' : False}
           #'attemp' : None}
attemptsLimitted = 3




class TakeQuiz:
    
    def __init__(self):
        '''
        attributs:
            quiz - quiz object.
            questions - list of questions.
            submit - boolean value (True : submitted / False : not submitted).
            attemp - integer, count # of attempts.

        methods:
            checkAccess - check the accessibility of a user.
            modifyAnswers - modify answers of a quiz.
            navigateQuestions - print all questions of the quiz.
            recordAnswers - record answers completed.
            recordAttempts - record # of attempts and update.
            submitQuiz - submit a quiz.
            suspendAttempts - suspend user attempts for later submission.
        '''
        print('__init()__')
        #quiz = storage.get_quiz("quiz ID")
        self.questions = ["This is question_1", "This is question_2"]#quiz.questions()# list
        
        self.submit = False #quiz.isSubmitted()# should be added
        self.attempt = 0 #storage.getAttempts()
        self.answers = ["hi"]
    
    def checkAccess(self):
        """
        This will check accessibility of a user
        by checking if the user is lgged in,
        if the user is a student,
        if the time is within valid period, and
        if attempts of the user exceed the limitation
        which quiz creator set up.
        """
        accessibility = False
        if 'logged_in' in session:#session['logged_in']:
            print('User is logged in')
            if self.attempt > attemptsLimitted:
                print('no more than {} attempts allowed'.format(attemptsLimitted))
            else:
                #if isStudent(session['username']):
                    print('You are good to proceed.')
                    accessibility = True
                    return accessibility
        else:
            print('Login first.')
            userID = input("ID : ")
            password = input("Password : ")
            return accessibility

    def navigateQuestions(self):
        '''
        show the user all questions from the quiz that the user enterd.
        '''
        if self.submit:
            self.attempt += 1
        #self.printQuestions()
        s = ' '.join(self.questions)
        print("question--- %s" %s)
        return self.questions

   
    def recordAnswers(self):
        '''
        record answers till submission.
        '''
        if not self.checkAccess():
            print('login first to record your answers!')
            return 'login first and record ! haha!'
        else:
            return 'your answers are recorded!'
        #for answer in self.answers:
            #quizAttempts._answers.append(answer)
        
        

    def modifyAnswers(self, questionNumber = 0):
        '''
        get a new answer for the question and
        modify answers that have been saved in storage.
        '''
        newAnswer = input("Answer : ")
        self.answers[questionNumber] = newAnswer
        #storage.get_quiz(quiz_ID Here)
        return newAnswer
        
        
    def suspendAttempts(self):
        '''
        suspend attempt for later submission
        set self.submit False and
        update persist data to current status of submission.
        '''
        self.submit = False
        #storage.updateSubmit(self.subimt)
        print("Your attempt is suspended.")
        return self.submit

    def recordAttempts(self):
        '''
        store numbers of attempts in the persistence data.
        '''
        #storage.updateAttempt(self.attempt)
        print("Your record is recorded : %d." %self.attempt)
        #quiz.add_quiz_attempt(quizAttempts)
        return self.attempt

    def submitQuiz(self):
        '''
        submit function.
        '''
        self.submit = True
        print("Your submit is processed")
        return "Your submit is processed"

def main():
    '''
    This is for testing
    '''
    t = TakeQuiz()
    t.checkAccess()
    t.navigateQuestions()
    t.recordAnswers()
    t.suspendAttempts()
    t.modifyAnswers()
    t.recordAttempts()
    t.submitQuiz()
    print(t.answers[0])
    

if __name__ == "__main__":
    import sys

    #storage = persist.Persist('Brown.dat')
    #quiz = storage.get_quiz(quiz_ID Here)
    #questions = quiz.get_questions() - list of all questions
    #quizAttempts = quiz.get_quiz_attempts_by_student(stuID)
    
    main()

