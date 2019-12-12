import functions as mn
  # #(bin(num)[2:])
  # userInput = "ADD 1 2"
  # userInput = userInput.split()
  # text_file = open("yomomma.txt", "w")
  # text_file.write(str(userInput))
  # text_file.close()

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

  # keywords = {"ADD":0000}

  # print(bin(ascii("INS"))[2:])

still_running = True

mnemonic_file = open("mnemonicCode.txt", "r")
binary_write = open("binaryWirte.txt", "w+")

binary_list = []

while(still_running):
  code_read = mnemonic_file.readlines()

  print(code_read)

  for idx, line in enumerate(code_read):
    line = line.split()
    #print(line)
    for index, keyWord in enumerate(line):
      if(index == 0):
        binary_list.append(mn.appendKey(mn.mnuemonic, keyWord, binary_list))
      #print(index, keyWord)
      else:
        mn.checkKey(mn.mnuemonic, keyWord, binary_list, idx)
    binary_write.write(str(binary_list[idx]))
    binary_write.write("\n")

  mnemonic_file.close()
  binary_write.close()

  binary_write = open("binaryWirte.txt", "r")
  code_read = binary_write.readlines()
  

  for idx, line in enumerate(code_read):
    line = line.split()
    #print(line, "Code")
    if(line[0]):
      if(mn.checkFunctionError(mn.funcs, line[0])):
        this_is_key = mn.checkFunction(mn.funcs, line[0])
        if (this_is_key == mn.funcs["11001"]): #display
          fn = mn.display()
          fn()
        if(this_is_key == mn.funcs["11010"]): # print register
          fn = mn.funcs.get(line[0])
          p = mn.funcs.get(line[1])
          fn(p)
        elif (this_is_key == mn.funcs["01110"]): #register insert


          #print(mn.funcs[line[0]])
          fn = mn.funcs.get(line[0])
          # fn = mn.register_insert
          #fn = (mn.funcs[line[0]])
          # print(mn.funcs[line[0]])
          # print(line[1], "Register")
          print(line)
          register = (mn.funcs.get(line[1]))
          #print(line[1])
          #print(register, namestr(register, globals()))
          
          num = mn.BinaryToDecimal(line[2])
          print("Denize ", mn.BinaryToDecimal(line[2]))
          #print(num)
          register = fn(register, num)
          print(register, "Register")
          mn.register_load(mn.funcs[line[1]])
          print(mn.medium, "med")




        elif (this_is_key == mn.funcs["01111"]):# register load
          mn.register_load(mn.funcs.get(line[1]))
          print("hey" * 10)
        elif (this_is_key == mn.funcs["10000"]):#register save
          mn.register_save(mn.funcs.get(line[1]))
          print(mn.funcs.get("00010"), "R2")
          print("hey" * 10)
        elif (this_is_key == mn.funcs["10001"]): # array insert
          fn = mn.funcs.get(line[0])
          amount_of_nums = mn.BinaryToDecimal(line[1])
          array = mn.funcs.get(line[2])

          fn(array, amount_of_nums)
          print("hey" * 10)
        elif (this_is_key == mn.funcs["10010"]): # Tartet check
          fn = mn.funcs.get(line[0])
          target = mn.BinaryToDecimal(line[1])
          array = mn.funcs.get(line[2])
          
          fn(array, target)

          print("hey" * 10)
        elif (this_is_key == mn.funcs["10011"]): # sum of registers

          fn =  mn.funcs.get(line[0])
          mn.register_clear()

          #print(mn.medium)
          #print(mn.funcs.get(line[1]), "R5")
          #print(mn.funcs.get("00011"), "R3")

          for binn in line[1:]:
            #print(binn)

            register = mn.funcs.get(binn)

            #print(mn.funcs.get(binn), "sum %s" % binn)

            fn(register)
            
        elif (this_is_key == mn.funcs["10100"]): # difference of register

          register = mn.funcs.get(line[1])
          
          mn.register_load(register)
          
          fn = mn.funcs.get(line[0])
          if(len(line) > 2):
            for binn in line[2:]:
              fn(mn.funcs.get(binn))
              print(mn.medium, mn.funcs.get(binn))
          else: 
            print("Difference is not possible")

        elif (this_is_key == mn.funcs["10101"]): # product of register
          mn.register_one()
          for num in line[1:]:
            register = mn.funcs.get(num)
            mn.product_of_registers(register)
        elif (this_is_key == mn.funcs["10110"]): # jump to
          pass
        elif (this_is_key == mn.funcs["10111"]): # loop through
          pass
        elif (this_is_key == mn.funcs["11000"]): # exit program
          mn.exit_program()
        elif this_is_key == mn.funcs["00000"]: # clears all containers
          mn.clear()
        elif (this_is_key == mn.funcs["11011"]): # sum of array
          mn.register_clear()
          fn = mn.funcs.get(line[0])
          array = mn.funcs.get(line[1])

          fn(array)

          
        elif (this_is_key == mn.funcs["11100"]): # difference of array
          mn.register_clear()
          fn = mn.funcs.get(line[0])
          array = mn.funcs.get(line[1])
          

          fn(array)
        
        elif (this_is_key == mn.funcs["11101"]): # product of register
          fn = mn.funcs.get(line[0])
          array = mn.funcs.get(line[1])

          fn(array)
        elif (this_is_key == mn.funcs["11110"]): # quo REG

          register = mn.funcs.get(line[1])
          
          mn.register_load(register)
          
          fn = mn.funcs.get(line[0])
          if(len(line) > 2):
            for binn in line[2:]:
              fn(mn.funcs.get(binn))
              print(mn.medium, mn.funcs.get(binn))
          else: 
            print("Quotient is not possible")
            
        elif (this_is_key == mn.funcs["11111"]): # quotient of array
          mn.register_clear()
          fn = mn.funcs.get(line[0])
          array = mn.funcs.get(line[1])

          fn(array)
        
        else:
          print(this_is_key)
          print("super")
          mn.exit_error()



  binary_write.close()        
  still_running = False                
