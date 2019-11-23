from data.pipelines.new_data import *
import sys

TEST_FILE_PATH = "./test_data/cron.log"
TEST_SUBJECT = "CO"
TEST_NUMBER = 250
DEFAULT_ENCODING = "utf-8"

def trigger_endpoint():
    return get_endpoint(generate_endpoint(WINTER_2020, TEST_SUBJECT, TEST_NUMBER))

def write_test_result(data, local_file_path, formatted=True):
    f = open(local_file_path, "w")
    f.write(data)
    f.close()

def run_test():
    write_test_result(str(parse_response(trigger_endpoint())), TEST_FILE_PATH)

def main(argv):
    run_test()

if __name__ == "__main__":
    main(sys.argv)
