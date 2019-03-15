#!/usr/bin/env python3
## COMP2005 assignment5
## Seokho Han 201761541
## Programmer_3_take_quiz
"""Take quiz

    Shows all available quizzes to user,
    user can select specific quiz,
    check accessibility(type of user, time, and # of attempts),
    navigate questions after accessibility is authenticated,
    record / modify answers till a user submits the quiz,
    suspend current attempt so that user can continue the quiz till submission,
    and record all attempts with its status(complet / incomplete).

    Construct TakeQuiz object and user can interact with it through flask.

    This module uses data that are retrieved from Persist module.

"""

'''
    Take quiz
    
    Attributes:
    storage : persist.Persist object - of quizzes, questions,
    quizattempts, and users.
    quiz : object - shared_classes.Quiz object.
    Quiz._questions : list - of Question objects.
    Quiz._is_submitted : boolean - submission of quiz.
    questions : list - of shared_classes.Question object.
    quizAttempts: list - of shared_classes.QuizAttempt object.
    studentId : string - student ID.
    submit : boolean - (True:submitted / False:not submitted).
    attemp : integer - count # of attempts.
    answers : list - of answers.
    
    Methods:
    closePersist - close the storage.
    checkAccess - check the accessibility of a user.
    navigateQuestions - print all questions of the quiz.
    recordAnswers - record answers completed.
    modifyAnswers - modify answers of a quiz.
    suspendAttempts - suspend user attempts for later submission.
    recordAttempts - record # of attempts and update.
    submitQuiz - submit a quiz.
    '''
import os
import sys
import datetime
#import persist


storage = {}

def getQuiz(quizNum):
    '''
    Retrieve all available quizzes from persist.

    Return:
        obgject of quizNum Quiz
    '''
    
    return Quiz(quizNum)

def closePersist():
    '''
    Close the persist.Persist object.

    return:
        boolean value of result
    '''
    #sotrage.close()
    return True

def checkAccess():
    """
    This will check accessibility of a user
    by checking if the user is a student,
    if the time is within valid period, and
    if # of attempts exceed the # which quiz creator set up.

    Return:
        boolean value of accessibility.

    <code>
    attemptsLimitted = 3 # This will be retrieved from persist.
    accessibility = True

    if self.studentId: # if a user has a studentId, it menas he's a student.
        print('User is logged in')
        if self.attempt > attemptsLimitted:
            print('no more than {} attempts allowed'.format(attemptsLimitted))
        else:
            print('You are good to proceed.')
            accessibility = True
            return accessibility
    else: # if a user is not a student.
        print('Login first.')
        userID = input("ID : ")
        password = input("Password : ")
        return accessibility
    </code>
    """
    return True

def navigateQuestions():
    '''
    Let the user take all questions from the quiz that the user enterd.

    Return:
        list of questions.

    This method will provide three choices.
    One is for submission when all questions have answers,
    and one is for modifying answers whenever user wants to change,
    and the other is for suspending current attempt.


    <code>
    if self.questions:# if questions are existing.
        return self.questions
    else:# if there is no question.
        e = []
        return e
    </code>
    '''
    return self.questions

def recordAnswers():
    '''
    Record answers in storage till submission.

    Return:
        bollean of result of this.
    '''
    return True

def modifyAnswers():
    '''
    Get a new answer for the question and
    modify the previous answer.
    When this method is called, the flask will handle
    new_answer(str) and question_#(int) by using POST method.

    Return:
        boolean of result of this.

    <code>
    newAnswer = "My new anwer 1"
    questionNumber = 0
    self.answers[questionNumber] = newAnswer
    </code>
    '''
    return True

def suspendAttempts():
    '''
    Suspend attempt for later submission.
    This method will change a boolean value in persist
    so that when the user resumes the quiz,
    # of quiz attempts won't be incremented.

    Return:
        boolean of result of this.
        
    <code>
    self.submit = False
    quiz._is_submitted = self.subimt
    </code>
    '''
    return True

def recordAttempts():
    '''
    Store # of attempts that a user tries in storage.

    Return:
        boolean of result of this.
    '''

    return True

def submitQuiz():
    '''
    Submit the quiz.
    increment the # of attempts for the quiz.
    record all answers.
    record attempt.


    Return:
        boolean of result of this.
    <code>
    self.submit = True
    if self.submit:
        self.attempt += 1
    self.recordAttempts()
    self.submit = False
    </code>
    '''
    return True

class Quiz:
    def __init__(self, qNum):
        self.title = "First Quiz"
        self.num = qNum
