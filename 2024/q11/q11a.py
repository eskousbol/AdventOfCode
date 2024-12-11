
def main():
  f = open("./q11_input.txt", "r")

  for line in f:
    arrangement = line.strip().split(' ')

  # arrangement = ['125', '17']
  blinks = 25

  for blink in range(blinks):
    print(blink)
    new_arrangement = []
    for i in range(len(arrangement)):
      stone = arrangement[i]
      if stone == '0':
        new_arrangement.append('1')
      elif len(stone) % 2 == 0:
        new_arrangement.append(str(int(stone[:round(len(stone)/2)])))
        new_arrangement.append(str(int(stone[round(len(stone)/2):])))
      else:
        new_arrangement.append(str(int(stone) * 2024))
    arrangement = new_arrangement

  print(len(arrangement))

main()