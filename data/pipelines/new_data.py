from urllib import request, parse
import json
import sys

API_URL = "http://www.adm.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl/?"

# Term enums
WINTER_2020 = 1201

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
    return API_URL + "level=under" + "&sess=" + str(term) + "&subject=" + subject + "&cournum=" + str(number)

# Takes the raw JSON response from the UW Course API endpoint
# and returns None or a JSON structure representing the query result
# Parameters:
# raw_json - JSON object
# Output:
# None
# set of dictionaries
def parse_response(raw_json):
    return None

