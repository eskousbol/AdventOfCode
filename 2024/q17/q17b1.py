from datetime import datetime
import math

REGISTERS = {
  'A': None,
  'B': None,
  'C': None
}

def get_combo_operand(operand):
  if operand <= 3:
    return operand
  elif operand == 4:
    return REGISTERS['A']
  elif operand == 5:
    return REGISTERS['B']
  elif operand == 6:
    return REGISTERS['C']

def opcode_0_adv(operand):
  numerator = REGISTERS['A']
  denominator = pow(2, get_combo_operand(operand))

  REGISTERS['A'] = math.trunc(numerator/denominator)
  return [None, None]

def opcode_0_adv_inv(operand):
  numerator = REGISTERS['A']
  denominator = pow(2, get_combo_operand(operand))

  REGISTERS['A'] = numerator * denominator
  return [None, None]

def opcode_1_bxl(operand):
  REGISTERS['B'] = REGISTERS['B'] ^ operand
  return [None, None]

def opcode_1_bxl_inv(operand):
  opcode_1_bxl(operand)
  return [None, None]

def opcode_2_bst(operand):
  combo_operand = get_combo_operand(operand)
  REGISTERS['B'] = combo_operand % 8
  return [None, None]

def opcode_2_bst_inv(operand):
  combo_operand = get_combo_operand(operand)
  REGISTERS['B'] = combo_operand % 8
  return [None, None]

def opcode_3_jnz(operand):
  if REGISTERS['A'] == 0:
    return [None, None]
  
  return [None, operand - 2]

def opcode_4_bxc(operand):
  REGISTERS['B'] = REGISTERS['B'] ^ REGISTERS['C']
  return [None, None]

def opcode_5_out(operand):
  combo_operand = get_combo_operand(operand)
  return [combo_operand % 8, None]

def opcode_6_bdv(operand):
  numerator = REGISTERS['A']
  denominator = pow(2, get_combo_operand(operand))

  REGISTERS['B'] = math.trunc(numerator/denominator)
  return [None, None]

def opcode_7_cdv(operand):
  numerator = REGISTERS['A']
  denominator = pow(2, get_combo_operand(operand))

  REGISTERS['C'] = math.trunc(numerator/denominator)
  return [None, None]

def operate(instruction, operand):
  if instruction == 0:
    return opcode_0_adv(operand)
  elif instruction == 1:
    return opcode_1_bxl(operand)
  elif instruction == 2:
    return opcode_2_bst(operand)
  elif instruction == 3:
    return opcode_3_jnz(operand)
  elif instruction == 4:
    return opcode_4_bxc(operand)
  elif instruction == 5:
    return opcode_5_out(operand)
  elif instruction == 6:
    return opcode_6_bdv(operand)
  elif instruction == 7:
    return opcode_7_cdv(operand)
  
def main():
  start = datetime.now()
  f = open("./q17_input.txt", "r")
  # f = [
  #   'Register A: 117440',
  #   'Register B: 0',
  #   'Register C: 0',
  #   '\n',
  #   'Program: 0,3,5,4,3,0',
  # ]
  i = 0
  initial_registers = {

  }
  for line in f:
    values = line.strip().split(': ')
    if i == 0:
      REGISTERS['A'] = int(values[1].strip())
    elif i == 1:
      initial_registers['B'] = int(values[1].strip())
    elif i == 2:
      initial_registers['C'] = int(values[1].strip())
    elif i == 4:
      program = [int(x) for x in values[1].strip().split(',')]
      result = values[1].strip()
    i += 1

  done = False
  initial_a = 0
  while not done:
    REGISTERS['A'] = initial_a
    REGISTERS['B'] = initial_registers['B']
    REGISTERS['C'] = initial_registers['C']
    instruction_pointer = 0
    outputs = []
    while instruction_pointer < len(program) - 1:
      instruction = program[instruction_pointer]
      operand = program[instruction_pointer + 1]

      [output, jump] = operate(instruction, operand)
      if jump != None:
        instruction_pointer = jump
      if output != None:
        outputs.append(str(output))

      instruction_pointer = instruction_pointer + 2
    if ','.join(outputs) == result:
      done = True
    else:
      initial_a += 1
    if initial_a % 10000 == 0:
      print(initial_a)
  end = datetime.now()

  diff = end - start
  print(diff)
  print(','.join(outputs))

main()