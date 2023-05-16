import random

# Define the grammar rules for declaring and initializing a variable
grammar = {
    "<DataType>": ["int", "float"],
    "<ID>": ["<Letter><id>"],
    "<id>": ["<Letter>", "<Digit><id>", "_<id>", ""],
    "<Letter>": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
                 "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                 "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                 "Y", "Z"],
    "<Digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<Expression>": ["<Value>", "<Value> <Operator> <Expression>"],
    "<Operator>": ["+", "-", "*", "/"],
    "<Value>": ["<Digit>", "<Digit>.<Digit>", "<ID>"],
    "<Initializer>": ["", "= <Expression>"]

}

# Define a function to generate a variable name
def generate_identifier():
    # Generate an ID by expanding the "<Letter><ID>" rule
    identifier = "<ID>"
    for symbol in grammar:
        identifier = identifier.replace(symbol, random.choice(grammar[symbol]))
    return identifier

# Define a function to generate a variable initialization statement using the grammar rules
def generate_initialization():
    # Generate a statement 
    statement = "<DataType> <ID> <Initializer> ;"
    for symbol in grammar:
        statement = statement.replace(symbol, random.choice(grammar[symbol]))
    # Replace the <ID> non-terminal with a generated variable name
    identifier = generate_identifier()
    statement = statement.replace("<ID>", identifier)
    # Generate an expression for initialization, if desired
    if "<Initializer>" in statement:
        expression = random.choice(grammar["<Expression>"])
        statement = statement.replace("<Initializer>", "= " + expression)
    else:
        statement = statement.replace("<Initializer>", "")
    return statement

# Example usage
for i in range(5):
    initialization = generate_initialization()
    print("Generated initialization:", initialization)
