import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__kodebuku = None
        self.__judul = None
        self.__pengarang = None
        self.__penerbit = None
        self.__tahun = None
        self.__kodekategori = None
        self.__url = "http://localhost/apperpus/buku_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodebuku(self):
        return self.__kodebuku
        
    @kodebuku.setter
    def kodebuku(self, value):
        self.__kodebuku = value
    @property
    def judul(self):
        return self.__judul
        
    @judul.setter
    def judul(self, value):
        self.__judul = value
    @property
    def pengarang(self):
        return self.__pengarang
        
    @pengarang.setter
    def pengarang(self, value):
        self.__pengarang = value
    @property
    def penerbit(self):
        return self.__penerbit
        
    @penerbit.setter
    def penerbit(self, value):
        self.__penerbit = value
    @property
    def tahun(self):
        return self.__tahun
        
    @tahun.setter
    def tahun(self, value):
        self.__tahun = value
    @property
    def kodekategori(self):
        return self.__kodekategori
        
    @kodekategori.setter
    def kodekategori(self, value):
        self.__kodekategori = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodebuku(self, kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idbuku']
            self.__kodebuku = item['kodebuku']
            self.__judul = item['judul']
            self.__pengarang = item['pengarang']
            self.__penerbit = item['penerbit']
            self.__tahun = item['tahun']
            self.__kodekategori = item['kodekategori']
        return data
    def simpan(self):
        payload = {
            "kodebuku":self.__kodebuku,
            "judul":self.__judul,
            "pengarang":self.__pengarang,
            "penerbit":self.__penerbit,
            "tahun":self.__tahun,
            "kodekategori":self.__kodekategori
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodebuku(self, kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        payload = {
            "kodebuku":self.__kodebuku,
            "judul":self.__judul,
            "pengarang":self.__pengarang,
            "penerbit":self.__penerbit,
            "tahun":self.__tahun,
            "kodekategori":self.__kodekategori
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodebuku(self,kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text