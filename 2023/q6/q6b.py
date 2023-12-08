import re

def main():
  f = open("./q6_input.txt", "r")

  total = 0
  time_line = f.readline()
  time_numbers = re.findall("\d+", time_line)
  time = int(''.join(time_numbers))
  
  distance_line = f.readline()
  distance_numbers = re.findall("\d+", distance_line)
  distance = int(''.join(distance_numbers))

  total = 1

  wins = 0
  for j in range(time):
    final_distance = (time - j) * j
    if final_distance > distance:
      wins += 1
  total *= wins


  print(total)

main()