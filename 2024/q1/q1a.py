import re

def main():
  f = open("./q1_input.txt", "r")

  col_1 = []
  col_2 = []
  for line in f:
    vals = line.split('   ')
    col_1.append(int(vals[0]))
    col_2.append(int(vals[1]))
  col_1.sort()
  col_2.sort()

  result = 0
  for i in range(len(col_1)):
    result += abs(col_1[i] - col_2[i])

  print(result)

main()