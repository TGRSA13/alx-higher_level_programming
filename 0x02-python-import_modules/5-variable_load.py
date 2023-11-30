#!/usr/bin/python3

import importlib

def main():
    # Importing the variable 'a' from variable_load_5.py
    module_name = 'variable_load_5'
    variable_name = 'a'

    try:
        module = importlib.import_module(module_name)
        a = getattr(module, variable_name)

        print("The value of 'a' is:", a)
    except (ModuleNotFoundError, AttributeError):
        print(f"Error: Unable to import variable '{variable_name}' from '{module_name}.py'.")

if __name__ == "__main__":
    main()
