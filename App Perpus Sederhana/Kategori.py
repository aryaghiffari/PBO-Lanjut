import requests
import json
class Kategori:
    def __init__(self):
        self.__id=None
        self.__kode_kategori = None
        self.__nama_kategori = None
        self.__url = "http://localhost/apperpus/kategori_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_kategori(self):
        return self.__kode_kategori
        
    @kode_kategori.setter
    def kode_kategori(self, value):
        self.__kode_kategori = value
    @property
    def nama_kategori(self):
        return self.__nama_kategori
        
    @nama_kategori.setter
    def nama_kategori(self, value):
        self.__nama_kategori = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_kategori(self, kode_kategori):
        url = self.__url+"?kode_kategori="+kode_kategori
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__kode_kategori = item['kode_kategori']
            self.__nama_kategori = item['nama_kategori']
        return data
    def simpan(self):
        payload = {
            "kode_kategori":self.__kode_kategori,
            "nama_kategori":self.__nama_kategori
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_kategori(self, kode_kategori):
        url = self.__url+"?kode_kategori="+kode_kategori
        payload = {
            "kode_kategori":self.__kode_kategori,
            "nama_kategori":self.__nama_kategori
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_kategori(self,kode_kategori):
        url = self.__url+"?kode_kategori="+kode_kategori
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
