# selects which package to test: exercises (default) or solution
import importlib, os
TARGET_PACKAGE = os.getenv("TARGET_PACKAGE", "exercises")

def load(modname: str):
    # ex00_create -> exercises.ex00_create  (default)
    # ex00_create -> solution.ex00_create_solution  (when TARGET_PACKAGE=solution)
    if TARGET_PACKAGE == "solutions" and not modname.endswith("_solution"):
        modname = f"{modname}_solution"
    return importlib.import_module(f"{TARGET_PACKAGE}.{modname}")
