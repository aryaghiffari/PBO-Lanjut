from decimal import Decimal

try :
    decimal = Decimal(23)
    print(decimal / 2)
except ZeroDivisionError :
    print("Tidak dapat dibagi nol")