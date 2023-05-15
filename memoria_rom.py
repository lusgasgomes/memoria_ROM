end_0 = end_1 = end_2 = end_3 = end_4 = end_5 = end_6 = end_7 = '0000'

while True:
   operação = str(input('Digite W para escrever, R para ler, L para listar e C para parar: '))
   if operação =='W' or operação=='w':
      write = (input('Digite o endereço de 3 bits: '))
      data  = (input('Digite um dado de 4 bits: '))
      if write =='000':
          end_0 = data
      elif write =='001':
          end_1 = data
      elif write =='010':
          end_2 = data
      elif write =='011':
          end_3 = data      
      elif write =='100':
          end_4 = data      
      elif write =='011':
          end_5 = data
      elif write =='110':
          end_6 = data
      elif write =='111':
          end_7 = data
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
   elif operação == 'R' or operação == 'r':
      read = (input('Digite o endereço de 3 bits: '))
      if read =='000':
         print(f'{end_0}')
      elif read =='001':
         print(f'{end_1}')
      elif read =='010':
         print(f'{end_2}')
      elif read =='011':
         print(f'{end_3}')
      elif read =='100':
         print(f'{end_4}')
      elif read =='101':
         print(f'{end_5}')
      elif read =='110':
         print(f'{end_6}')
      elif read =='111':
         print(f'{end_7}')
      else:
         ('')
   elif operação =='C' or 'c':
      end_0 = end_1 = end_2 = end_3 = end_4 = end_5 = end_6 = end_7 ='0000'
