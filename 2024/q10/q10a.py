def count_paths(position, trail_map):
  peaks = set()
  i = position[0]
  j = position[1]
  
  height = int(trail_map[i][j])
  if height == 9:
    peaks.add((i, j))
    return peaks
  
  height += 1
  if i + 1 < len(trail_map[0]) and int(trail_map[i + 1][j]) == height:
    peaks = peaks.union(count_paths([i+1, j], trail_map))
  if i - 1 >= 0 and int(trail_map[i - 1][j]) == height:
    peaks = peaks.union(count_paths([i-1, j], trail_map))
  if j + 1 < len(trail_map) and int(trail_map[i][j + 1]) == height:
    peaks = peaks.union(count_paths([i, j+1], trail_map))
  if j - 1 >= 0 and int(trail_map[i][j - 1]) == height:
    peaks = peaks.union(count_paths([i, j - 1], trail_map))
  
  return peaks

def main():
  f = open("./q10_input.txt", "r")
  trail_map = []
  for line in f:
    trail_map.append(list(line.strip()))

  count = 0
  for i in range(len(trail_map)):
    for j in range(len(trail_map[i])):
      height = int(trail_map[i][j])
      if height == 0:
        trail_score = count_paths([i,j], trail_map)
        count += len(trail_score)

  print(count)

main()