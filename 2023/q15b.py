class Lens:
  def __init__(self, name, lens_length):
    self.lens_length = lens_length
    self.name = name

  def __str__(self):
     return f"{self.name} {self.lens_length}"
  
def holiday_hash(entry):
  value = 0
  for letter in entry:
    ascii_value = ord(letter)
    value += ascii_value
    value *= 17
    value = value % 256
  return value

def print_boxes(boxes):
  for box in boxes.keys():
    lens_boxes = boxes[box]
    print(f"---Box {box}--")
    for lens_box in lens_boxes:
      print(lens_box)

def main():
  f = open("./q15_input.txt", "r")

  data = f.readline()

  entries = data.split(',')

  boxes = {}
  for entry in entries:
    if '-' in entry:
      value = entry.split('-')[0]
      box = holiday_hash(value)
      if box in boxes.keys():
        for i in range(len(boxes[box])):
          lens = boxes[box][i]
          if lens.name == value:
            boxes[box].pop(i)
            break
    elif '=' in entry:
      len_updated = False
      values = entry.split('=')
      box = holiday_hash(values[0])
      if box in boxes.keys(): 
        for lens in boxes[box]:
          if lens.name == values[0]:
            lens.lens_length = values[1]
            len_updated = True
            break
        if not len_updated:
          boxes[box].append(Lens(values[0], values[1]))
      else:
        boxes[box] = [Lens(values[0], values[1])]

  total_focusing_power = 0
  for box in boxes.keys():
    lens_boxes = boxes[box]
    box_number = box + 1
    for i in range(len(lens_boxes)):
      lens = lens_boxes[i]
      total_focusing_power += box_number * (i + 1) * int(lens.lens_length)
  print(total_focusing_power)

main()