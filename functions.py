import sys


def halt(error):
  halt = sys.exit("Program Halted due to Errors : %s" % error)

medium = 0
R1 = [0] 
R2 = [0]
R3 = [0]
R4 = [0]
R5 = [0]
R6 = [0]
R7 = [0]
R8 = [0]
A1 = []
A2 = []
A3 = [] 
A4 = [] 
A5 = []
SP = [0] 

def clear():
  global medium
  global R1
  global R2
  global R3
  global R4
  global R5
  global R6
  global R7
  global R8
  R1 = [0] 
  R2 = [0]
  R3 = [0]
  R4 = [0]
  R5 = [0]
  R6 = [0]
  R7 = [0]
  R8 = [0]
  medium = 0

def display():
  global medium
  print(medium)

def print_register(register):
  print(register[0])

def register_clear():
  global medium
  medium = 0

def register_one():
  global medium
  medium = 1

def register_insert(regs, num):
  #print(regs, num, "Before")
  regs[0] = num
  #print(regs, num, "After")
  return regs

def register_load(regs):
  global medium
  medium = regs[0]

def register_save(regs):
  regs[0] = medium

def array_insert(arr, num):
  for x in range(num):
    element = input('Enter number: %s for the array: ' % (x + 1))
    arr.append(int(element))

def target_check(arr, target):
  for index, element in enumerate(arr):



    if element == target:
      print('Number found on index: %s for array %s' % (index, arr))
      return
  print("o.o, no target found in %s" % arr)

def sum_of_registers(register):
  global medium
  medium += register[0]

def difference_of_registers(register):
  global medium
  medium -= register[0]

def product_of_registers(register):
  global medium
  medium *= register[0]

def sum_of_array(array):
  global medium
  register_clear()
  for index, num in enumerate(array):
    medium = medium + num

def difference_of_array(array):
  global medium
  medium = array[0]
  if(len(array) > 1):
    for index, num in enumerate(array[1:]):
      medium -= num
  else:
    raise ValueError("Array is not big enough for differences...")
    halt("Dirrefence Func")
    


def product_of_array(array):
  global medium
  register_one()
  for index, num in enumerate(array):
    medium = medium * num

def jump_to():
  pass

def loop_through():
  pass
  
def exit_program():
  sys.exit("""Thank for using,
 ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌       ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌       ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌       ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌       ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌       ▐░▌     ▐░▌  ▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌     ▐░▌  
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▄      ▐░▌      ▐░▌ ▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀  ▀       ▀         ▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                                                               
	\n Bye...""")

def exit_error():
  sys.exit("error, no matching  input was found try again ")

def decimalToBinary(n):
    total= str(bin(int(n))[2:])
    while len(total) != 8:
        total = "0" + total
    return total

def BinaryToDecimal(n):
   return int(n, 2)

def line_split(line):
  line = line.split()

def appendKey(dict, key, ls):
  return dict[key] + " "

def checkKey(dict, key, ls, index):
  if key in dict.keys():
    ls[index] += dict[key] + " "
  else:
    #print(bin(int(key))[2:])
    ls[index] += decimalToBinary(key) + " "

def checkFunctionError(dict, key):
  if(key in dict.keys()):
    return True
  else:
    raise TypeError("Key Word input is not found, Wrong")
    halt("CheckFuncionError Func")

def checkFunction(dict, key):
  return dict[key]

def quotient_of_registers(register):
  global medium
  medium  = medium // register[0]

def quotient_of_array(array):
  global medium
  medium = array[0]
  if(len(array) > 1):
    for index, num in enumerate(array[1:]):
      medium = medium // num
  else:
    raise ValueError("Array is not big enough for quotients...")
    halt("Quotient Func")

def easter_egg(our_grade):
  our_grade *= 1.05
  return 


funcs = {
  '00000' : clear,
  '00001' : R1, #no
  '00010' : R2,
  '00011' : R3,
  '00100' : R4,
  '00101' : R5,
  '00110' : R6,
  '00111' : R7,
  '01000' : R8,
  '01001' : A1,
  '01010' : A2,
  '01011' : A3,
  '01100' : A4,
  '01101' : A5, 
  '01110' : register_insert,
  '01111' : register_load,
  '10000' : register_save,
  '10001' : array_insert,
  '10010' : target_check,
  '10011' : sum_of_registers,
  '10100' : difference_of_registers,
  '10101' : product_of_registers,
  '10110' : jump_to,
  '10111' : loop_through,
  '11000' : exit_program,
  '11001' : display,
  '11010' : print_register,
  '11011' : sum_of_array,
  '11100' : difference_of_array,
  '11101' : product_of_array,
  '11110' : quotient_of_registers,
  '11111' : quotient_of_array
}

mnuemonic  = {
  'CLEAR' : '00000',
  'R1' : '00001',
  'R2' : '00010',
  'R3' : '00011',
  'R4' : '00100',
  'R5' : '00101',
  'R6' : '00110',
  'R7' : '00111',
  'R8' : '01000',
  'A1' : '01001',
  'A2' : '01010',
  'A3' : '01011',
  'A4' : '01100',
  'A5' : '01101',
  'INS' : '01110',
  'LOAD' : '01111',
  'SAVE' : '10000',
  'ARRAY' : '10001',
  'TAR' : '10010',
  'SUMR' : '10011',
  'SUBR' : '10100',
  'MULTR' : '10101',
  'JUMP' : '10110',
  'LOOP' : '10111',
  'END' : '11000',
  'PRINT' : '11001',
  'PRINTR' : '11010',
  'SUMA' : '11011',
  'SUBA' : '11100',
  'MULTA' : '11101',
  'QUOR' : '11110',
  'QUOA' : '11111'
  
}
