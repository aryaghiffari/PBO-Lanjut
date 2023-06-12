class AkunBank:
    def __init__(self, nomor_akun, saldo):
        self.nomor_akun = nomor_akun
        self.saldo = saldo
    def get_nomor_akun(self):
        self.nomor_akun
        print(f"Nomor Akun : {self.nomor_akun}")
    def get_saldo(self):
        self.saldo
        print(f"Saldo : {self.saldo}")
class AkunTabungan(AkunBank):
    def __init__(self, nomor_akun, saldo, persentase_bunga):
        super().__init__(nomor_akun, saldo)
        self.persentase_bunga = persentase_bunga
    def get_persentase_bunga(self):
        self.persentase_bunga
        print(f"Persentase bunga : {self.persentase_bunga}")
class CekAkun(AkunBank):
    def __init__(self, nomor_akun, saldo, overdraft_limit):
        super().__init__(nomor_akun, saldo)
        self.overdraft_limit = overdraft_limit
    def get_overdraft_limit(self):
        self.overdraft_limit
        print(f"Overdraft Limit : {self.overdraft_limit}")
# Hierarchical Inheritance
class JointAccount(AkunTabungan):
    def __init__(self, nomor_akun, saldo, persentase_bunga, owners):
        super().__init__(nomor_akun, saldo, persentase_bunga)
        self.owners = owners
    def get_owners(self):
        self.owners
        print(f"owner : {self.owners}")
a=JointAccount(1,"Rp.99.999.999.999","0%","Arya Ghiffari")
a.get_nomor_akun()
a.get_owners()
a.get_saldo()
a.get_persentase_bunga()