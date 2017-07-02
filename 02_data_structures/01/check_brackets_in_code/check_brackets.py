# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def is_balanced(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):

        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i+1))

        if next == ')' or next == ']' or next == '}':

            if len(opening_brackets_stack) > 0:
                last = opening_brackets_stack.pop()
            else:
                return i+1

            if last and last.Match(next) == False:
                return i+1

    if len(opening_brackets_stack) == 0:
        return 'Success'
    else:
        return opening_brackets_stack.pop().position


if __name__ == "__main__":
    text = input()

    print(is_balanced(text))
