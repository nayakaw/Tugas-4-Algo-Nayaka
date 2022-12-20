class Kendaraan:
    def __init__(self, nama, jumlah_roda):
        self.nama = nama
        self.jumlah_roda = jumlah_roda

    def berkendara(self):
        print(f"{self.nama} sedang berkendara")

class Motor(Kendaraan):
    def __init__(self, nama, jumlah_roda, jumlah_susunan_silinder):
        super().__init__(nama, jumlah_roda)
        self.jumlah_susunan_silinder = jumlah_susunan_silinder

    def ngebut(self):
        print(f"{self.nama} sedang ngebut")

class Mobil(Kendaraan):
    def __init__(self, nama, jumlah_roda, jumlah_penumpang):
        super().__init__(nama, jumlah_roda)
        self.jumlah_penumpang = jumlah_penumpang

    def mudik(self):
        print(f"{self.nama} sedang mudik")

class Bis(Kendaraan):
    def __init__(self, nama, jumlah_roda, jumlah_penumpang):
        super().__init__(nama, jumlah_roda)
        self.jumlah_penumpang = jumlah_penumpang

    def beroperasi(self):
        print(f"{self.nama} sedang beroperasi")

class Truk(Kendaraan):
    def __init__(self, nama, jumlah_roda, kapasitas_muatan):
        super().__init__(nama, jumlah_roda)
        self.kapasitas_muatan = kapasitas_muatan

    def mengangkut(self):
        print(f"{self.nama} sedang mengangkut muatan")

# Membuat instance object dari setiap sub class
motor1 = Motor("Motor: \nHonda CBR", 2, 4)
mobil1 = Mobil("\nMobil: \nToyota Avanza", 4, 7)
bis1 = Bis("\nBus: \nPO Harapan Jaya", 4, 30)
truck1 = Truk("\nTruk:\nMitsubishi Colt Diesel", 6, 5000)

# Menggunakan method dari masing-masing object
motor1.ngebut()
mobil1.mudik()
bis1.beroperasi()
truck1.mengangkut()