def factorial (n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == '__main__':
    try:
        print("the factorial of 999 is :{}".format(factorial(999)))
    except:
        print("Tidak dapat dihitung, angka terlalu besar")
