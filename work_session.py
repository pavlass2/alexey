from datetime import timedelta
from datetime import datetime

class Work_session:

    def __init__(self, name, problem, goal, session_length):
        """Initializes the session.
        name = The name of the session.
        problem = The problem that you are going to work on during this session.
        goal = The goal you are hoping to achieve during this session.
        session_length = The timedelta representing the total length of the session.
        """
        # Pre-session properties.
        self.__name = name
        self.__problem = problem
        self.__goal = goal
        self.__session_length = session_length
        self.__time_left = session_length
        self.__timestamp = datetime.now()
        
        # After-session properties.
        self.__goal_achieved = ""
        self.__problem_solved = ""
        self.__result_message = ""

    def close(self, goal_achieved, problem_solved, result_message):
        """Closes the session after it has elapsed."""
        if self.__time_left != timedelta():
            raise ValueError("__time_left must be 0. __time_left: " + str(self.__time_left))
        self.__goal_achieved = goal_achieved
        self.__problem_solved = problem_solved
        self.__result_message = result_message

    def tick(self):
        """Lowers the time_left by 1 second."""
        self.__time_left -= timedelta(seconds=1)
    
    def get_name(self):
        return self.__name

    def get_problem(self):
        return self.__problem

    def get_goal(self):
        return self.__goal

    def get_session_length(self):
        return self.__session_length

    def get_time_left(self):
        return self.__time_left

    def get_timestamp(self):
        return self.__timestamp

    def get_goal_achieved(self):
        return self.__goal_achieved

    def get_problem_solved(self):
        return self.__problem_solved

    def get_result_message(self):
        return self.__result_message
