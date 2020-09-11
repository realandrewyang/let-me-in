from data.pipelines.notify import *
from auth.key import *
from auth.contact import PHONE_NUMBER
import sys

TEST_MESSAGE = "CS 341: 2 spots open!"
VALID_RESULT = {"SendMessageWithReferenceResult": "Message queued successfully"}

def run_test():
    return send_notification(
                generate_noti_endpoint(
                    SWIFT_GATEWAY_KEY,
                    PHONE_NUMBER,
                ),
                TEST_MESSAGE
            )

def main(argv):
    assert run_test() == VALID_RESULT

if __name__ == "__main__":
    main(sys.argv)
