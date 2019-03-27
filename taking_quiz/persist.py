import shelve
import datetime
from exceptions import *
import uuid
from shared_classes import *

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
        Persist.quiz_shelve - the shelve dictionary opened upon each init
    '''
    quiz_shelve = None

    def __init__(self, filename = "quiz_software_persist"):
        if not Persist.quiz_shelve:  
            Persist.quiz_shelve = shelve.open(filename, writeback=True)

    def close(self):
        '''logs active user out, and closes shelve'''
        Persist.quiz_shelve.sync()
        Persist.quiz_shelve.close()
        Persist.quiz_shelve = None
    def sync(self):
        '''syncs shelve.'''
        Persist.quiz_shelve.sync()
    

    def add_user(self, user):
        '''adds new user to persistence.

        Args:
            user(User) - the user to be added
        
        Raises:
            DuplicateError - if user is already in system
            ValueError - If a parameter type is incorrenct
        '''
        if not isinstance(user, User):
            raise ValueError("user parameter must be of type User")

        if not "users" in Persist.quiz_shelve: 
            Persist.quiz_shelve["users"] = {}

        quiz_users = Persist.quiz_shelve["users"]
        if user.user_ID in quiz_users:
            raise DuplicateError("User already in system.")
        else:
            quiz_users[user.user_ID] = user

    def get_user(self, user_ID):
        '''uses user_ID to return User object with that ID.

        Args:
            user_ID(str) - the user's ID you want to get

        Returns:
            User - the user you want

        Raises:
            EmptyError - if the user is not in the database
            KeyError - if no user is stored in database
        '''
        quiz_users = Persist.quiz_shelve["users"]
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

        Raises:
            KeyError - if no users are stored
            
        '''
        quiz_users = Persist.quiz_shelve["users"]
        user_list = []
        if not type:
            for user in quiz_users.values():
                user_list.append(user)

        else:
            for user in quiz_users.values():
                if user.user_type == type:
                    user_list.append(user)
        return user_list

    def add_quiz(self, quiz):
        '''adds a quiz to persistence and generates a unique ID for it.

        Args:
            quiz(Quiz) - the quiz to be added.

        Raises:
            ValueError - if quiz is not type Quiz
        '''
        if not isinstance(quiz , Quiz):
            raise ValueError("parameter quiz should be of type Quiz")
       
        if not "quizzes" in Persist.quiz_shelve: 
            Persist.quiz_shelve["quizzes"] = {}
            
        quizzes = Persist.quiz_shelve["quizzes"]
        quiz_ID = uuid.uuid4()
        author = quiz.instructor
        author.quizIDs.append(quiz_ID)
        quiz.quiz_ID = quiz_ID
        quizzes[quiz_ID] = quiz

    def add_quiz_attempt(self, quiz_ID, student, quiz_attempt):
        '''adds a quiz attempt to persistence.

        Args:
            quiz_ID(uuid) - the randomly generated ID of the quiz
            student(User) - the User object of student submitting attempt
            quiz_attempt(QuizAttempt) - the object storing data about attempt

        Raises:
            ValueError - if the type of a parameter is incorrect
        '''
        if not isinstance(quiz_ID, uuid.UUID):
            raise ValueError("quiz_ID should be of type uuid")

        if not isinstance(student, User):
            raise ValueError("student should be of type user")

        if not isinstance(quiz_attempt, QuizAttempt):
            raise ValueError("quiz_attempt should be of type QuizAttempt")
        
        if not "quiz_attempts" in Persist.quiz_shelve:
            Persist.quiz_shelve["quiz_attempts"] = {}

        all_quizzes =  Persist.quiz_shelve["quiz_attempts"]
        student_ID = student.user_ID
        student.quizIDs.append(quiz_ID)
        if not quiz_ID in all_quizzes:
            all_quizzes[quiz_ID] = {}
        quiz_attempts = all_quizzes[quiz_ID]
        if not student_ID in quiz_attempts:
            quiz_attempts[student_ID] = []
        quiz_attempts[student_ID].append(quiz_attempt)

    def get_all_attempts_for_quiz(self, quizID):
        '''returns a list of all QuizAttempts for a given quiz.

        Args:
            quizID(uuid) - the randomly generated ID for the quiz.

        Returns:
            [QuizAttempt] - list of all quiz attempts for the specified quiz.

        Raises:
            KeyError - if no quiz attempts have been recorded
            ValueError - if the type of a parameter is incorrect
        '''
        if not isinstance(quizID, uuid.UUID):
            raise ValueError("Incorrect parameter type")
        
        all_quizzes = Persist.quiz_shelve["quiz_attempts"]
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

        Raises:
            KeyError - If no attempts are stored for the given student.
            ValueError - If a parameter type is incorrect
        '''
        if not isinstance(quizID, uuid.UUID):
            raise ValueError("Incorrect parameter type for QuizID entered")

        if not isinstance(studentID, str):
            raise ValueError("Incorrect parameter type for studentID entered")

        all_quizzes = Persist.quiz_shelve["quiz_attempts"]
        quiz_attempts =  all_quizzes[quizID]
        return quiz_attempts[studentID]

    def get_stu_participation(self, quizID):
        '''returns the number of students who submitted a QuizAttempt

        Args:
            quizID(uuid) - the unique ID of quiz

        Returns:
            int - the number of students who submitted an attempt.

        Raises:
            KeyError - if no quiz attempts have been added.
            ValueError - if parameter type is incorrect.
        '''
        if not isinstance(quizID, uuid.UUID):
            raise ValueError("Incorrect parameter type entered.")
        all_quizzes = Persist.quiz_shelve["quiz_attempts"]
        quiz_attempts =  all_quizzes[quizID]
        return len(quiz_attempts)

    def remove_user(self, userID):
        '''removes user with specified ID from persistence.

        Args:
            userID(str) - the ID of user to be removed

        Raises:
            EmptyError - if the user is not registered in persistence
            ValueError - if incorrect parameter type is entered
            KeyError - if no users are stored in the persistence

        '''
        if not isinstance(userID, str):
            raise ValueError("Incorrect parameter type entered.")
        quiz_users = Persist.quiz_shelve["users"]
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
            ValueError - if incorrect parameter type is entered
            KeyError - if no quizzes are stored
        '''
        if not isinstance(quizID, uuid.UUID):
            raise ValueError("Incorrect parameter type entered.")
        quizzes = Persist.quiz_shelve["quizzes"]
        if not quizID in quizzes:
            raise EmptyError("This quiz is not in the system.")
        else:
            quizzes.pop(quizID)

    def add_to_quiz_bank(self, question):
        '''Adds a question to the quiz bank.

        Args:
            question(Question) - the question object to be added to quiz bank
        '''
        if not "quiz_bank" in Persist.quiz_shelve: 
            Persist.quiz_shelve["quiz_bank"] = []
        quiz_bank = Persist.quiz_shelve["quiz_bank"]
        quiz_bank.append(question)

        
    def remove_from_quiz_bank(self, index_to_remove):
        '''removes a question from quiz bank at given index.

        Args:
            index_to_remove(int) -  the index of quiz bank to remove

        Raises:
            KeyError - if no questions have been added to quiz bank
            IndexError - if the index is out of bounds of quiz_bank list
        '''
        quiz_bank = Persist.quiz_shelve["quiz_bank"]
        quiz_bank.pop(index_to_remove)

    def get_last_question_ID(self):
        '''returns the question ID of the last question stored in the quiz bank

        Returns:
            int - the ID of the last question stored in the quiz bank.
        '''
        if not "quiz_bank" in Persist.quiz_shelve:
            return 0
        quiz_bank = Persist.quiz_shelve["quiz_bank"]
        question_IDs = []
        for question in quiz_bank:
            question_IDs.append(question.question_ID)
        last_key = max(question_IDs, key=int)
        return last_key


    def get_quiz_bank_question(self, question_ID = None):
        '''returns a question with specific question_ID, if ID
        is not specified then all questions in quiz bank are returned 
        in a list.

        Args:
            question_ID(int) - the ID of the question to be returned
            
        Returns:
            Question - if a question_ID is specified
            [Question] - list of all questions if no ID is specified
        
        Raises:
            IndexError - if no question has given ID
            ValueError - if incorrect parameter type
        '''
        if not (isinstance(question_ID, int) or not question_ID):
            raise ValueError("Incorrect parameter type")
        
        quiz_bank = Persist.quiz_shelve["quiz_bank"]
        if not question_ID:
            return quiz_bank
        else:
            for question in quiz_bank:
                if question.question_ID == question_ID:
                    return question
        raise IndexError("No question has the given ID.")
        
    def get_quiz(self, quiz_ID = None):
        '''Returns the specified quiz from persist. If no
        ID is specified returns a list of all quizzes stored.

        Args:
            quiz_ID(uuid) - the unique ID of the quiz

        Returns:
            Quiz - the specified quiz if ID is entered
            [Quiz] - a list of all quizzes if no ID is entered

        Raises:
            EmptyError - if no quizzes are stored
            KeyError - if the ID entered is not valid
        '''
        if not "quizzes" in Persist.quiz_shelve:
            raise EmptyError("There are no quizzes stored.")
        quizzes = Persist.quiz_shelve["quizzes"]
        if not quiz_ID:
            allQuizzes = []
            for quiz in quizzes.values():
                allQuizzes.append(quiz)
            return allQuizzes
        else:
            return quizzes[quiz_ID]

    def get_assigned_quizzes(self, student_ID):
        '''returns a list of quizzes assigned to specified student.
        Args:
            student_ID(str) - the unique ID of the student 
        Returns:
            [Quiz] - the list of quizzes assigned to the student
        Raises:
            KeyError - if no quizzes have been added
            EmptyError - if there are no quizzes assigned to student
    '''  
        assignedQuizzes = []
        allQuizzes = self.get_quiz()
        for quiz in allQuizzes:
            if student_ID in quiz.assigned_students:
                assignedQuizzes.append(quiz)
        if assignedQuizzes == []:
            raise EmptyError("The student is not assigned to any quizzes.")


    def _clear(self):
        '''This method removes all data from persistence.'''
        Persist.quiz_shelve.clear()


    