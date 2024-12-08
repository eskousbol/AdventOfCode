import math

def is_int(number):
  return math.floor(number) == number

def max_value(test_values):
  val = 1
  for value in test_values:
    val *= value
  return val

def concatenate_numbers(int_1, int_2):
  return int(str(int_1) + str(int_2))

def check_possible(target, test_values):
  if len(test_values) == 1:
    return test_values[0] == target

  value = test_values[-1]

  if is_int(target / value):
    new_target  = int(target/value)
    is_possible = check_possible(new_target, test_values[:-1])
    if is_possible:
      return True
  
  if len(test_values) == 2:
    new_target = concatenate_numbers(test_values[-2], value)
    if new_target == target:
      return True
  elif len(test_values) > 2:
    new_val = str(target)[0: -len(str(value))]
    trim_off = str(target)[-len(str(value)):]
    if new_val and trim_off and int(trim_off) == value:
      new_target = int(new_val)
      concat_possible = check_possible(new_target, test_values[:-1])
      if (concat_possible):
        return True

  new_target = target - value
  if new_target < 0:
    return False
  return check_possible(new_target, test_values[:-1])

def main():
  f = open("./q7_input.txt", "r")

  sum = 0
  for line in f:
    vals = line.split(': ')
    target = int(vals[0])
    test_vals = vals[1].split(' ')
    test_values = [int(val) for val in test_vals]
    is_possible = check_possible(target, test_values)
    if is_possible:
      sum += target

  print(sum)

main()