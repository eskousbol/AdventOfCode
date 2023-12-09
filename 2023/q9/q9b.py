def all_zero(my_list):
  if len(set(my_list)) != 1:
    return False
  return my_list[0] != 0

def main():
  f = open("./q9_input.txt", "r")

  values = 0
  for line in f:
    sequences = [[ int(x) for x in line.strip().split(' ') ]]
    while not all_zero(sequences[-1]):
      new_sequence = []
      sequence = sequences[-1]
      for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        new_sequence.append(diff)
      sequences.append(new_sequence)
    value = 0
    for i in range(0, len(sequences)):
      sequence = sequences[len(sequences) - 1 - i]
      value = sequence[0] - value
      sequence.insert(0, value)
    values += value

  print(values)

main()