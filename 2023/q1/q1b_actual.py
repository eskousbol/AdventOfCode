import re

def indices(str, item):
  my_indices = []
  last_index = 0
  while item in str and item in str[last_index:]:
    my_index = str.index(item, last_index)
    my_indices.append(my_index)
    last_index = my_index + len(item)
  return my_indices

def main():
  #f = open("./q1b_test.txt", "r")
  f = open("./q1_input.txt", "r")

  number_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  numbers = [1,2,3,4,5,6,7,8,9]
  total = 0
  for line in f:
    
    first_match = None
    first_match_index = 1000
    last_match = None
    last_match_index = -1

    for number in number_strings:
      num_indices = indices(line, number)
      for index in num_indices:
        if index < first_match_index:
          first_match = number_strings.index(number) + 1
          first_match_index = index
        if index > last_match_index:
          last_match = number_strings.index(number) + 1
          last_match_index = index

    for number in numbers:
      num_indices = indices(line, str(number))
      for index in num_indices:
        if index < first_match_index:
          first_match = number
          first_match_index = index
        if index > last_match_index:
          last_match = number
          last_match_index = index

    my_total = (first_match * 10) + last_match

    total += my_total
  print(total)

main()