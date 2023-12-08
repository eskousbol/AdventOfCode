import re

def main():
  f = open("./q5_input.txt", "r")

  seeds_line = f.readline().strip()

  seed_numbers = re.findall("\d+ \d+", seeds_line)

  resource_mappings = []
  mapping = []
  line = f.readline()
  while line:
    mapping_numbers = re.findall("\d+", line)
    
    # Starting a new mapping
    if len(line.strip()) != 0 and len(mapping_numbers) == 0:
      if len(mapping) > 0:
        resource_mappings.append(mapping)
      mapping = []

    # Otherwise it is a new set of mapping numbers
    if len(mapping_numbers) > 0:
      # range of numbers mapped and how many it gets changed by
      destination = int(mapping_numbers[0])
      source = int(mapping_numbers[1])
      val_range = int(mapping_numbers[2])
      mapping.append([source, source + val_range, destination - source])

    line = f.readline()
  resource_mappings.append(mapping)

  lowest_location = float('inf')
  for number in seed_numbers:
    pair = number.split(' ')
    old_values = [[int(pair[0]), int(pair[0]) + int(pair[1])]]
    values = []
    for resource_mapping in resource_mappings:
      for mapping in resource_mapping:
        unmapped_values = []
        for i in range(len(old_values)):

          old_value = old_values[i]
          a = max(mapping[0], old_value[0])
          b = min(mapping[1], old_value[1])

          if a >= b:
            unmapped_values.append(old_value)
          else:
            # Add values not impacted as is
            # Add values impacted modified
            if [a + mapping[2], b + mapping[2]] not in values:
              values.append([a + mapping[2], b + mapping[2]])
            if a >= old_value[0] and [old_value[0], a] not in values:
              unmapped_values.append([old_value[0], a])
            if b < old_value[1] and [b, old_value[1]] not in values:
              unmapped_values.append([b, old_value[1]])
        old_values = unmapped_values

      old_values = values + unmapped_values

      values = []

    for value_range in old_values:
      for num in value_range:
        if num < lowest_location and num != 0:
          lowest_location = num

  print(lowest_location)

main()