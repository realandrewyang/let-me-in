import sys
import pandas as pd

COURSE_LOG_FILE = "../course_data/courses.csv"
COURSE_SCHEMA = ["Term", "Course ID", "Subject", "Number"]


# Takes in a file path and schema and produces a pandas dataframe object
# from the data in that file
# Parameters:
# local_file_path: str
# schema: List[str]
# Output:
# pandas dataframe
def read_courses(local_file_path, schema = COURSE_SCHEMA):
    return pd.read_csv(local_file_path, names = schema)

# Takes in a row of a pandas dataframe and checks if the course still exists
# Parameters:
# course_info: pandas dataframe row
# Output:
# boolean
def valid_course(course_info):
    return False

# Takes in a pandas dataframe, key and value and removes the row(s)
# matching that pair
# Parameters:
# data: pandas dataframe
# key: str
# value: str
# Output:
# pandas dataframe
def remove_course(data, key, value):
    try:
        data.drop(data.index[data[key] == value], inplace = True)
    return data


