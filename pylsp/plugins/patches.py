import re
import autopep8
import pycodestyle


def patch_pycodestyle(funcs):
    for orig_func, new_func, err_code, arg in funcs:
        err_codes, args = pycodestyle._checks['logical_line'][orig_func]
        pycodestyle._checks['logical_line'][new_func] = (err_codes + err_code, args + arg)
        del pycodestyle._checks['logical_line'][orig_func]


def patch_e225(logical_line=None, tokens=None):
    """
    Change pycodestyle check for PEP8 E225 (missing whitespace around operator) to support Sage syntax sugar.
    """
    # E225: R.<x>, A.<x, y>, L.<t1, t2, t3>
    sage_pattern = re.compile(r'\w+\.<\s*\w+\s*(,\s*\w+\s*)*\s*>')
    match = sage_pattern.search(logical_line)
    if match:
        inner = re.search(r'<\s*\w+\s*(,\s*\w+\s*)*\s*>', logical_line)
        if logical_line[inner.start() + 1] == ' ':
            pos = inner.start() + 1
            yield pos, "E201 whitespace after '<'"
        if logical_line[inner.end() - 2] == ' ':
            pos = inner.end() - 2
            yield pos, "E202 whitespace after '>'"
        if "=" in logical_line:
            inner = re.search(r'.=.', logical_line)
            if logical_line[inner.start()] != ' ' or logical_line[inner.end() - 1] != ' ':
                yield inner.start() + 1, "E225 missing whitespace around operator"
        if "," in logical_line:
            for inner in re.finditer(r'\w,.', logical_line):
                if logical_line[inner.end() - 1] != ' ':
                    yield inner.start() + 1, "E231 missing whitespace after ','"
        return
    # Otherwise, call the original function
    yield from pycodestyle.missing_whitespace(logical_line, tokens)

FUNCS = [
    (
        pycodestyle.missing_whitespace,
        patch_e225,
        ["E201", "E202", "E225"],
        [],
    ),
]

def patch():
    patch_pycodestyle(FUNCS)

if __name__ == "__main__":
    patch()
    # test code
    lines = [
        "R.< x,y ,z> = PolynomialRing(QQ)\n",
        "a = [1]\n",
    ]
    # test codestyle checker
    checker = pycodestyle.Checker(lines=lines)
    print(checker.check_all())
    # test code formatter
    fixed = autopep8.fix_code("".join(lines))
    print(fixed)