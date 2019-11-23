import pandas as pd
import numpy as np

# States of a course
NOT_FOUND = -1
OPEN = 0
FILLED = 1
OVERFILLED = 2

# Checks a course capacity given a course id
# and returns the state and the number of free spots
# Parameters:
# course - pandas dataframe row
# course_id - str
# Output:
# List[enum, int]
def check_course_core(course, course_id):
    return [OPEN if (course["Enrl Tot"] < course["Enrl Cap"]).bool()
                    else OVERFILLED if (course["Enrl Tot"] > course["Enrl Cap"]).bool()
                    else FILLED,
            int(course["Enrl Cap"] - course["Enrl Tot"])]

# Checks a course capacity given a course id
# and returns the state and the number of free spots
# Parameters:
# d - pandas dataframe
# course_id - str
# Output:
# List[enum, int]
def check_course(d, course_id):
    try:
        return check_course_core(d.loc[d["Class"] == np.int64(course_id)], np.int64(course_id))
    except KeyError:
        return [NOT_FOUND, 0]

# Produces a message given a course result and name
# Parameters:
# result - List[enum, int]
# course_name = str
# Output:
# str
def create_message(result, course_name):
    return course_name + ": " + ("not found" if result[0] == NOT_FOUND else "filled" if result[0] == FILLED else str(result[1] * -1) + " spot(s) overfilled" if result[0] == OVERFILLED else str(result[1]) + " spot(s) open")
