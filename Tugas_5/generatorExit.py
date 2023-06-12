hewan = {'singa','kucing','jerapah'}
def Hewan (list):
    for hewan in list:
        try:
            yield hewan
        except GeneratorExit as e :
            print(type(e))
            print("Generator Exit")
            return
H = Hewan(hewan)
for a in H:
    print(next(H))
    H.close()