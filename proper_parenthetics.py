"""."""


def proper_parenthetics(string):
    """."""
    from stack import Stack
    container = Stack()
    closed_parens_counter = 0
    for char in string:
        if char == '(':
            container.push(char)
        elif char == ')':
            closed_parens_counter += 1
            if closed_parens_counter > len(container):
                return -1
    if closed_parens_counter != len(container):
        return 1
    else:
        return 0
