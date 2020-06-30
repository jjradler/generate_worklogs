import json
import os
import sys

import main_menu
import profile_management
import utils
import worklog


def main(write_month=True, write_week_only=False):
    """
    .. function::main()
    .. desc::entry point for the worklog_generator utility.
    This function handles the high-level calls to the various
    interfaces, functions, data files, and object instances
    for this utility.

    :return:
    """
    users_file = "./resources/users.json"
    profiles_file = "./resources/profiles.json"
    runtime_tests_passed = True
    user_settings_dict= json.load(users_file)
    profiles_dict = json.load(profiles_file)

    # if username given in command line is not found in the key:value
    # pairs in the users_file dict(), then start up user manager module...

    wl = worklog.WorkLog
    # switch statement of some sort?



    if runtime_tests_passed:
        status_code = 0
    else:
        status_code = 1
    return status_code


if __name__ == "__main__":
    status = main()
    try:
        status = 0
    except RuntimeError("main() has failed at runtime...")
        sys.exit()