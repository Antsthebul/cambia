print("yo")

from pathlib import Path
import os
import importlib


location = os.getcwd()
if "switchconf.py" not in os.listdir(location):
    raise ImproperlyConfigured
else:
    print("yo")
    file = Path(location)
    importlib.import_module(file.name + ".switchconf.py")
    print(CAMBIA_VARIABLES)
    run(prog="Cambia")
