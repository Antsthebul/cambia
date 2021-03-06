import pytest

from cambia.config import *


def test_word_match_python(python_word):
    found = CAMBIA_SYNTAX.search(python_word)
    names = found.groupdict()
    assert names["command"] == "MOCK"


def test_raise_error_if_no_config():
    with pytest.raises(ImproperlyConfigured):
        import cambia
