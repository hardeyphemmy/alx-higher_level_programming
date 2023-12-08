#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    function that returns a set of all elements in one set
    Args:
    set_1 - element in the first set
    set_2 - element in the second set
    Return:
    different element
    """
    odd_set = set_1.symmetric_difference(set_2)
    return (odd_set)


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}

    od_set = only_diff_elements(set_1, set_2)

    print(od_set)
