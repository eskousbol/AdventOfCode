import re

def main():
  f = open("./q6_test_input.txt", "r")

  total = 0
  time_line = f.readline()
  time_numbers = re.findall("\d+", time_line)
  
  distance_line = f.readline()
  distance_numbers = re.findall("\d+", distance_line)

  total = 1
  for i in range(len(time_numbers)):
    time = int(time_numbers[i])
    distance = int(distance_numbers[i])

    wins = 0
    for j in range(time):
      final_distance = (time - j) * j
      if final_distance > distance:
        wins += 1
    total *= wins


  print(total)

main()