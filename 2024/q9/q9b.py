from os import path

def parse_disk_map(disk_map):
  id = 0
  free_space = False
  mapping = []
  for item in disk_map:
    mapping.append(int(item) * (['.'] if free_space else [str(id)]))
    if not free_space:
      id += 1
    free_space = not free_space
  return mapping

def compact_files(disk_mapping):
  end_index = len(disk_mapping) - 1
  start_index = 0

  while end_index > 0:
    if start_index > end_index:
      start_index = 0
      end_index -= 1
    elif len(disk_mapping[end_index]) == 0 or disk_mapping[end_index][0] == '.':
      end_index -= 1
    elif len(disk_mapping[start_index]) == 0 or disk_mapping[start_index][0] != '.':
      start_index += 1
    elif disk_mapping[start_index][0] == '.' and len(disk_mapping[start_index]) < len(disk_mapping[end_index]):
      start_index += 1
    else:
      if len(disk_mapping[end_index]) < len(disk_mapping[start_index]):
        disk_mapping.insert(start_index + 1, '.' * (len(disk_mapping[start_index]) -  len(disk_mapping[end_index])))
        end_index += 1
      disk_mapping[start_index] = disk_mapping[end_index]
      disk_mapping[end_index] = '.' * len(disk_mapping[start_index])
      start_index = 0

  return disk_mapping

def calculate_checksum(compacted_files):
  checksum = 0
  index = 0
  for i in range(len(compacted_files)):
    for val in compacted_files[i]:
      if val != '.':
        checksum += (index) * int(val)
      index += 1
  return checksum

def main():
  f = open(path.abspath("./q9_input.txt"), "r")

  for line in f:
    mapping = parse_disk_map(line)

  compacted_files = compact_files(mapping)
  checksum = calculate_checksum(compacted_files)

  print(checksum)


main()