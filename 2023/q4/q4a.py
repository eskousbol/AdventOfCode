import re

def main():
  f = open("./q4_input.txt", "r")

  total = 0
  for line in f:
    all_numbers = line.split(':')[1].strip()
    all_numbers_split = all_numbers.split('|')
    winning_numbers = re.findall("\d+", all_numbers_split[0]) 
    ticket_numbers = re.findall("\d+", all_numbers_split[1]) 
    points = 0
    for number in winning_numbers:
      if number in ticket_numbers:
        points += 1 if points == 0 else points
    total += points
  print(total)

main()