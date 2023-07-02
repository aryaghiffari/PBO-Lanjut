import requests
import json
class Peminjaman:
    def __init__(self):
        self.__id=None
        self.__nomorbukti = None
        self.__tgl_pinjam = None
        self.__kodeanggota = None
        self.__kodebuku1 = None
        self.__kodebuku2 = None
        self.__tglhrskembali = None
        self.__tgl_dikembalikan = None
        self.__status_pinjam = None
        self.__url = "http://localhost/apperpus/peminjaman_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def nomorbukti(self):
        return self.__nomorbukti
        
    @nomorbukti.setter
    def nomorbukti(self, value):
        self.__nomorbukti = value
    @property
    def tgl_pinjam(self):
        return self.__tgl_pinjam
        
    @tgl_pinjam.setter
    def tgl_pinjam(self, value):
        self.__tgl_pinjam = value
    @property
    def kodeanggota(self):
        return self.__kodeanggota
        
    @kodeanggota.setter
    def kodeanggota(self, value):
        self.__kodeanggota = value
    @property
    def kodebuku1(self):
        return self.__kodebuku1
        
    @kodebuku1.setter
    def kodebuku1(self, value):
        self.__kodebuku1 = value
    @property
    def kodebuku2(self):
        return self.__kodebuku2
        
    @kodebuku2.setter
    def kodebuku2(self, value):
        self.__kodebuku2 = value
    @property
    def tglhrskembali(self):
        return self.__tglhrskembali
        
    @tglhrskembali.setter
    def tglhrskembali(self, value):
        self.__tglhrskembali = value
    @property
    def tgl_dikembalikan(self):
        return self.__tgl_dikembalikan
        
    @tgl_dikembalikan.setter
    def tgl_dikembalikan(self, value):
        self.__tgl_dikembalikan = value
    @property
    def status_pinjam(self):
        return self.__status_pinjam
        
    @status_pinjam.setter
    def status_pinjam(self, value):
        self.__status_pinjam = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_nomorbukti(self, nomorbukti):
        url = self.__url+"?nomorbukti="+nomorbukti
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idpeminjaman']
            self.__nomorbukti = item['nomorbukti']
            self.__tgl_pinjam = item['tgl_pinjam']
            self.__kodeanggota = item['kodeanggota']
            self.__kodebuku1 = item['kodebuku1']
            self.__kodebuku2 = item['kodebuku2']
            self.__tglhrskembali = item['tglhrskembali']
            self.__tgl_dikembalikan = item['tgl_dikembalikan']
            self.__status_pinjam = item['status_pinjam']
        return data
    def simpan(self):
        payload = {
            "nomorbukti":self.__nomorbukti,
            "tgl_pinjam":self.__tgl_pinjam,
            "kodeanggota":self.__kodeanggota,
            "kodebuku1":self.__kodebuku1,
            "kodebuku2":self.__kodebuku2,
            "tglhrskembali":self.__tglhrskembali,
            "tgl_dikembalikan":self.__tgl_dikembalikan,
            "status_pinjam":self.__status_pinjam
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_nomorbukti(self, nomorbukti):
        url = self.__url+"?nomorbukti="+nomorbukti
        payload = {
            "nomorbukti":self.__nomorbukti,
            "tgl_pinjam":self.__tgl_pinjam,
            "kodeanggota":self.__kodeanggota,
            "kodebuku1":self.__kodebuku1,
            "kodebuku2":self.__kodebuku2,
            "tglhrskembali":self.__tglhrskembali,
            "tgl_dikembalikan":self.__tgl_dikembalikan,
            "status_pinjam":self.__status_pinjam
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_nomorbukti(self,nomorbukti):
        url = self.__url+"?nomorbukti="+nomorbukti
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text