obj = ["Tv", "Kulkas","Kucing","uwu"]
def benda(elektronik1):
    for i in elektronik1:
        yield i
def error(i):
    try:
        val = next(i)
        print(val)
    except StopIteration:
        print("tidak ada lagi item yang akan dikembalikan oleh sebuah iterator")

a=benda(obj)
error(a)
error(a)
error(a)
error(a)
error(a)
