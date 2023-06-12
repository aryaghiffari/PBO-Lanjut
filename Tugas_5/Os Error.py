import os

try :
    File = 'text.txt'
    buka_file = os.open(File, os.O_RDWR)
    os.close(File)
except os.error:
    print("Error pada file :",File)