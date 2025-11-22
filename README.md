# Akıllı Depo Yönetim Sistemi & Stok Analizi (WMS) 

Bu proje, Python ve SQL teknolojileri kullanılarak geliştirilmiş, ilişkisel veritabanı tabanlı bir **Envanter Takip Sistemi**dir. Endüstri Mühendisliğindeki stok yönetimi prensiplerini dijitalleştirmeyi amaçlar.

##  Projenin Amacı
Manuel stok takibindeki hataları önlemek ve yönetime anlık finansal raporlar sunmak.
* **Veri Bütünlüğü:** Ürünler ve stok hareketleri **SQLite** veritabanında yapısal olarak saklanır.
* **KPI Takibi:** Toplam envanter değeri ve stok seviyeleri anlık hesaplanır.
* **Görselleştirme:** Stok dağılımı grafiklerle analiz edilir.

##  Teknik Özellikler
* **Backend:** Python + SQLite (İlişkisel Veritabanı Tasarımı)
* **Veri İşleme:** SQL `INSERT`, `SELECT`, `SUM`, `ORDER BY` sorguları.
* **Raporlama:** Pandas Dataframe entegrasyonu.
* **Arayüz:** Konsol tabanlı formatlı veri gösterimi.

##  Nasıl Çalışır?
1. Program çalıştığında otomatik olarak `depo_veritabani.db` dosyasını oluşturur.
2. `Urunler` tablosunu SQL komutlarıyla inşa eder.
3. Ürün girişi, listeleme ve finansal analiz fonksiyonlarını çalıştırır.

---

*Geliştirici: [EFE BEKTAŞ]*
