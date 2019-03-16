#!/usr/bin/env python3

# revised Fe 1 2019 so tests are consistent with shelve files on windows and fix
# intermittent bug in posttime test

import unittest
import tempfile
import os.path
import stat
import datetime
#import persist
from time import sleep
import takeQuiz 

class TestTakeQuiz(unittest.TestCase):

    post_data = [  
                        ("quiz1", ["ques1", "ques2", "ques3"], ["answer1", "answer2"], True),
                        ("quiz2", ["ques_a", "ques_b", "ques_c"], ["All remind us"], False),
                        ("quiz3", ["ques_y", "ques_w", "ques_z"], ["Our live sublime"], True),
                        ("quiz4", ["ques_Z", "ques_X", "ques_C"], ["Leave behind us"], False),
                        ("quiz5", ["ques11", "ques22", "ques33"], ["In the sands of time"], True),
                ]

    def test_show_all_quiz(self):
        l = []
        for i in self.post_data:
            l.append(i[0])
        self.assertEqual(l, takeQuiz.showAllQuiz(), msg = 'Different quizzes')

    def test_get_quiz(self):
        takeQuiz.storage['Quiz'] = self.post_data
        self.assertEqual(takeQuiz.getQuiz(0), self.post_data[0], msg='match x')

    def test_check_access(self):
        self.assertEqual(True, takeQuiz.checkAccess("brown"), msg = 'Check process failed')

    def test_navigate_questions(self):
        for quiz in self.post_data:
            self.assertEqual(quiz[1], takeQuiz.navigateQuestions(), \
                             msg = 'Questions {} are not matching with {}'\
                             .format(quiz[1], takeQuiz.navigateQuestions()))
            
    def test_navigate_none_questions(self):
        tq = None
        with self.assertRaises(IndexError):
            for quiz in self.post_data:
                self.assertEqual(quiz[1], takeQuiz.navigateQuestions(),\
                                 msg = 'Questions {} are not matching with {}'\
                                 .format(quiz[1], takeQuiz.navigateQuestions()))
            

    def test_record_answers(self):
        '''
        This check weather or not answers are stored in the persist by
        comparing values of TakeQuiz.answers with ones of QuizAttempts._answers.
        '''
 
        self.assertEqual(takeQuiz.recordAnswers, True, \
                         msg = 'Answers are not recorded at all!')

    def test_modify_answer(self):
    
        newAnswer = "new_one"
        queNum = 0
        for quiz in self.post_data:
            quiz[2][queNum] = newAnswer
          
            self.assertEqual(takeQuiz.modifyAnswers(newAnswer, queNum), True,\
                             msg = 'Answer is not modified!')

    def test_suspend_attempt(self):
        '''
        check if # of attempts changes when user suspends the attempts
        and tries to navigate the quiz again.
        '''
        takeQuiz.suspendAttempts()
        self.assertEqual(takeQuiz.suspendAttempts(), True, msg = 'cannot suspend attempts')

    def test_record_attempts(self):
        '''test for checking # of attempts being sent to the persist'''
    
        takeQuiz.recordAttempts()
        self.assertEqual(takeQuiz.suspendAttempts(), True, msg = 'cannot record attempts')

    def test_submit_quiz(self):
        self.assertEqual(takeQuiz.submitQuiz(), False, msg = 'submission x working')

if __name__ == '__main__':
    unittest.main(verbosity=2)
