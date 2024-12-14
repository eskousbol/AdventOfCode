from datetime import datetime

def main():
  start = datetime.now()
  f = open("./q_input.txt", "r")

  for line in f:
    pass

  result = 0
  end = datetime.now()

  diff = end - start
  print(diff)
  print(result)

main()