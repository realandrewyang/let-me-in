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
TEST_STATUS_FILE_PATH = "./test_data/state.txt"
VALID_RESULT = {"SendMessageWithReferenceResult": "Message queued successfully"}

# Reads state from file and returns as an integer
def check_prev_status(local_file_path):
    temp = -1
    f = open(local_file_path, "r")
    f.read(temp)
    f.close()
    return int(temp)

# Update status to file
def write_status(local_file_path, status):
    f = open(local_file_path, "w")
    f.write(str(status))
    f.close()

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

    # Don't send notification if status hasn't changed
    if status[0] == check_prev_status(TEST_STATUS_FILE_PATH): return

    # Update state
    write_status(TEST_STATUS_FILE_PATH, status[0])
    
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
    run_test()

if __name__ == "__main__":
    main(sys.argv)
