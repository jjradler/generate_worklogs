#!/bin/env python3
import datetime
import sys


class WorkLog:
    """
    .. class:: WorkLog
    .. desc:: Generic base class for WorkLog documents
    """
    acceptable_formats = ["md", "txt", "rst", "html"]

    def __init__(self, username=None, input_path=None, output_format="md"):
        # TODO: Consider making this into a helper method...self._validate_output_format()
        try:
            output_format in self.acceptable_formats
        except ValueError(f"Output format must be a member of {self.acceptable_formats}"):
            retry = True
            new_format = input("Enter an acceptable format or -1 to quit:")
            while retry:
                if new_format in self.acceptable_formats:
                    self._set_template_format(new_format)
                    retry = False
                elif new_format == -1:
                    print("Quitting...")
                    sys.exit()
                else:
                    print("This is still not an acceptable format... Please try again later!")
                    sys.exit()
        else:
            self._output_format = output_format  # can be md, rst, txt, or html

        self._username = username
        # self._validate_username()
        self._last_week_path = input_path
        # self._validate_last_week_path().

        self._date_format = "dd/mm/yy"
        self._time_format = "%H:%M:%S"

        self._monday_dates = list()
        self._output_file_path = None

        # Containers declared for holding the component strings of a generated Work Log. These are populated with calls.
        self._header_string = None
        self._to_do_string = None
        self._blank_weeks_string = None
        self._notes_string = None
        self._footer_string = None

    @property
    def _profile(self):
        profile_dict = dict()
        return profile_dict

    @property
    def _today_date(self):
        today_date = datetime.datetime.now().date()
        return today_date.strftime(self._date_format)

    @property
    def _now_time(self):
        now = datetime.datetime.now().time()
        return now.strftime(self._time_format)

    @property
    def _to_dos(self):
        to_do_dict = dict()
        return to_do_dict

    @property
    def _template_path(self):
        return f"./templates/{self._output_format}/"

    @property
    def _template_header_string(self):
        template_header_path = self._template_path + f"header.{self._output_format}"
        with open(template_header_path, "r") as FILE:
            template_header_string = FILE.readlines()
        return template_header_string

    @property
    def _template_footer_string(self):
        template_footer_path = self._template_path + f"footer.{self._output_format}"
        with open(template_footer_path, "r") as FILE:
            template_footer_string = FILE.readlines()
        return template_footer_string

    @ property
    def _blank_week_string(self):
        blank_week_template_path = self._template_path + f"blank_week.{self._output_format}"
        with open(blank_week_template_path, "r") as FILE:
            blank_week_string = FILE.readlines()
        return blank_week_string

    @property
    def _to_do_list(self):
        """
        Reads To-Do items from JSON and/or last month's log items that weren't checked off.

        :return:
        """
        to_do_list = list()
        return to_do_list

    def _validate_username(self, username):
        pass

    def _validate_template_format(self, template_format):
        pass

    def _set_template_format(self, template_format):
        """
        Chooses and sets the templates for weeks and months.
        :return:
        """
        self._output_format = template_format

    def _append_week(self):
        """
        Loads an existing week worklog file and appends to it with additional weeks.
        :return:
        """
        pass

    def display(self):
        pass

    def generate(self):
        # TODO: write internal calls to generate these strings for the user.
        log_text_string = f"{self._header_string}\n" \
                          f"{self._to_do_list}\n" \
                          f"{self._blank_weeks_string}\n\n" \
                          f"{self.notes_string}\n" \
                          f"{self._footer_string}"

        with open(self._output_file_path, "w") as LOG:
            LOG.writelines(log_text_string)
            print("Work Log generated!")

    def reset(self):
        pass
