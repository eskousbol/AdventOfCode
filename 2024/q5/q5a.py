import math
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
        is_valid = True
        before_pages = set()
        for page in order:
          if page in rules.keys():
            if len(before_pages.intersection(rules[page])) > 0:
              is_valid = False
              break
          before_pages.add(page)
        if is_valid:
          middle_pages += order[math.floor(len(order) / 2)]
  print(middle_pages)

main()