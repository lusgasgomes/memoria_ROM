end_0 = end_1 = end_2 = end_3 = end_4 = end_5 = end_6 = end_7 = end_8 = end_9 = end_10 = end_11 = end_12 = end_13 = end_14 = end_15 = '00000000'

while True:
   operação = str(input('Digite W para escrever, R para ler, L para listar e C para parar: '))
   if operação =='W' or operação=='w':
      write = (input('Digite o endereço de 4 bits: '))
      data  = (input('Digite um dado de 8 bits: '))
      if write =='0000':
          end_0 = data
      elif write =='0001':
          end_1 = data
      elif write =='0010':
          end_2 = data
      elif write =='0011':
          end_3 = data      
      elif write =='0100':
          end_4 = data      
      elif write =='0011':
          end_5 = data
      elif write =='0110':
          end_6 = data
      elif write =='0111':
          end_7 = data
      elif write =='1000':
          end_8 = data
      elif write =='1001':
          end_9 = data
      elif write =='1010':
          end_10 = data
      elif write =='1011':
          end_11 = data
      elif write =='1100':
          end_12 = data
      elif write =='1101':
          end_13 = data
      elif write =='1110':
          end_14 = data
      elif write =='1111':
          end_15 = data
      else:
          print('Dados inválidos')
   elif operação =='L' or operação =='l':
      print(f'{end_0}')
      print(f'{end_1}')
      print(f'{end_2}')
      print(f'{end_3}')
      print(f'{end_4}')
      print(f'{end_5}')
      print(f'{end_6}')
      print(f'{end_7}')
      print(f'{end_8}')
      print(f'{end_9}')
      print(f'{end_10}')
      print(f'{end_11}')
      print(f'{end_12}')
      print(f'{end_13}')
      print(f'{end_14}')
      print(f'{end_15}')


   elif operação == 'R' or operação == 'r':
      read = (input('Digite o endereço de 4 bits: '))
      if read =='0000':
         print(f'{end_0}')
      elif read =='0001':
         print(f'{end_1}')
      elif read =='0010':
         print(f'{end_2}')
      elif read =='0011':
         print(f'{end_3}')
      elif read =='0100':
         print(f'{end_4}')
      elif read =='0101':
         print(f'{end_5}')
      elif read =='0110':
         print(f'{end_6}')
      elif read =='0111':
         print(f'{end_7}')
      elif read =='1000':
         print(f'{end_8}')
      elif read =='1001':
         print(f'{end_9}')
      elif read =='1010':
         print(f'{end_10}')
      elif read =='1011':
         print(f'{end_11}')
      elif read =='1100':
         print(f'{end_12}')
      elif read =='1101':
         print(f'{end_13}')
      elif read =='1110':
         print(f'{end_14}')
      elif read =='1111':
         print(f'{end_15}')
      else:
         ('Endereço inválido.')
   elif operação =='C' or 'c':
      end_0 = end_1 = end_2 = end_3 = end_4 = end_5 = end_6 = end_7 = end_8 = end_9 = end_10 = end_11 = end_12 = end_13 = end_14 = end_15 = '00000000'

