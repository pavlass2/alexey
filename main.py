import os
import json

from time import sleep
from datetime import datetime
from datetime import timedelta
from work_session import Work_session


# Functions
def clear():
    """Clears the console."""
    os.system('cls' if os.name=='nt' else 'clear')

def countdown(session):
    """Counts down from session length and show the remaining time."""
    clear()
    while session.get_time_left() > timedelta():        
        print(session.get_name() + ": " + str(session.get_time_left()))
        session.tick()
        sleep(1)
        clear()

def init(default_time="1:00"):
    """Initializes the session."""
    print("Work session initialization. Please fill in the following data.")

    # Fetch necessary data from the user.
    name = input("Session name:\n")
    problem = input("Problem - basic description of the problem you are trying to solve:\n")
    goal = input("Goal - how do you plan to contribute to the solution of this problem in this session?\n")
    time = input("Input the length of the time period in format \"HH:MM\" (default " + default_time + "):\n")
    # If user did not set any data, default.    
    if not time:
        time = default_time
    # Convert timestring to datetime.
    time = datetime.strptime(time, "%H:%M")
    # Convert datetime to timedelta.
    time = timedelta(hours=time.hour, minutes=time.minute)

    return Work_session(name, problem, goal, time)

def finish(session):
    """Closes the elapsed session."""
    goal_achieved = input("Did you achieved you projected goal?\n")
    problem_solved = input("Is the problem, you worked on, solved?\n")
    result_message = input("Any comment concerning result of this session?\n")
    
    session.close(goal_achieved, problem_solved, result_message)
        
def log_session(session):
    """Saves the closed session to .json file."""
    data = {session.get_name(): []}
    data[session.get_name()].append({
        "name" : session.get_name(),
        "problem" : session.get_problem(),
        "goal" : session.get_goal(),
        "session_length": str(session.get_session_length()),
        "timestamp" : str(session.get_timestamp()),
        "goal_achieved" : session.get_goal_achieved(),
        "problem_solved" : session.get_problem_solved(),
        "result_message" : session.get_result_message()
    })

    if os.name=='nt':
        separator = "\\"
    else:
        separator = "/"
    file_name = "data" + separator + str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".json"

    with open(file_name, 'w') as outfile:
        json.dump(data, outfile, indent=4)


# Program cycle.
print("Welcome to Alexey, the work session management and logging program.\nCreated by Pavel Skála.")
run = True
while run:
    # Prepare session.
    session = init()
    # Run session.
    countdown(session)
    print("Session has ended.")
    finish(session)
    # Save session to json.
    log_session(session)
    print("Session has been logged.")

    # Ask user if he or she wants to run another session and handle the answer.
    user_input_correct = False
    while not user_input_correct:
        user_input = input("Do you want to prepare another session? Press \"y\" for yes, \"n\" for no.\n")
        if user_input == "y" or user_input == "Y":
            print("Alexey would be so proud!")
            user_input_correct = True
        elif user_input == "n" or user_input == "N":
            user_input_correct = True
            run = False
        else:
            print("\"" + user_input + "\" is invalid input. Please try again.")
