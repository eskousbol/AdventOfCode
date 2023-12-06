import re
from datetime import datetime

def merge_ranges(value1, value2):
  a = max(value1[0], value2[0])
  b = min(value1[1], value2[1])

  overlap_range =range(a, b)

  if len(overlap_range) == 0:
    return [value1, value2]
  else:
    # Add values not impacted as is
    # Add values impacted modified
    return [[min(value1[0], value2[0]), max(value1[1], value2[1])]]

def merge_values(values):
  if len(values) ==1:
    return values
  merged_values = []
  merge_occured = True
  while merge_occured:
    merge_occured = False
    for value1 in values:
      for value2 in values:
        if value1 != value2:
          merged = merge_ranges(value1, value2)
          print(value1, value2, merged)
          print(merged)
          if len(merged) == 1:
            merge_occured = True
          for item in merged:
            print('hi')
            if item not in merged_values:
              merged_values.append(item)
    if len(values) == len(merged_values):
      merge_occured = False
    values = merged_values
    print(merged_values)
  return merged_values

def main():
  f = open("./q5_test_input.txt", "r")

  seeds_line = f.readline().strip()

  seed_numbers = re.findall("\d+ \d+", seeds_line)

  mappings = []
  mapping = []
  line = f.readline()
  while line:
    mapping_numbers = re.findall("\d+", line)
    
    # Starting a new mapping
    if len(line.strip()) != 0 and len(mapping_numbers) == 0:
      if len(mapping) > 0:
        mappings.append(mapping)
      mapping = []

    # Otherwise it is a new set of mapping numbers
    if len(mapping_numbers) > 0:
      # range of numbers mapped and how many it gets changed by
      destination = int(mapping_numbers[0])
      source = int(mapping_numbers[1])
      val_range = int(mapping_numbers[2])
      mapping.append([source, source + val_range, destination - source])

    line = f.readline()
  mappings.append(mapping)

  lowest_location = float('inf')
  for number in seed_numbers:
    pair = number.split(' ')
    old_values = [[int(pair[0]), int(pair[0]) + int(pair[1]) - 1]]
    values = []
    for resource_mapping in mappings:
      for mapping in resource_mapping:
        print('-----------------------------')
        print(mapping)

        for old_value in old_values:
          a = max(mapping[0], old_value[0])
          b = min(mapping[1], old_value[1])
          overlap_range =range(a, b)
          if len(overlap_range) == 0:
            if old_value not in values:
              values.append(old_value)
          else:
            # Add values not impacted as is
            # Add values impacted modified

            if [a + mapping[2], b + mapping[2]] not in values:
              values.append([a + mapping[2], b + mapping[2]])
            if a > old_value[0] and [old_value[0], a] not in values:
              values.append([old_value[0], a])
            if b < old_value[1] and [b, old_value[1]] not in values:
              values.append([b, old_value[1]])
      
      breaks = []
      if len(values) == 2:
        values = merge_ranges(values[0], values[1])

      values = merge_values(values)
      old_values = values
      values = []


main()