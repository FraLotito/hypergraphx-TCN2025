# Running `pytest solutions/` will pick up this file.
# It switches the target to 'solution' and reuses every test in tests/.
import os, pkgutil, importlib, tests  # tests must be a package (has __init__.py)

os.environ["TARGET_PACKAGE"] = "solutions"

# Import every test_*.py module from the tests package and expose its tests here
for mod in pkgutil.iter_modules(tests.__path__):
    if mod.name.startswith("test_"):
        m = importlib.import_module(f"tests.{mod.name}")
        globals().update(m.__dict__)
