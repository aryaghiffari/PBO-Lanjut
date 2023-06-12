rank_petualang = {"Argy Rem" :"S" ,"Shin sato": "S" ,"Rin": "S"}
try:
    value = rank_petualang["Argy Rem"]
except KeyError:
    print("Petualang tidak ditemukan!")