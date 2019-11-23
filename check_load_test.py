from auth.key import *
from auth.contact import *
from data.pipelines.new_data import *
from data.pipelines.notify import *
from core.check_load import *
import sys

TEST_COURSE_ID = 7667
TEST_COURSE_NAME = "CO 250"
TEST_SUBJECT = "CO"
TEST_NUMBER = 250
TEST_STATE = OPEN
VALID_RESULT = {"SendMessageWithReferenceResult": "Message queued successfully"}

def run_test():

    # Get state
    status = check_course(
        parse_response(
            get_endpoint(
                generate_endpoint(
                    WINTER_2020,
                    TEST_SUBJECT,
                    TEST_NUMBER
                )
            )
        ),
        TEST_COURSE_ID
    )
    
    # Check whether to send or not
    if status[0] == TEST_STATE:
        return send_notification(
            generate_noti_endpoint(
                SWIFT_GATEWAY_KEY,
                PHONE_NUMBER
            ),
            create_message(
                status,
                TEST_COURSE_NAME
            )
        )
    return None

def main(argv):
    assert run_test() == VALID_RESULT

if __name__ == "__main__":
    main(sys.argv)
