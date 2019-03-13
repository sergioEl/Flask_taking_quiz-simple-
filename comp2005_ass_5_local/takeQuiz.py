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
import persist

#from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

session = {'username' : None,
           'logged_in' : False}
           #'attemp' : None}
attemptsLimitted = 3




class TakeQuiz:
    
    def __init__(self):
        '''
        attributs:
            storage - persist of quizzes, questions, quizattempts, and users.
                quiz:
                    Quiz._questions - list of Question objects.
                    Quiz._is_submitted - boolean variable.
                questions - list of questions.
                quizAttempts:
                    QuizAttempt._answers - list of all answers.
            self.submit - boolean value (True:submitted / False:not submitted).
            self.attemp - integer, count # of attempts.
            self.answers - list of answers.

        methods:
            closePersist - close the storage.
            checkAccess - check the accessibility of a user.
            modifyAnswers - modify answers of a quiz.
            navigateQuestions - print all questions of the quiz.
            recordAnswers - record answers completed.
            recordAttempts - record # of attempts and update.
            submitQuiz - submit a quiz.
            suspendAttempts - suspend user attempts for later submission.
        '''
        print('__init()__')
        #storage = persist.Persist('Brown.dat')
        #quiz = storage.get_quiz("quiz ID")
        #quizAttempts = storage.get_quiz_attempts_by_student(quizID, stuID)
        self.questions =["This is question_1", "This is question_2"] #quiz._questions# list
        
        self.submit = False#quiz._is_submitted# should be added
        self.attempt = 0 #initial value
        self.answers = ["first answer is always free"] #

    def closePersist(self):
        '''
        close the persist.
        '''
 #       sotrage.close()
        return "storage closed"
    
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
        if 'logged_in' in session:#and session['user_type'].equals('s'):
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
        if self.questions:#If questions are existing.
            s = ' '.join(self.questions)
            print("question--- %s" %s)
            return self.questions
        else:
            s = "There is no question created yet!"
            print("question--- %s" %s)
            return s
       
        

   
    def recordAnswers(self):
        '''
        record answers till submission.
        '''
        if not self.checkAccess():
            print('login first to record your answers!')
            return 'login first and record ! haha!'
        else:
 #           quizAttempts._answers = answers
            return 'your answers are recorded!'
        
    def modifyAnswers(self, questionNumber = 0):
        '''
        get a new answer for the question and
        modify the previous answer.
        '''
        newAnswer = input("Answer : ")
        self.answers[questionNumber] = newAnswer
        #return newAnswer
        return "The question's answer is modified!"
         
    def suspendAttempts(self):
        '''
        suspend attempt for later submission
        set self.submit False and
        update persist data to current status of submission.
        '''
        self.submit = False
 #       quiz._is_submitted = self.subimt
        print("Your attempt is suspended.")
       # return self.submit
        return "Current attempt suspended!" 

    def recordAttempts(self):
        '''
        store numbers of attempts in the persistence data.
        '''
 #       newQuizAttempt = QuizAttempt(student, st_time, end_time, answers)
 #       storage.add_quiz_attempt(quizID, student, newQuizAttempt)
        print("Your record is recorded \n your attempts: %d." %self.attempt)

 #       return self.attempt
        return "Current attempt is recorded in the server now!"

    def submitQuiz(self):
        '''
        Submit the quiz.
        This will increment the # of attempts for the quiz.
        '''
        self.submit = True
        
        if self.submit:
            self.attempt += 1
        
 #       quiz._is_submitted = self.subimt
        self.recordAttempts()
        self.submit = False
#        quiz._is_submitted = self.subimt
                
        print("submission processed")
        return "Your submission is processed"

##def main():
##    '''
##    This is for testing
##    '''
##    t = TakeQuiz()
##    t.checkAccess()
##    t.navigateQuestions()
##    t.recordAnswers()
##    t.suspendAttempts()
##    t.modifyAnswers()
##    t.recordAttempts()
##    t.submitQuiz()
##    print(t.answers[0])
##    
##
##if __name__ == "__main__":
##    import sys    
##    main()

