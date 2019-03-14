#!/usr/bin/env python3
## COMP2005 assignment5
## Seokho Han 201761541
## Programmer_3_take_quiz
"""Take quiz

    Check accessibility(type of user, time, and # of attempts),
    navigate questions after accessibility is authenticated,
    record / modify answers till a user submits the quiz,
    suspend current attempt so that user can continue the quiz till submission,
    and record all attempts with its status(complet / incomplete).

    Construct TakeQuiz object and user can interact with it through flask.

    This module uses data that are retrieved from Persist module.

    class:
        TakeQuiz - user can take a quiz by creating this object.
"""

import os
import sys
import datetime
#import persist

session = {'username' : None,
           'logged_in' : False}
           #'attemp' : None}
attemptsLimitted = 3


__all__ = ["TakeQuiz"]

class TakeQuiz:
    '''Take quiz

        Attributes:
            storage : persist.Persist object - of quizzes, questions,
            quizattempts, and users.
                quiz : object - shared_classes.Quiz object.
                    Quiz._questions : list - of Question objects.
                    Quiz._is_submitted : boolean - submission of quiz.
                questions : list - of shared_classes.Question object.
                quizAttempts: list - of shared_classes.QuizAttempt object.
            submit : boolean - (True:submitted / False:not submitted).
            attemp : integer - count # of attempts.
            answers : list - of answers.

        Methods:
            closePersist - close the storage.
            checkAccess - check the accessibility of a user.
            modifyAnswers - modify answers of a quiz.
            navigateQuestions - print all questions of the quiz.
            recordAnswers - record answers completed.
            recordAttempts - record # of attempts and update.
            submitQuiz - submit a quiz.
            suspendAttempts - suspend user attempts for later submission.
        '''
    def __init__(self, quizId = 0, studentId = 0):
        '''
        Args:
            quizID - valid quiz id for a quiz
            studentId - valid student id
        '''
        print('__init()__')
        #storage = persist.Persist()
        #quiz = storage.get_quiz("quiz ID")
        #quizAttempts = storage.get_quiz_attempts_by_student(quizID, stuID)
        self.questions =["This is question_1", "This is question_2"] #quiz._questions
        
        self.submit = False#quiz._is_submitted# should be added
        self.attempt = 0 #initial value
        self.answers = ["first answer is always free"]

    def closePersist(self):
        '''
        Close the persist.Persist object.
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

        Return:
            boolean value of accessibility.
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
        Let the user take all questions from the quiz that the user enterd.

        Return:
            list of questions.

        This method will provide three choices.
        One is for submission,
        and one is for modifying answers,
        and the other is for suspending current attempt.
        
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
        Record answers till submission.

        Return:
            list of answers checked.
        '''
        if not self.checkAccess():
            print('login first to record your answers!')
            return 'login first and record ! haha!'
        else:
 #           quizAttempts._answers = answers
            return 'your answers are recorded!'
        
    def modifyAnswers(self, answer, questionNumber = 0):
        '''
        Get a new answer for the question and
        modify the previous answer.

        Args:
            answer : string - answer for a questions
            questionNumber : integer - # of the question

        Return:
            msg - message back to the user the result of modification
        '''
        newAnswer = input("Answer : ")
        self.answers[questionNumber] = newAnswer
        #return newAnswer
        return "The question's answer is modified!"
         
    def suspendAttempts(self):
        '''
        Suspend attempt for later submission
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
        Store numbers of attempts in the persistence data.
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

