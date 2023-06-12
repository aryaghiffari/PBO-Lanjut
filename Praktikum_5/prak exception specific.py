try:
    Nim = int(input('enter your NIM : '))
except ValueError:
    print('Invalid NIM')
except KeyboardInterrupt:
    print('You have interrupted the program')