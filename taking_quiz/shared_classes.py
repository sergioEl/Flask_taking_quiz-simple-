'''Common classes that are shared by all modules of the software
but are not directly related to the persist module.

Classes:
    Quiz - object that holds data for taking a quiz.
    QuizAttempt - object that holds data for a students
    attempt of a specified quiz.
    Question - object that holds data for a question to be asked
    in a quiz.

Note: The style used for Args in the docstrings are as follows,
argument_name(Argument_Type). In the case that the value is a list
or dictionary it will be presented in the appropriate brackets.
eg. students[User] - would be a list of objects that are type User.
'''


class Quiz:
    '''Holds data for a quiz.
    
    Attributes:
        quiz_ID (uuid) - randomly generated ID used to reference and fetch quiz.
        instructor (User) - the author of the quiz.
        quiz_name (str) - the name of the quiz.
        attempts_allowed (int) - number of attempts allowed per student.
        course_ID (str) - the course ID for quiz.
        questions [Question] - list of question objects.
        assigned_students[str] - a list of student_IDs assigned to take quiz.
        start_time(datetime) - the time the quiz becomes available
        end_time(datetime) - the time the quiz is no longer available
    '''    
    
    def __init__(self, instructor, quiz_name, attempts_allowed, start_time, end_time):
        self.quiz_ID = None
        self.instructor = instructor
        self.quiz_name = quiz_name
        self.attempts_allowed = attempts_allowed
        self.questions = []
        self.assigned_students = []
        self.start_time = start_time
        self.end_time = end_time
    
class Question:
    '''holds data for a question.

    Attributes:
        question(str) - The question that is being asked
        correct_answer(str) - all correct answers for question eg "ab"
        question_weight(int) - the worth of the question
        MC_options[str] - list of strings of possible answers to the question
        question_ID(int) - unique ID for the question  
    '''
    
    def __init__(self, question, correct_answer, question_weight, question_ID):
        self.question_ID = question_ID
        self.question = question
        self.correct_answer = correct_answer
        self.question_weight = question_weight
        self.MC_options = []

    
class QuizAttempt:
    '''Stores data of a student's attempt of a quiz.

    Attributes:
        student(User) - the user object for student attempting quiz
        start_time(datetime) - when the student began attempting the quiz
        end_time(datetime) - when the student submitted the quiz
        answers[str] - list of strings of student's choices for answers
        student_grade(float) - the student's grade on the quiz
        is_submitted(bool) - whether the attempt has been submitted
    '''

    def __init__(self, student, start_time, end_time, answers, is_submitted, student_grade=None):
        
        self.student = student
        self.start_time = start_time
        self.end_time = end_time
        self.answers = answers
        self.student_grade = student_grade
        self.is_submitted = is_submitted
   
    
class User:
    '''Stores student or instructor user information.

    Attributes:
        user_ID(str) - unique ID user will use to log in
        real_name(str) - the user's real name
        password_hash(hash) - hash of user's password for verification
        user_type(str) - s for student, i for instructor
        quizIDs[uuid] - for student, list of quizIDs of quizzes taken, 
            for instructors, list of quizIDs of quizzes written
    '''

    def __init__(self, user_ID, real_name, password_hash, user_type):
        self.user_ID = user_ID
        self.real_name = real_name
        self.password_hash = password_hash
        self.user_type = user_type
        self.quizIDs = []

   