#!/usr/bin/env python3
## COMP2005 assignment5
## Seokho Han 201761541
## Programmer_3_take_quiz

"""Take quiz

    Shows all available quizzes to a user,
    a user can select a specific quiz,
    check accessibility(type of the user, time, and # of attempts),
    navigate questions after accessibility authentication is done,
    record / modify answers till the user submits the quiz,
    suspend current attempt so that # of attempts remain,
    and record all attempts with its status(complet / incomplete).

    Construct TakeQuiz object and user can interact with it through flask.

    This module uses data that are retrieved from Persist module.

"""

'''
    Take quiz
    
    Attributes:
        storage : Persist() - shelve of persist.Persist()
        selectedQuiz : Quiz - Quiz obj selected
        quizAttempt : quizAttempt - current quizAttempt object
        user : User - User object that is attempting this quiz
    
    Methods:
        showAllQuiz - present available quizzes to the user.
        getQuiz - present a selected quiz by the user.
        closePersist - close the storage.
        checkAccess - check the accessibility of a user.
        navigateQuestions - present all questions of the selected quiz
                            get answers for the questions.
        showQuestion - present a question of the quiz selected by the user.
        recordAnswers - record answers completed and store in persist.
        modifyAnswer - modify an answer of a question.
        suspendAttempts - suspend user attempts for later submission.
        recordAttempts - record current attempt in persist.
        submitQuiz - submit a quiz.
    '''
import os
import sys
import datetime
from persist import Persist


storage = Persist() # persist.Persist()
selectedQuiz = None # Quiz obj selected
quizAttempt = None # My quiz attempt
user = None # User who attempting a quiz

def showAllQuiz(studentId = "brown"):
    '''
    Show all available quizzes which are assigned to a student.
    Quizzes are retrieved from persist.

    Args:
    studentId : int - student ID
  
    Return:
        list of quizzes
    
    '''
    try:
        q = storage.get_assigned_quizzes(studentId)
        return q
    except :
        return("There is no quiz at all.", studentId)
        #raise
 #   print(q)
#    return q

def getQuiz(quizNum = None):
    '''
    Retrieve all available quizzes from persist.

    Args:
        quizNum : int - quiz number

    Return:
        list of quizNum Quiz
    '''
    global selectedQuiz
    if not quizNum:
        qs = showAllQuiz()
        qn = input("Quiz number? ")
        q = qs[qn]
        selectedQuiz = q
    return selectedQuiz

def closePersist():
    '''
    Close the persist.Persist object.

    return:
        boolean value of result
    '''
    
    storage.close()
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
    global user, quizAttempt
    ans = []
    
    quizId = selectedQuiz.quiz_ID# quiz Id for the quiz that the user selects.
    user = storage.get_user(studentId)
    #check the type of a user
    if user.user_type == 's':
        timeNow = datetime.datetime.now()
        # check the time
        if  (timeNow >= selectedQuiz.start_time and\
           timeNow <= selectedQuiz.end_time) :
            # check # of attempts
            if ( len(storage.get_all_attempts_for_quiz(quizId)) >\
                 selectedQuiz.attempts_allowed):
                print("pass!")
                quizAttempt = QuizAttempt(user, datetime.datetime.now(), 0, ans, False)
                return "Accessibility check done"
            else:
                return "Your attempts is full."
        else:
            return "Time is done"
    else:
        return "You are not a student."
    
    return False

def navigateQuestions():
    '''
    Let the user take all questions from the quiz that the user enterd.

    Show the user questions one by one and acquire an answer for each question till
    all questions are answered or the user requests suspend an attempt.
    When all questions are answered, the user can submit the quiz, suspend the attempt
    , or modify previous answers.

    Raise:
        IndexError - When the user answers all questions.
    
    '''
    global storage, quizAttempt
    
    time = datetime.datetime.now()
    quizAttempt.start_time = time
    
    i = 0
    sus = False #suspended? no
    while not sus:
        try:
            showQuestion(selectedQuiz, i)
            ans = input("answer: ")
            recordAnswer(i, ans)
            i += 1
            qNum = int(input("question number?"))
            if qNum:
                showQuestion(selectedQuiz, i)
                ans[i] = input("answer: ")
                i += 1
        except IndexError:
            sus = True


def showQuestion(quiz, queNum):
    '''
    Show a question of a number
    
    Args:
        quiz : Quiz object
        queNum : int - number for the question
        
    Return:
        questions srting
    '''
    s = "ok"
    question = quiz.questions[queNum].question # get the question str.
    s = question
    return s


def recordAnswer(queNum, ans):
    '''
    Record an answer in persist till submission.

    Args:
        queNum : int - question number.
        ans : str - answer string.
    '''
    global quizAttempt
    
    quizAttempt.answers[queNum] = ans #answer storing
    recordAttempts()
    

def modifyAnswers(newAnswer, queNum):
    '''
    Get a new answer for the question and
    modify the previous answer.
    When this method is called, the flask will handle
    new_answer(str) and queNum(int) by using POST method.

    Args:
        newAnswer : str - new answer.
        queNum : int - question #.
    '''

    global quizAttempt
    
    quizAttempt.answers[queNum] = newAnswer


def suspendAttempts():
    '''
    Suspend attempt for later submission.
    This method will change quizAttempt.is_submitted to False.
    When the user resumes the quiz, a new quizAttempt obj won't be added.

    '''
    global quizAttempt
    
    quizAttempt.is_submitted = False # quizAttempt is suspended.
    recordAttempts() # record this quizAttempt

def recordAttempts():
    '''
    Store quizAttempt obj in persist.
    When the list of quizAttempt is empty,
    append the quizAttempt ojb to the end of the list in persist.
    When previous quizAttempt is not submitted yet,
    change the unsubmitted quizAttempt obj to current one.
    '''
    global storage
    
    quizId = selectedQuiz.quiz_ID # quiz ID of selected quiz.
    allAttempts = storage.get_all_attempts_for_quiz(quizId)
    if (allAttempts == None): # empty
        storage.add_quiz_attempt(quizId, user, quizAttempt)
    else: # not enmpty
        for i in len(allAttempts):
            if (allAttempts[i].is_submitted == False): # not submitted
                storage["quiz_attempts"][i] = quizAttempt # assign quizAttempt
                break
            else:
                if (i == len(allAttempts) - 1): # append quizAttempt
                    storage.add_quiz_attempt(quizId, user, quizAttempt)
                    break

def submitQuiz():
    '''
    Submit the quiz if all the questions of the quiz have been answered.
    Store quizAttempt object in Persist.
    
    
    Return:
        True for successfully submit a quiz.

    '''
    global quizAttempt
    if (len(quizAttempt.answers) != len(selectedQuiz.questions)):
        return "Answer all the questions first!!!"
        return False
    else:
        quizAttempt.is_submitted = True
        recordAttempts()
        return True
