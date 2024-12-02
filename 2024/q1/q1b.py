import re

def main():
  f = open("./q1_input.txt", "r")

  col_1 = []
  col_2 = []
  mapping = {}

  for line in f:
    vals = line.split('   ')
    col_1.append(int(vals[0]))
    col_2.append(int(vals[1]))

  for i in range(len(col_2)):
    if col_2[i] in mapping.keys():
      mapping[col_2[i]] += 1
    else: 
      mapping[col_2[i]] = 1

  result = 0
  for i in range(len(col_1)):
    if col_1[i] in mapping.keys():
      result += col_1[i] * mapping[col_1[i]]
  print(result)

main()