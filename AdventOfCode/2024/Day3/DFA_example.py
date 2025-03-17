# Define token types
KEYWORDS = {"int", "if", "else", "while", "return"}
OPERATORS = {"+", "-", "*", "/", "="}
WHITESPACE = {" ", "\t", "\n"}

# DFA states
STATE_START = "START"
STATE_IDENTIFIER = "IDENTIFIER"
STATE_NUMBER = "NUMBER"
STATE_OPERATOR = "OPERATOR"

def tokenize(source_code):
    tokens = []
    state = STATE_START
    current_token = ""
    i = 0

    while i < len(source_code):
        char = source_code[i]

        if state == STATE_START:
            if char.isalpha() or char == "_":  # Identifiers & Keywords start
                state = STATE_IDENTIFIER
                current_token += char
            elif char.isdigit():  # Number start
                state = STATE_NUMBER
                current_token += char
            elif char in OPERATORS:  # Operator
                state = STATE_OPERATOR
                current_token += char
            elif char in WHITESPACE:  # Ignore whitespace
                i += 1
                continue
            else:
                raise ValueError(f"Unexpected character: {char}")

        elif state == STATE_IDENTIFIER:
            if char.isalnum() or char == "_":  # Continue identifier
                current_token += char
            else:  # End of identifier
                tokens.append(("KEYWORD" if current_token in KEYWORDS else "IDENTIFIER", current_token))
                current_token = ""
                state = STATE_START
                continue  # Reprocess this char

        elif state == STATE_NUMBER:
            if char.isdigit() or char == ".":  # Continue number
                current_token += char
            else:  # End of number
                tokens.append(("NUMBER", current_token))
                current_token = ""
                state = STATE_START
                continue  # Reprocess this char

        elif state == STATE_OPERATOR:
            tokens.append(("OPERATOR", current_token))
            current_token = ""
            state = STATE_START
            continue  # Reprocess this char

        i += 1

    # Handle last token
    if current_token:
        if state == STATE_IDENTIFIER:
            tokens.append(("KEYWORD" if current_token in KEYWORDS else "IDENTIFIER", current_token))
        elif state == STATE_NUMBER:
            tokens.append(("NUMBER", current_token))
        elif state == STATE_OPERATOR:
            tokens.append(("OPERATOR", current_token))

    return tokens

# Example source code
source_code = "int x = 42 + y"

# Run tokenizer
tokens = tokenize(source_code)

# Print tokens
for token in tokens:
    print(token)
