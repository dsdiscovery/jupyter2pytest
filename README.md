# Jupyter Notebook Grader

This is a script that will compile a jupyter notebook with a specified structure into a python script that is pytest compatible.

Importantly: all graded cells for the student MUST be prefixed with "### ASSIGNMENT CODE for Puzzle (whatever) ==" and all test cells
must be prefixed with "### TEST CASE for Puzzle (whatever) ==". Assignment code does not need to have a corresponding testcase and
all code dependencies must be included as assignment code cells in some form or another.

To generate the pytest script run "python3 generate_compiled_testcases.py [Assignment code notebook] [Testcases notebook] [Output script]"

Two examples have additionally been provided.
