 1 #!/usr/bin/python3
  2 def replace_in_list(my_list, idx, element):
  3     """
  4     Replace an elemnt of a list.
  5     Args:
  6     my_list: The list from from the element.
  7     idx: index from the element to replace
  8     new_element: The number to replace
  9     Returns:
 10     The original list
 11     """
 12
 13     if 0 <= idx < len(my_list):
 14         my_list_copy = my_list.copy()
 15         my_list_copy[idx] = new_element
 16         return (my_list_copy)
 17     else:
 18         return (my_list)
 19
 20
 21 if __name__ == "__main__":
 22     my_list = [1, 2, 3, 4, 5]
 23     idx = 3
 24     new_element = 8
 25
 26     new_list = replace_in_list(my_list, idx, new_element)
 27     new_list[3] = 8
 28     print(new_list)
 29     print(my_list)
