import re

class Seed:
  def __init__(self, number):
    self.number = number
    self.mapping = number
    self.previous_mappings = []
    self.mapped = False
  
  def __str__(self):
    return f"Seed {self.number} maps to {self.mapping} (previously {self.previous_mappings})"

  def map(self, destination, source, range):
    if not self.mapped and self.mapping >= source and self.mapping < (source + range):
      self.previous_mappings.append(self.mapping)
      self.mapping = self.mapping - source + destination
      self.mapped = True

def main():
  f = open("./q5_input.txt", "r")

  seeds_line = f.readline().strip()

  seed_numbers = re.findall("\d+ \d+", seeds_line)

  line = f.readline()
  
  mappings = []
  mapping = []
  while line:
    mapping_numbers = re.findall("\d+", line)
    
    if len(line.strip()) != 0 and len(mapping_numbers) == 0 and len(mapping) != 0:
      mappings.append(mapping)
      mapping = []

    if len(mapping_numbers) > 0:
      mapping.append([int(mapping_numbers[0]), int(mapping_numbers[1]), int(mapping_numbers[2])])

    line = f.readline()

  lowest_location = float('inf')
  i = 0
  for numbers in seed_numbers:
    print('Seed done')
    pair = numbers.split(' ')
    seeds = range(int(pair[0]), int(pair[0]) + int(pair[1]))
    for protoseed in seeds:
      seed = Seed(protoseed)
      for resource_mappings in mappings:
        for resource_mapping in resource_mappings:
          seed.map(resource_mapping[0], resource_mapping[1], resource_mapping[2])
        seed.mapped = False
      if seed.mapping < lowest_location:
        lowest_location = seed.mapping

  print(lowest_location)


main()