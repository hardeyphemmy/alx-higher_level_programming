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
        length_tuple = (string_length,)
        return (first_character, length_tuple)
    else:
        return (None)


if __name__ == "__main__":
    sentence = "Holberton"
    result = multiple_returns(sentence)

    first_character, length_tuple = result

    if length_tuple[0] is not None:
        print("Length: {:d} - First character: {:s}".format(
            length_tuple[0], first_character))
    else:
        print("Length: None - First character: None")
