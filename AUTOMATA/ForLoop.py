import random

# Define the CFG rules
rules = {
    "<F_loop>": ["for (<initial> ; <condition> ; <inc/dec>) { <statement> }"],
    "<initial>": ["<DataType> <value>"],
    "<DataType>": ["int", "float"],
    "<value>": ["<digit>", "<floating_point>"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<floating_point>": ["<digit>.<digit>"],
    "<condition>": ["<value> <rel_op> <value>"],
    "<rel_op>": ["<", ">", "<=", ">=", "==", "!="],
    "<inc/dec>": ["<Identifier>++", "<Identifier>--"],
    "<statement>": ["<print_statement>", "<assignment_statement>"],
    "<print_statement>": ["print(<value>)"],
    "<assignment_statement>": ["<Identifier> = <value>"]
}

# Define a function to generate random strings based on the CFG
def generate_random_string(rule_key):
    if rule_key not in rules:
        return rule_key
    rule = random.choice(rules[rule_key])
    return "".join(generate_random_string(token) for token in rule.split())

# Generate a random loop using the CFG
loop = generate_random_string("<F_loop>")
print("Generated loop: " + loop)

# Check if the loop is valid
valid_loop = True
try:
    exec(loop)
except:
    valid_loop = False
if valid_loop:
    print("The loop is valid.")
else:
    print("The loop is not valid.")
