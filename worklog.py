import json


class WorkLog:
    """
    .. class:: WorkLog
    .. synopsis::
        Work log document template class. Contains entry fields as attributes that can be modified or rearranged as
        needed by the user.
    """
    def __init__(self):
        self.format = None
        self.input_path = None
        self.output_path = None

        get_format()
        check_format()


    def get_format(self):
        # read JSON configuration file.
        json.loads(configs, *)


    def check_format(self):
        """
        Format options include "md" for markdown, "txt" or None for raw text file, "rst" for ReStructured Text, "html"
        for HTML. Default is Markdown.
        :param format:
        """
        format_types = ["md", "txt", "html", "rst", None]
        try:
            self.format in format_types
        except ValueError(f"\'format\' argument is not a member of allowed \'format_types\' = {format_types}"):
            self.get_format()
        else:
            self.format = format
