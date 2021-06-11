import re


class ImproperlyConfigured(Exception):
    def __str__(self):
        return (
            "No config file found, Are you sure "
            'your running in the root dir? and have created "switchconf.py" '
        )


JAVASCRIPT = "//"
PYTHON = "#"

CAMBIA_SYNTAX = re.compile(r"<!(?P<command>.*)!>")
WORDS = []
