from typing import List, Dict, Callable
from collections import defaultdict
from re import compile
from random import choices
from string import ascii_lowercase, ascii_uppercase
from textwrap import indent

import nbformat

class TestcellBlock:
    cases: List[str]
    blocks: Dict[str, List[str]]

    def __init__(
            self
        ):
        self.cases = []
        self.blocks = defaultdict(lambda: [])

    def add_codeblock(
            self, 
            testcase: str, 
            code: str
        ):
        block = self.blocks[testcase]
        if len(block) == 0:
            self.cases.append(testcase)

        block.append(code)

    # def compile_into_py(
    #         self,
    #         cases: List[str] = [],
    #         transform_block: Callable[[str], str] = lambda x: x
    #     ) -> str:
    #     if len(cases) == 0:
    #         cases = self.cases
    #
    #     py_code = ""
    #     for testcase in cases:
    #         section = "\n".join(self.blocks[testcase])
    #         py_code += transform_block(section)
    #
    #     return py_code

    def get_code_for_testcase(
            self,
            testcase: str
        ) -> str:
        if testcase in self.cases:
            return "\n".join(self.blocks[testcase])
        else:
            return ""
def open_notebook(
        path: str    
    ) -> nbformat.NotebookNode:
    with open(path, "r") as nfp:
        notebook = nbformat.read(nfp, as_version=4)
    return notebook

def extract_with_prefix(
        notebook: nbformat.NotebookNode,
        prefix: str
    ) -> TestcellBlock:
    """Extract code blocks from a notebook matching a given prefix.

    Args:
        notebook: Notebook to extract code blocks from.
        prefix: Regex prefix to both decide if a block is extaction worthy, and to extract the testcase name.
                E.g. "### ASSIGNMENT CODE for Puzzle (.*) ==" 

    Returns:
        TestcellBlock object associating testcase names with code blocks.
    """
    per_testcase_code = TestcellBlock()
    pat = compile(prefix)
    clean_pat = compile('\W|^(?=\d)')

    for cell in notebook.cells:
        if cell.cell_type == "code":
            source = cell.source
            newline_idx = source.find("\n")
            first_line = source[:newline_idx]
            rest = source[newline_idx+1:]
            re_match = pat.fullmatch(first_line)
            if re_match is not None:
                testcase_name = re_match.group(1)
                testcase_name = clean_pat.sub("_", testcase_name)
                per_testcase_code.add_codeblock(testcase_name, rest)
    
    return per_testcase_code

def compile_code_and_tests_into_py(
    code_blocks: TestcellBlock,
    test_blocks: TestcellBlock
    ):
    part_name = choices(ascii_lowercase + ascii_uppercase, k=20)
    part_name = "".join(part_name)

    func_name = choices(ascii_lowercase + ascii_uppercase, k=20)
    func_name = "".join(func_name)
    py_code = f"def {func_name}({part_name}):\n"
    content = ""

    for testcase in code_blocks.cases:
        print("Writing in testcase", testcase)
        code_content = code_blocks.get_code_for_testcase(testcase)
        test_content = test_blocks.get_code_for_testcase(testcase)
        test_content += "\nreturn\n"

        content += code_content
        content += "\n"
        if len(test_content) > 0:
            content += f"if {part_name} == \"{testcase}\":\n"
            content += indent(test_content, "\t")

    py_code += indent(content, "\t")
    py_code += "\n"

    for testcase in test_blocks.cases:
        py_code += f"def test_{testcase}():\n\t{func_name}(\"{testcase}\")\n\n"

    return py_code
