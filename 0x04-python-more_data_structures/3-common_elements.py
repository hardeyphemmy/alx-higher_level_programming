#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Function that returns a set of common elements in two sets
    Args:
    set_1 - elements in first set
    set_2 -  element in the second set
    Return:
    common element in the set
    """
    common_set = set_1.intersection(set_2)
    return (common_set)


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)

    print(c_set)
