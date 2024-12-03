import re

def main():
  f = open("./q3_input.txt", "r")

  total = 0

  on = True
  for line in f:
    end = 0
    while end < len(line):
      data = ""
      while len(re.findall("mul\(\d{1,3},\d{1,3}\)", data)) == 0 and end < len(line):
        data += line[end]
        end += 1
      toggles = re.findall("don't\(\)|do\(\)", data)
      muls = re.findall("mul\(\d{1,3},\d{1,3}\)", data)
      on = toggles[-1] == "do()" if len(toggles) > 0 else on
      if on and len(muls) > 0:
        numbers = re.findall("\d+", muls[0])
        total += int(numbers[0]) * int(numbers[1])
      data = ""
    
  print(total)

main()