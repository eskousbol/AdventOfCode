import math

def is_int(number):
  return math.floor(number) == number

def max_value(test_values):
  val = 1
  for value in test_values:
    val *= value
  return val

def check_possible(target, test_values):
  if len(test_values) == 1:
    return test_values[0] == target

  value = test_values[-1]
  if is_int(target / value):
    new_target  = target/value
    is_possible =  check_possible(new_target, test_values[: -1])
    if is_possible:
      return True
  
  new_target = target - value
  return check_possible(new_target, test_values[: -1])

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