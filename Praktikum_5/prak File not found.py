try:
    x = open('fwf.txt')
except FileNotFoundError:
    print("FileNotFoundError successfully handled")