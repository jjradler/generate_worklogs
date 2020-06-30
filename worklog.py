import datetime
import time


class WorkLog:
    """
    .. class:: WorkLog
    .. desc:: Generic base class for WorkLog documents
    """
    def __init__(self, input_path):
        self._last_week_path = input_path
        self.date = None
        self.time = None
        self.week_monday_dates = list()
        self._output_file_path = None
        self._profile = None
        self._to_dos = dict()
        self._user_data = dict()

        # Make these into properties, perhaps?
        self._file_header = None
        self._month_header = None
        self._week_header = None

    def set_template(self):
        """
        Chooses and sets the templates for weeks and months.
        :return:
        """
        pass

    def read_to_dos(self):
        """
        Reads To-Do items from JSON and/or last month's log items that weren't checked off.

        :return:
        """
        pass

    def write_new_month(self):
        """
        Writes an entire month of blank worklogs with alternating blocks.
        :return:
        """
        pass

    def write_new_week(self):
        """
        Writes WorkLog file header, user name and data, and any TODOs found in todos.json.
        """
        pass

    def append_week(self):
        """
        Loads an existing week worklog file and appends to it with additional weeks.
        :return:
        """
        pass





