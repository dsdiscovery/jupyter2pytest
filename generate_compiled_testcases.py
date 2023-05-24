from jupyter_notebook_grader import open_notebook, extract_with_prefix, compile_code_and_tests_into_py

import sys

code_file = sys.argv[1]
test_file = sys.argv[2]
out_file = sys.argv[3]

code = open_notebook(code_file)
tests = open_notebook(test_file)

code_blocks = extract_with_prefix(code, "### ASSIGNMENT CODE for Puzzle (.*) ==")
test_blocks = extract_with_prefix(tests, "### TEST CASE for Puzzle (.*) ==")

tester_code = compile_code_and_tests_into_py(code_blocks, test_blocks)

with open(out_file, "w") as f:
    f.write(tester_code)
