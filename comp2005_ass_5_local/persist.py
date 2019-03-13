import shelve
import datetime
from exceptions import *
import uuid
from shared_classes import User
from shared_classes import Quiz
'''Provides the persistence to all of the other modules of the software.

Classes:
    Persist - The class that stores and fetches data 

Note: The style used for Args in the docstrings are as follows,
argument_name(Argument_Type). In the case that the value is a list
or dictionary it will be presented in the appropriate brackets.
eg. students[User] - would be a list of objects that are type User.
'''


class Persist:
    '''Persistence method for quiz software. utilizes shelve.

    Attributes:
        quiz_shelve - the shelve dictionary opened upon each init
    '''

    def __init__(self, filename = "quiz_software_persist"):
        self.quiz_shelve = shelve.open(filename, writeback=True)

    def close(self):
        '''logs active user out, and closes shelve'''
        self.quiz_shelve.sync()
        self.quiz_shelve.close()

    def sync(self):
        '''syncs shelve.'''
        self.quiz_shelve.sync()
    

    def add_user(self, user):
        '''adds new user to persistence.

        Args:
            user(User) - the user to be added
        
        Raises:
            DuplicateError - if user is already in system
        '''
        if not "users" in self.quiz_shelve: 
            self.quiz_shelve["users"] = {}

        quiz_users = self.quiz_shelve["users"]
        if user.get_user_ID() in quiz_users:
            raise DuplicateError("User already in system.")
        else:
            quiz_users[user.get_user_ID()] = user

    def get_user(self, user_ID):
        '''uses user_ID to return User object with that ID.

        Args:
            user_ID(str) - the user's ID you want to get

        Returns:
            User - the user you want

        Raises:
            EmptyError - if the user is not in the database
        '''
        quiz_users = self.quiz_shelve["users"]
        if not user_ID in quiz_users:
            raise EmptyError("This user is not registered.")
        else:
            return quiz_users[user_ID]

    def get_users_by_type(self, type=None):
        '''returns all students if input is s, all instructors for i,
        or all users for no input.

        Args:
            type(str/None) - s for students. i for instructors, no input for both

        Returns:
            [User] - list of all students or instructors or all
        '''
        quiz_users = self.quiz_shelve["users"]
        user_list = []
        if not type:
            for user in quiz_users.values():
                user_list.append(user)

        else:
            for user in quiz_users.values():
                if user.get_user_type() == type:
                    user_list.append(user)
        return user_list

    def add_quiz(self, quiz):
        '''adds a quiz to persistence and generates a unique ID for it.

        Args:
            quiz(Quiz) - the quiz to be added.
        '''
        if not "quizzes" in self.quiz_shelve: 
            self.quiz_shelve["quizzes"] = {}
            
        quizzes = self.quiz_shelve["quizzes"]
        quiz_ID = uuid.uuid4()
        author = quiz.get_instructor()
        author.add_quiz_ID(quiz_ID)
        quizzes[quiz_ID] = quiz

    def add_quiz_attempt(self, quiz_ID, student, quiz_attempt):
        '''adds a quiz attempt to persistence.

        Args:
            quiz_ID(uuid) - the randomly generated ID of the quiz
            student(User) - the User object of student submitting attempt
            quiz_attempt(QuizAttempt) - the object storing data about attempt
        '''
        if not "quiz_attempts" in self.quiz_shelve:
            self.quiz_shelve["quiz_attempts"] = {}

        all_quizzes =  self.quiz_shelve["quiz_attempts"]
        student_name = student.get_user_ID()
        student.add_quiz_ID(quiz_ID)
        if not quiz_ID in all_quizzes:
            all_quizzes[quiz_ID] = {}
        quiz_attempts = all_quizzes[quiz_ID]
        if not student_name in quiz_attempts:
            quiz_attempts[student_name] = []
        quiz_attempts[student_name].append(quiz_attempt)

    def get_all_attempts_for_quiz(self, quizID):
        '''returns a list of all QuizAttempts for a given quiz.

        Args:
            quizID(uuid) - the randomly generated ID for the quiz.

        Returns:
            [QuizAttempt] - list of all quiz attempts for the specified quiz.
        '''
        all_quizzes = self.quiz_shelve["quiz_attempts"]
        quiz_attempts =  all_quizzes[quizID]
        attemptList = []
        for stu in quiz_attempts.values():
            for attempt in stu:
                attemptList.append(attempt)

        return attemptList

    def get_attempts_by_student(self, quizID, studentID):
        '''returns a list of all quiz attempts by a student on given quiz.

        Args:
            quizID(uuid) - the randomly generated ID for quiz.
            studentID(str) - the unique ID for the student.

        Returns:
            [QuizAttempt] - a list of quiz attempts by student for specified quiz.
        '''
        all_quizzes = self.quiz_shelve["quiz_attempts"]
        quiz_attempts =  all_quizzes[quizID]
        return quiz_attempts[studentID]

    def get_stu_participation(self, quizID):
        '''returns the number of students who submitted a QuizAttempt

        Args:
            quizID(uuid) - the unique ID of quiz

        Returns:
            int - the number of students who submitted an attempt.
        '''
        all_quizzes = self.quiz_shelve["quiz_attempts"]
        quiz_attempts =  all_quizzes[quizID]
        return len(quiz_attempts)

    def get_quiz(self, quiz_ID):
        '''returns the quiz with specified ID.

        Args: 
            quiz_ID(uuid) - the unique ID of the quiz

        Raises:
            EmptyError - if no quizzes are stored
        '''
        if not "quizzes" in self.quiz_shelve:
            raise EmptyError("There are no quizzes stored.")

        else:
            quizzes = self.quiz_shelve["quizzes"]
            return quizzes[quiz_ID]

    def remove_user(self, userID):
        '''removes user with specified ID from persistence.

        Args:
            userID(str) - the ID of user to be removed

        Raises:
            EmptyError - if the user is not registered in persistence
        '''
        quiz_users = self.quiz_shelve["users"]
        if not userID in quiz_users:
            raise EmptyError("This user is not registered.")
        else:
            quiz_users.pop(userID)

    def remove_quiz(self, quizID):
        '''removes quiz with given ID from persistence.

        Args:
            quizID(uuid) - unique ID of quiz to be removed

        Raises:
            EmptyError - if the quiz is not in persistence
        '''
        quizzes = self.quiz_shelve["quizzes"]
        if not quizID in quizzes:
            raise EmptyError("This quiz is not in the system.")
        else:
            quizzes.pop(quizID)

    def add_to_quiz_bank(self, question):
        '''Adds a question to the quiz bank.

        Args:
            question(Question) - the question object to be added to quiz bank
        '''
        if not "quiz_bank" in self.quiz_shelve: 
            self.quiz_shelve["quiz_bank"] = []
        quiz_bank = self.quiz_shelve["quiz_bank"]
        quiz_bank.append(question)

    def get_quiz_bank(self):
        '''returns the list of questions stored in quiz bank.

        Returns:
            [Question] - the list of questions stored in bank
        
        Raises:
            KeyError - If there have been no questions stored.
        '''
        return self.quiz_shelve["quiz_bank"]
        
    def remove_from_quiz_bank(self, index_to_remove):
        '''removes a question from quiz bank at given index.

        Args:
            index_to_remove(int) -  the index of quiz bank to remove

        Raises:
            KeyError - if no questions have been added to quiz bank
            IndexError - if the index is out of bounds of quiz_bank list
        '''
        quiz_bank = self.quiz_shelve["quiz_bank"]
        quiz_bank.pop(index_to_remove)
        