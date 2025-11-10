import re
import pycodestyle


def patch_e225():
    """
    Change pycodestyle's E225 (missing whitespace around operator)
    to support Sage syntax sugar.
    Exp: R.<x>, A.<x, y>, L.<t1, t2, t3>
    """
    orig_func = pycodestyle.missing_whitespace_around_operator

    def missing_whitespace_around_operator_sage(logical_line, tokens):
        # support Sage syntax sugar
        # support R.<x>, RP.<x, y>, L.<t1, t2, t3>
        if re.search(r'\w+\.<\s*\w+(,\s*\w+)*\s*>', logical_line):
            return  

        # Otherwise, call the original function
        yield from orig_func(logical_line, tokens)

    # Replace the original function with the patched one
    pycodestyle.missing_whitespace_around_operator = missing_whitespace_around_operator_sage

    # Clear existing registrations of the original function
    pycodestyle._checks['logical_line'][orig_func] = []
    pycodestyle.register_check(missing_whitespace_around_operator_sage)