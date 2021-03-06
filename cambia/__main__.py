import importlib
import os
from pathlib import Path

from .config import *
from .switch import *

location = os.getcwd()
if "switchconf.py" not in os.listdir(location):
    raise ImproperlyConfigured
else:
    file = Path(location)
    mod = importlib.import_module(".switchconf", package=file.name)
    print(mod.CAMBIA_VARIABLES)
    run(prog="Cambia")
