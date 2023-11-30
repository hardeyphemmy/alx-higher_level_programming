#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Functions that returns a tuple length and its first character
    Arg:
    sentence: A string input
    Return:
    None character, if statement is empty
    """
    string_length = len(sentence)
    if len(sentence) > 0:
        first_character = sentence[0]
        return (first_character, string_length)
    else:
        return 0, (None)


if __name__ == "__main__":
    sentence = "Holberton"
    result = multiple_returns(sentence)

    length, first_character = multiple_returns(sentence)

    if length is not None:
        print("Length: {} - First character: {}".format(
            length, first_character))
    else:
        print("Length: None - First character: None")
