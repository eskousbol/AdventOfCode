import re
from datetime import datetime

class SeedRange:
  def __init__(self, range):
    self.range = range
    self.mapping = range
    self.mapped = False
  
  def __str__(self):
    return f"Seeds {self.range} maps to {self.mapping}"

  def map(self, destination, source, range):

    if not self.mapped and self.mapping >= source and self.mapping < (source + range):
      self.mapping = self.mapping - source + destination
      self.mapped = True

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

  sorted_values = []
  for i in range(len(values)):
    place = 0
    if len(sorted_values) == 0:
      sorted_values.append(values[i]) 
    else:
      for j in range(len(sorted_values)):
        if values[i][0] > sorted_values[j][0]:
          print('inc')
          place += 1
        else:
          break
      sorted_values.insert(place, values[i])

  merged_indices = []
  merged_values = []
  merge_occured = True
  while merge_occured:
    merge_occured = False
    merged = []
    for i in range(len(sorted_values)):
      for j in range(len(sorted_values)):
        print(merged)
        print(sorted_values)
        if j <= i or i in merged_indices or j in merged_indices:
          continue
        value1 = sorted_values[i]
        value2 = sorted_values[j]
        merged = merge_ranges(value1, value2)
        print(value1, value2, merged)
        if len(merged) == 1:
          merged_indices.append(i)
          merged_indices.append(j)
          merge_occured = True
        for item in merged:
          if item not in merged_values:
            merged_values.append(item)
        
    if len(sorted_values) == len(merged_values):
      merge_occured = False
    sorted_values = merged_values
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

        unmapped_values = []

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
      print('BEFORE')
      print(values)
      print('-----------------------')
      values = merge_values(values)
      print('AFTER')
      print(values)
      old_values = values
      values = []

  print('END')
  print(old_values)

main()