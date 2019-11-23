from urllib import request, parse
import json

SWIFT_GATEWAY_URL = "http://smsgateway.ca/services/message.svc/"

# Adds Content-Type JSON to a request
# Parameters:
# req - Request
# headers - dict
# Output:
# Request
def prep_request(req, headers):
    for key in headers:
        req.add_header(key, headers[key])
    return req

# Takes in an API endpoint and message as strings and sends a request
# to the Swift Gateway API, returning a queue status as a JSON object
# Parameters:
# endpoint - str
# message - str
# Output:
# JSON object
def send_notification(endpoint, message):
    return request.urlopen(
        prep_request(
            request.Request(
                url=endpoint
            ),
            {
                "Content-Type": "application/json"
            }
        ),
        data=json.dumps({
            "MessageBody": message
        }).encode()
    ).read().decode("utf-8")

# Takes in an API key and phone number and generates the Swift Gateway API
# endpoint to send an SMS message to the phone number
# Parameters:
# api_key - str
# phone_number - str
# Output:
# str
def generate_noti_endpoint(api_key, phone_number):
    return SWIFT_GATEWAY_URL + api_key + "/" + phone_number
