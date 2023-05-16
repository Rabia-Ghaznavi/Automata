import random

# Define the grammar rules for declaring a variable
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
    "<Digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

# Define a function to generate a variable name
def generate_identifier():
    # Generate an ID by expanding the "<Letter><ID>" rule
    identifier = "<ID>"
    for symbol in grammar:
        identifier = identifier.replace(symbol, random.choice(grammar[symbol]))
    return identifier

# Define a function to generate a variable declaration using the grammar rules
def generate_declaration():
    # Generate a declaration rule
    declaration = "<DataType> <ID>";
    for symbol in grammar:
        declaration = declaration.replace(symbol, random.choice(grammar[symbol]))
    # Replace the <Identifier> non-terminal with a generated variable name
    identifier = generate_identifier()
    declaration = declaration.replace("<ID>", identifier)
    return declaration

# Example usage
declaration = generate_declaration()
print("Generated declaration:", declaration)
