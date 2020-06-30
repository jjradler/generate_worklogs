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
    runtime_tests_passed = True

    wl = worklog.WorkLog

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