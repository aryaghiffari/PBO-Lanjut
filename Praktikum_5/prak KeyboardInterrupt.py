try:
    print("Tekan CTRL +C untuk membatalkan")
    name = input("Enter your name: ")

except KeyboardInterrupt:
    print("Program dibatalkan")

else:
    print("You name is ",name)