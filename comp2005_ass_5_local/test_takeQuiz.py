#!/usr/bin/env python3

# revised Fe 1 2019 so tests are consistent with shelve files on windows and fix
# intermittent bug in posttime test

import unittest
import tempfile
import os.path
import stat
import datetime
import persist
from time import sleep
from takeQuiz import TakeQuiz

class TestTakeQuiz(unittest.TestCase):

    post_data = [  
                        ("quiz1", ["ques1", "ques2", "ques3"], ["answer1", "answer2"], True),
                        ("quiz2", ["ques_a", "ques_b", "ques_c"], ["All remind us"], False),
                        ("quiz3", ["ques_y", "ques_w", "ques_z"], ["Our live sublime"], True),
                        ("quiz4", ["ques_Z", "ques_X", "ques_C"], ["Leave behind us"], False),
                        ("quiz5", ["ques11", "ques22", "ques33"], ["In the sands of time"], True),
                ]

    def test_check_access(self):
        tq = TakeQuiz()
        self.assertEqual(True, tq.checkAccess(), msg = 'Check process failed')

    def test_navigate_questions(self):
        tq = TakeQuiz()
        for quiz in self.post_data:
            tq.questions = quiz[1]
            self.assertEqual(quiz[1], tq.navigateQuestions(), \
                             msg = 'Questions {} are not matching with {}'.format(quiz[1], tq.navigateQuestions()))

    def test_record_answers(self):
        tq = TakeQuiz()
        '''
        This check weather or not answers are stored in the persist by
        comparing values of TakeQuiz.answers with ones of QuizAttempts._answers.
        '''
        tq.recordAnswers()
        self.assertEqual(tq.answers, persist.Persist().\
                         get_attempts_by_student('None','None'),\
                         msg = 'Answers are not recorded at all!')

    def test_modify_answer(self):
        tq = TakeQuiz()
        newAnswer = "new_one"
        queNum = 0
        for quiz in self.post_data:
            quiz[2][queNum] = newAnswer
            tq.modifyAnswers(queNum)
            self.assertEqual(quiz[2][queNum], tq.answers[queNum], msg = 'Answer is not modified!')

    def test_suspend_attempt(self):
        '''
        check if # of attempts changes when user suspends the attempts
        and tries to navigate the quiz again.
        '''

    def test_record_attempts(self):
        '''test for checking # of attempts being sent to the persist'''

if __name__ == '__main__':
    unittest.main(verbosity=2)
