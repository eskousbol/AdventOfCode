from datetime import datetime

MAPPINGS = {}

def process_stone(stone, blinks_left):
  if str(stone) not in MAPPINGS:
    MAPPINGS[str(stone)] = {}
  
  if str(blinks_left) in MAPPINGS[str(stone)]:
    return MAPPINGS[str(stone)][str(blinks_left)]

  result = 0
  if blinks_left == 0:
    result += 1
  elif stone == '0':
    result += process_stone('1', blinks_left - 1)
  elif len(stone) % 2 == 0:
    result += process_stone(str(int(stone[:round(len(stone)/2)])), blinks_left - 1) + process_stone(str(int(stone[round(len(stone)/2):])), blinks_left - 1)
  else:
    result += process_stone(str(int(stone) * 2024), blinks_left - 1)
  
  MAPPINGS[str(stone)][str(blinks_left)] = result
  return result

def main():
  start = datetime.now()
  f = open("./q11_input.txt", "r")

  for line in f:
    arrangement = line.strip().split(' ')

  blinks = 75

  stone_count = 0
  for i in range(len(arrangement)):
    stone_count += process_stone(arrangement[i], blinks)

  end = datetime.now()
  difference = end - start
  print(stone_count)
  print('Ran in ' + str(difference.microseconds / 1000) + 'ms')

main()