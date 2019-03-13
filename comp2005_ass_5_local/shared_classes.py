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
        is_submitted (bool) - Indicates whether the quiz is submitted to be taken.
        assigned_students[str] - a list of student_IDs assigned to take quiz.
    '''    
    
    def __init__(self, instructor, quiz_name, attempts_allowed, course_ID):
        self._quiz_ID = None
        self._instructor = instructor
        self._quiz_name = quiz_name
        self._attempts_allowed = attempts_allowed
        self._course_ID = course_ID
        self._questions = []
        self._is_submitted = False
        self._assigned_students = []

    def add_assigned_student(self, studentID):
        '''Appends the provided student to assigned list.

        Args:
            studentID(str) - the student's unique ID
        '''
        if studentID not in self._assigned_students:
            self._assigned_students.append(studentID)

    def remove_assigned_student(self, index_to_remove):
        '''Removes assigned student at specified index.

        Args:
            index_to_remove(int) - the index of assigned students to remove.
        '''
        self._assigned_students.pop(index_to_remove)

    def get_all_assigned_students(self):
        '''Returns the list of all assigned students.

        Returns:
        [str] - list of student IDs of all assigned students.
        '''
        return self._assigned_students


    def get_submitted_status(self):
        '''returns the submission status of the quiz.

        Returns:
            bool - whether quiz is submitted or not.
        '''
        return self._is_submitted

    def set_submitted_status(self, new_status):
        '''sets a new submission status for the quiz.

        Args: new_status (bool) - the new submission status of quiz
        '''
        self._is_submitted = new_status
        
    def get_quiz_ID(self):
        '''returns quiz_ID.

        Returns:
            uuid - randomly generated quiz ID
        '''            
        return self._quiz_ID

    def set_quiz_ID(self, quiz_ID):
        '''sets quiz_ID.

        Args:
            quiz_ID (uuid) - randomly generated quiz ID
        '''        
        self._quiz_ID = quiz_ID

    def get_instructor(self):
        '''returns user object of author.

        Returns:
            user - user object for quiz author (instructor)
        '''    
        return self._instructor

    def set_instructor(self, new_instructor):
        '''sets new author for quiz.

        Args:
            new_instructor (user) - the new author for quiz.
        '''    
        self._instructor = new_instructor

    def get_quiz_name(self):
        '''returns the name of the quiz.

        Returns:
            str - name of quiz
        '''
        return self._quiz_name

    def set_quiz_name(self, new_quiz_name):
        '''sets new quiz name.

        Args:
            new_quiz_name(str): the new name of quiz
        '''    
        self._quiz_name = new_quiz_name   

    def get_num_attempts(self):
        '''returns number of quiz attempts allowed.

        Returns:
            int - attempts allowed per student.
        '''
        return self._attempts_allowed

    def set_num_attempts(self, new_num_attempts):
        '''sets a new number of max attempts per student.

        Args:
            new_num_attempts(int) - how many attempts.
        '''
        self._attempts_allowed = new_num_attempts

    def get_course_ID(self):
        '''returns the courseID corresponding to quiz.

        Returns:
            str - the course ID
        '''
        return self._course_ID

    def set_course_ID(self, new_course_ID):
        '''sets new courseID corresponding to quiz.

        Args:
            new_course_ID(str) - the new course ID
        '''
        self._course_ID = new_course_ID

    def get_questions(self):
        '''returns list of questions for quiz.

        Returns:
            [Question] - list of objects type Question
        '''
        return self._questions

    def add_question(self, question):
        '''appends Question object to list of objects.

        Args:
            question(Question) - question object to be added
        '''
        self._questions.append(question)

    def remove_question(self, index_to_remove):
        '''removes question object at specified index of question list.
        
        Args:
            index_to_remove(int) - the index of the question to be removed
        '''
        self._questions.pop(index_to_remove)

class Question:
    '''holds data for a question.

    Attributes:
        question(str) - The question that is being asked
        correct_answer(str) - all correct answers for question eg "ab"
        question_weight(int) - the worth of the question
        MC_options[str] - list of strings of possible answers to the question
    '''
    
    def __init__(self, question, correct_answer, question_weight):
        self._question = question
        self._correct_answer = correct_answer
        self._question_weight = question_weight
        self._MC_options = []

    def get_question(self):
        '''returns string of question being asked.

        Returns:
            str - the question being asked
        '''
        return self._question

    def set_question(self, new_question):
        '''sets the question being asked.

        Args:
            new_question(str) - the new question being asked
        '''
        self._question = new_question

    def get_correct_answer(self):
        '''returns correct answer(s) to question

        Returns:
            str - all correct answers
        '''
        return self._correct_answer

    def set_correct_answer(self, new_answer):
        '''sets new correct answer(s) to question 

        Note: for multiple correct answers, enter in a singular string
        eg "ab" if either a or b is correct.

        Args:
            new_answer(str) - all new correct answers to question
        '''
        self._correct_answer = new_answer

    def add_MC_option(self, MC_option):
        '''appends a new multiple choice option to list of options.

        Args:
            MC_option(str) - a choice for the answer to the question
        '''
        self._MC_options.append(MC_option)

    def get_MC_options(self):
        '''returns a list of all multiple choice options for a question.

        Returns:
            [str] - a list of strings that contain the options for an answer.
        '''
        return self._MC_options

    def remove_MC_option(self, index_to_remove):
        '''removes a MC option at specified index.

        Args:
            index_to_remove(int) - index of MC option to remove
        '''
        self._MC_options.pop(index_to_remove)

    def get_weight(self):
        '''returns the weight of a question

        Returns:
            int - the weight of the question
        '''
        return self._question_weight

    def set_weight(self, new_weight):
        '''sets a new question weight.

        Args:
            new_weight(int) - the new weight of question
        '''
        self._question_weight = new_weight

class QuizAttempt:
    '''Stores data of a student's attempt of a quiz.

    Attributes:
        student(User) - the user object for student attempting quiz
        start_time(datetime) - when the student began attempting the quiz
        end_time(datetime) - when the student submitted the quiz
        answers[str] - list of strings of student's choices for answers
        student_grade(float) - the student's grade on the quiz
    '''

    def __init__(self, student, start_time, end_time, answers, student_grade=None):
        self._student = student
        self._start_time = start_time
        self._end_time = end_time
        self._answers = answers
        self._student_grade = student_grade

    def get_student(self):
        '''returns User object of student writing quiz.

        Returns:
            User - the student writing the quiz
        '''
        return self._student

    def get_start_time(self):
        '''returns the time the student started the quiz.

        Returns:
            datetime - when the quiz was started
        '''
        return self._start_time

    def get_end_time(self):
        '''returns the time the student ended the quiz.

        Returns:
            datetime - when the quiz was started
        '''
        return self._end_time

    def get_answers(self):
        '''returns list of student's answers.

        Returns:
            [str] - list of strings of each answer
        '''
        return self._answers

    def get_grade(self):
        '''returns student's grade on quiz.

        Returns:
            float - student's grade
        '''
        return self._student_grade

    def set_grade(self, new_grade):
        '''sets new value for student's grade

        Args:
            new_grade(float) - the student's new grade 
        '''
        self._student_grade = new_grade

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
        self._user_ID = user_ID
        self._real_name = real_name
        self._password_hash = password_hash
        self._user_type = user_type
        self._quizIDs = []

    def get_user_ID(self):
        '''returns the user_ID of the user.

        Returns:
            str - user's ID
        '''
        return self._user_ID

    def get_real_name(self):
        '''returns user's real name.

        Returns:
            str - user's full name.
        '''
        return self._real_name

    def set_real_name(self, new_name):
        '''updates user's real name

        Args: 
            new_name(str) - user's new name
        '''
        self._real_name = new_name

    def get_password_hash(self, new_name):
        '''return's user's password hash
        
        Returns:
            hash - encryption of user's password
        '''
        return self._password_hash

    def get_user_type(self):
        '''return's user's type, s or i

        Returns:
            str - user's type s or i
        '''
        return self._user_type
    
    def set_user_type(self, new_type):
        '''updates user's type, s or i

        Args:
            new_type(str) - s for student, i for instructor

        Raises:
            KeyError - if other input is entered
        '''
        if new_type != ("s" or "i"):
            raise KeyError("invalid type entered. enter s for student or i for instructor ")
        self._user_type = new_type

    def get_quiz_IDs(self):
        '''returns list of quizIDs taken/written by user

        Returns:
            [uuid] - list of unique quiz IDs
        '''
        return self._quizIDs

    def add_quiz_ID(self, quiz_ID):
        '''appends new quizID to list.

        Args:
            quiz_ID(uuid) - unique quiz ID

        
        '''
        if quiz_ID not in self._quizIDs:  
            self._quizIDs.append(quiz_ID)

    def remove_quiz_ID(self, index_to_remove):
        '''removes quizID from specified index from user's ID list.

        Args:
            index_to_remove(int) - the index of the quizID to remove
        '''   
        self._quizIDs.pop(index_to_remove)