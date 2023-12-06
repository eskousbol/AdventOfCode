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

  seeds = []
  seeds_line = f.readline().strip()

  seed_numbers = re.findall("\d+", seeds_line)
  for number in seed_numbers:
    seeds.append(Seed(int(number)))

  line = f.readline()
  
  while line:
    mapping_numbers = re.findall("\d+", line)
    
    if len(line.strip()) != 0 and len(mapping_numbers) == 0:
      for seed in seeds:
        seed.mapped = False

    if len(mapping_numbers) > 0:
      for seed in seeds:
        seed.map(int(mapping_numbers[0]), int(mapping_numbers[1]), int(mapping_numbers[2]))

    line = f.readline()

  lowest_location = float('inf')
  for seed in seeds:
    if seed.mapping < lowest_location:
      lowest_location = seed.mapping

  print(lowest_location)


main()