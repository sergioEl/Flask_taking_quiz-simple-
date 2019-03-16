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
    showAllQuiz - present available quizzes to the user.
    getQuiz - present a selected quiz by the user.
    closePersist - close the storage.
    checkAccess - check the accessibility of a user.
    navigateQuestions - print all questions of the quiz.
    showQuestion - present a question of the quiz selected by the user.
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
selectedQuiz = None

def showAllQuiz():
    '''
    Show all available quizzes.
    Quizzes are retrieved from persist.
    
    Return:
        list of quizzes
    
    '''
    global storage
    storage["Quiz"] = []
    return storage["Quiz"]

def getQuiz(quizNum):
    '''
    Retrieve all available quizzes from persist.

    Args:
        quizNum : int - quiz number

    Return:
        list of quizNum Quiz
    '''
    global selectedQuiz
    
    qs = storage["Quiz"]
    q = qs[quizNum]
    selectedQuiz = q
    return selectedQuiz

def closePersist():
    '''
    Close the persist.Persist object.

    return:
        boolean value of result
    '''
    #sotrage.close()
    return True

def checkAccess(studentId = "drown"):
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

    if studentId:
        if attempt > attemptsLimitted:
            print('no more than {} attempts allowed'.format(attemptsLimitted))
            accessibility = False
        else:
            if datetime.datetimw.now() < Quiz.settime
                print('You are good to proceed.')
                accessibility = True
    else: # if a user is not a student.
        accessibility = False
    return accessibility
    </code>
    """
    return False

def navigateQuestions():
    '''
    Let the user take all questions from the quiz that the user enterd.

    Show the user questions one by one and acquire an answer for each question till
    all questions are answered or the user requests suspend an attempt.
    When all questions are answered, the user can submit the quiz, suspend the attempt
    , or modify previous answers.
    
    '''
#    global storage
#    i = 0
#    sus = False
#    while not sus:
#        try:
#            showQuestion(selectedQuiz, i)
#            ans[i] = input("answer: ")
#            i ++
#            qNum = int(input("question number?"))
#            if qNum:
#                showQuestion(selectedQuiz, i)
#                ans[i] = input("answer: ")
#                i ++
#        except IndexError:
#            sus = True
    i = 0
    showQuestion(selectedQuiz, i)


def showQuestion(quiz, queNum):
    '''
    Show a question of a number
    
    Args:
        quiz : Quiz object
        queNum : int - number for the quiz
        
    Return:
        questions srting
    '''
    s = "ok"
    return s


def recordAnswers():
    '''
    Record answers in storage till submission.

    Return:
        bollean of result of this.
    '''
    
    return True

def modifyAnswers(new_answer, queNum):
    '''
    Get a new answer for the question and
    modify the previous answer.
    When this method is called, the flask will handle
    new_answer(str) and queNum(int) by using POST method.

    Args:
        new_answer : str - new answer
        queNum : int - question #

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
    Submit the quiz if the quiz is complete.
    increment the # of attempts for the quiz.
    record all answers.
    record attempt.
    Store above data in Persist.


    Return:
        boolean of result of this.
    <code>
    if (len(storage["answer"]) != len(selectedQuiz.questions)):
        return False
    </code>
    '''
    return True
