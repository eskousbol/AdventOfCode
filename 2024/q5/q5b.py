import math

def is_sorted(rules, order):
  is_valid = True
  before_pages = set()
  for page in order:
    if page in rules.keys():
      if len(before_pages.intersection(rules[page])) > 0:
        is_valid = False
        break
    before_pages.add(page)
  return is_valid

def sort_row(rules, order):
  sorted = False
  while not sorted:
    before_pages = set()
    sorted = True
    for i in range(len(order)):
      page = order[i]
      if page in rules.keys():
        intersection = before_pages.intersection(rules[page])
        if len(intersection) > 0:
          sorted = False
          lowest_index = len(order)
          offending_value = None
          while len(intersection) > 0:
            value = intersection.pop()
            index = order.index(value)
            if index < lowest_index:
              lowest_index = index
              offending_value = value
          page_index = order.index(page)
          order[page_index] = offending_value
          order[lowest_index] = page
      before_pages.add(page)
  return order

def main():
  f = open("./q5_input.txt", "r")

  rules = {}
  middle_pages = 0
  for line in f:
    rule = line.split('|')
    if len(rule) == 2:
      first_page = int(rule[0])
      second_page = int(rule[1])
      if (first_page in rules.keys()):
        rules[first_page].append(second_page)
      else: 
        rules[first_page] = [second_page]
    else:
      raw_order = line.split(',')
      if len(raw_order) > 1:
        order = [int(val) for val in raw_order]
        is_valid = is_sorted(rules, order)
        if not is_valid:
          sorted_row = sort_row(rules, order)
          middle_pages += sorted_row[math.floor(len(sorted_row) / 2)]
  print(middle_pages)

main()