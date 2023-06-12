import gc as g
import weakref as wk

try:
    class cek_objek(object):
        def __init__(self,nama) -> None:
            self.nama = nama
        def __del__(self):
            print('delete it ')
    obj_cek = cek_objek('objek')
    abc=wk.proxy(obj_cek)
    print('Sebelum dihapus =',abc.nama)
    obj_cek=None
    print('setelah dihapus =',abc.nama)
except ReferenceError as e:
    print("Terjadi referensi lemah merujuk pada objek yang telah dikumpulkan oleh garbage collector")