import re

JAVASCRIPT = "//"
PYTHON = "#"

CAMBIA_SYNTAX = re.compile(r"<!(?P<command>.*)!>")
WORDS = []
