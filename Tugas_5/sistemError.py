try:
    def hewan():
        pass
        raise SystemError
    hewan()
except SystemError as e:
    print("system error: terdapat kesalahan internal")