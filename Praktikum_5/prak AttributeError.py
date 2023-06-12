class Hewan:
    def __init__(self) -> None:
        self.hewan = 'KUCING'
obj = Hewan()
try:
    print(obj.hewan)
except AttributeError:
    print("Tidak dapat menemukan attribute")
    