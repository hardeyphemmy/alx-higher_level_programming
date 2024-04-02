#!/usr/bin/python3
"""The module that prints a text."""


def text_indentation(text):
    """Print a function text

    Arg:
        text(str): text must be a string

    Raise:
        TypeError: if text is not  string."""

    if not (isinstance(text, str)):
        raise TypeError("text must be a string")

        punctuation_marks = {'.', '?', ':'}
        start_of_line = True

        for char in text:
            if start_of_line and char == ' ':
                continue  # to skip space
            elif char == '\n':
                start_of_line = True  # reset if newline char is encountered
            else:
                print(char, end='')
                start_of_line = False
                if char in punctuation_marks:
                    print('\n\n', end='')


if __name__ == "__main__":
    text_indentation("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
