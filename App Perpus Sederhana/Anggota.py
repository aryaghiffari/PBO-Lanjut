import requests
import json
class Anggota:
    def __init__(self):
        self.__id=None
        self.__kodeanggota = None
        self.__nama = None
        self.__jk = None
        self.__alamat = None
        self.__url = "http://localhost/apperpus/anggota_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodeanggota(self):
        return self.__kodeanggota
        
    @kodeanggota.setter
    def kodeanggota(self, value):
        self.__kodeanggota = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def jk(self):
        return self.__jk
        
    @jk.setter
    def jk(self, value):
        self.__jk = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodeanggota(self, kodeanggota):
        url = self.__url+"?kodeanggota="+kodeanggota
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idanggota']
            self.__kodeanggota = item['kodeanggota']
            self.__nama = item['nama']
            self.__jk = item['jk']
            self.__alamat = item['alamat']
        return data
    def simpan(self):
        payload = {
            "kodeanggota":self.__kodeanggota,
            "nama":self.__nama,
            "jk":self.__jk,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodeanggota(self, kodeanggota):
        url = self.__url+"?kodeanggota="+kodeanggota
        payload = {
            "kodeanggota":self.__kodeanggota,
            "nama":self.__nama,
            "jk":self.__jk,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodeanggota(self,kodeanggota):
        url = self.__url+"?kodeanggota="+kodeanggota
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text