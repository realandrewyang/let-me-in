from urllib import request, parse
import json
import re
import pandas as pd
import sys

# API
UW_API_URL = "http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl/?"

# Term enums
WINTER_2020 = 1201

# Regex for response parsing
INVALID_MATCH = "((query had no matches)|(Please return to))"

# Number Columns in response
NUMBER_COLS = {"Enrl Cap", "Enrl Tot", "Wait Cap", "Wait Tot"}

# Takes in an API endpoint as a string and calls the UW Course API
# at that endpoint, returning a response as a JSON object
# Parameters:
# endpoint - str
# Output:
# JSON object
def get_endpoint(endpoint):
    return request.urlopen(endpoint).read().decode("utf-8")

# Takes in representing API parameters and generates
# the corresponding endpoint as a string
# Parameters:
# term - enum
# subject - str
# number - int
# Output:
# str
def generate_endpoint(term, subject, number):
    return UW_API_URL + "level=under" + "&sess=" + str(term) + "&subject=" + subject + "&cournum=" + str(number)

# Takes a pandas dataframe and converts numbers to ints
# Parameters:
# data - pandas dataframe
# Output:
# pandas dataframe
def clean_int(data):
    for field in NUMBER_COLS:
        data[field] = pd.to_numeric(data[field], errors="coerce")
    return data

# Takes the raw HTML Response from the UW Course API endpoint
# and returns None or a pandas dataframe representing the query result
# Parameters:
# raw_json - str
# Output:
# None or pandas dataframe
def parse_response(raw_html):

    # Invalid query
    if re.findall(INVALID_MATCH, raw_html) != []: return None

    return clean_int(pd.read_html(raw_html)[1])
