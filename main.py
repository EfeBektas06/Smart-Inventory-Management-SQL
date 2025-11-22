import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# PROJE: Akıllı Depo Yönetim Sistemi ve ABC Stok Analizi
# YAZAN: [EFE BEKTAŞ]
# TEKNOLOJİLER: Python, SQL (SQLite), Pandas, Matplotlib
# =============================================================================

class DepoSistemi:
    def __init__(self):
        # Veritabanı Bağlantısı (Backend)
        self.baglanti = sqlite3.connect('depo_veritabani.db')
        self.imlec = self.baglanti.cursor()
        self.tablo_olustur()

    def tablo_olustur(self):
        # SQL Tablo Tasarımı (Schema)
        komut = """
            CREATE TABLE IF NOT EXISTS Urunler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad TEXT,
                fiyat REAL,
                stok INTEGER
            )
        """
        self.imlec.execute(komut)
        self.baglanti.commit()

    def urun_ekle(self, ad, fiyat, stok):
        # Veri Girişi (Transaction)
        komut = "INSERT INTO Urunler (ad, fiyat, stok) VALUES (?, ?, ?)"
        self.imlec.execute(komut, (ad, fiyat, stok))
        self.baglanti.commit()
        # print(f" Eklendi: {ad}") 

    def urunleri_listele(self):
        # Veri Okuma (Querying)
        print("\n---  GÜNCEL STOK LİSTESİ ---")
        self.imlec.execute("SELECT * FROM Urunler")
        veriler = self.imlec.fetchall()
        
        print(f"{'ID':<5} {'ÜRÜN ADI':<20} {'BİRİM FİYAT':<12} {'STOK':<8} {'DEĞER (TL)'}")
        print("-" * 65)
        
        for veri in veriler:
            toplam_deger = veri[2] * veri[3]
            print(f"{veri[0]:<5} {veri[1]:<20} {veri[2]:<12} {veri[3]:<8} {toplam_deger:.2f}")
        print("-" * 65)

    def finansal_analiz(self):
        # Mühendislik Analizi (Aggregation & KPIs)
        print("\n --- YÖNETİCİ RAPORU (ABC & KPI) ---")
        
        # SQL ile Hesaplama Gücü
        self.imlec.execute("SELECT SUM(fiyat * stok) FROM Urunler")
        toplam_sermaye = self.imlec.fetchone()[0]
        
        self.imlec.execute("SELECT ad, fiyat FROM Urunler ORDER BY fiyat DESC LIMIT 1")
        en_pahali = self.imlec.fetchone()
        
        self.imlec.execute("SELECT SUM(stok) FROM Urunler")
        toplam_adet = self.imlec.fetchone()[0]

        print(f" Toplam Envanter Değeri : {toplam_sermaye:,.2f} TL")
        print(f" Toplam Stok Adedi      : {toplam_adet}")
        if en_pahali:
            print(f" En Değerli Ürün        : {en_pahali[0]} ({en_pahali[1]} TL)")
        
        # Pandas ile ABC Analizi Görselleştirmesi
        # Veriyi SQL'den DataFrame'e çek
        df = pd.read_sql_query("SELECT ad, (fiyat*stok) as deger FROM Urunler", self.baglanti)
        
        if not df.empty:
            plt.figure(figsize=(10, 6))
            plt.bar(df['ad'], df['deger'], color='skyblue')
            plt.title('Ürün Bazlı Stok Değeri (ABC Analizi)')
            plt.xlabel('Ürünler')
            plt.ylabel('Toplam Değer (TL)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

# --- SENARYO ÇALIŞTIRMA ---
if __name__ == "__main__":
    app = DepoSistemi()
    
    # Test Verileri (Sadece ilk çalıştırmada anlamlıdır)
    # app.urun_ekle("Endüstriyel Robot", 45000, 2)
    # app.urun_ekle("Konveyör Bant", 5000, 10)
    # app.urun_ekle("Sensör", 250, 100)
    
    app.urunleri_listele()
    app.finansal_analiz()