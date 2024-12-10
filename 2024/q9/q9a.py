from os import path

def parse_disk_map(disk_map):
  id = 0
  free_space = False
  mapping = []
  for item in disk_map:
    for i in range(int(item)):
      mapping.append('.' if free_space else str(id))
    if not free_space:
      id += 1
    free_space = not free_space
  return mapping

def compact_files(disk_mapping):
  end_index = len(disk_mapping) - 1
  start_index = 0

  while start_index < end_index:
    if disk_mapping[start_index] != '.':
      start_index += 1
    elif disk_mapping[end_index] == '.':
      end_index -= 1
    else:
      disk_mapping[start_index] = disk_mapping[end_index]
      disk_mapping[end_index] = '.'

  return disk_mapping

def calculate_checksum(compacted_files):
  checksum = 0
  for i in range(len(compacted_files)):
    if compacted_files[i] != '.':
      checksum += (i) * int(compacted_files[i])
  return checksum

def main():
  f = open(path.abspath("./q9_input.txt"), "r")

  for line in f:
    mapping = parse_disk_map(line)

  compacted_files = compact_files(mapping)
  checksum = calculate_checksum(compacted_files)

  print(checksum)


main()