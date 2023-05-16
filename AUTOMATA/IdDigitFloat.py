import re

# Define regex patterns
patterns = {
    "id": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "digit": r"\d+",
    "float": r"[-+]?[0-9]+\.[0-9]+([eE][-+]?[0-9]+)?"
}

# Test strings
test_strings = ["2.3", "y_2", "var_3_name", "123", "456.78", "-3.14e+2"]

# Test regex patterns
for string in test_strings:
    print(f"Testing string: {string}")
    for pattern_name, pattern in patterns.items():
        if re.fullmatch(pattern, string):
            print(f"  Matched {pattern_name}")
        else:
            print(f"  Not matched {pattern_name}")
