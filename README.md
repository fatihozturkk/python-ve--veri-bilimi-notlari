# 🐍 Sıfırdan Python & Veri Bilimi Notları

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scientific-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)

Bu repo; sıfırdan Python öğrenim sürecimden başlayarak Veri Analizi ve Görselleştirme kütüphanelerine (**NumPy, Pandas, Matplotlib**) uzanan kapsamlı kod notlarımı, modüler alıştırmalarımı ve veri seti uygulamalarımı içermektedir.

---

## 📌 İçerik Özeti

Proje kapsamındaki tüm konular, `sıfırdanpython.py` dosyası içerisinde adım adım ve uygulamalı olarak işlenmiştir:

| Modül | Kapsanan Konular & Yetkinlikler |
| :--- | :--- |
| **1. Python Temelleri** | Değişkenler, Veri Tipleri, String Formatlama/Metotları, Veri Yapıları (`List`, `Tuple`, `Dict`, `Set`), Değer ve Referans Tipleri. |
| **2. Mantık ve Döngüler** | Koşullu İfadeler (`if-elif-else`), `for` & `while` Döngüleri, `break/continue`, `List Comprehensions`, `enumerate` & `zip` kullanımı. |
| **3. Fonksiyonlar & İleri Konular** | Parametreler (`*args`, `**kwargs`), `lambda`, `map` & `filter`, Scope (`global`/`local`), **Decorators**, **Iterators** & **Generators**. |
| **4. OOP (Nesne Yönelimli)** | `Class` & `Object` yapısı, Yapıcı Metotlar (`__init__`), Kalıtım (`Inheritance`), Özel (Magic) Metotlar (`__str__`, `__len__`). |
| **5. Modüller & Dosya Yönetimi** | `math`, `random`, `os`, `re` (Regex), `json` modülleri ve Hata Yönetimi (`try-except`) ile `.txt` dosya okuma/yazma işlemleri. |
| **6. NumPy ile Veri Manipülasyonu** | 1D/2D Diziler, `shape` & `reshape`, İstatistiksel Metotlar, Satır/Sütun bazlı Toplam (`axis`), Boolean Indexing ve Matrix Stacking. |
| **7. Pandas ile Veri Analizi** | Series & DataFrame Mimarisi, Filtreleme, Kayıp Veri Yönetimi (`dropna`, `fillna`), Gruplama (`groupby`, `agg`), Birleştirme (`merge`, `concat`). |
| **8. Matplotlib ile Görselleştirme** | Line Plot, Subplots mimarisi, Bar Chart, Pie Chart (Pasta), Histogram ve Yığılı Alan Grafikleri. |

---

## 📊 Uygulama Veri Setleri (Real Datasets)

Depoda yer alan `.csv` veri setleri üzerinde gerçekleştirilen uçtan uca analiz alıştırmaları:

* 🎬 **`imdb.csv`:** Film başlıkları, IMDb puanları ve değerlendirme sayıları üzerinden filtreleme, sıralama ve mantıksal sorgu alıştırmaları.
* 🏀 **`nba.csv`:** Oyuncu yaşları, takımlar ve maaş verileri üzerinde `groupby` istatistikleri, metin temizleme ve Pandas `string` fonksiyon uygulamaları.


---

## 🚀 Yerelde Çalıştırma

Gerekli kütüphaneleri yükledikten sonra script'i direkt çalıştırabilirsiniz:

```bash
# Kütüphaneleri yükleyin
pip install pandas numpy matplotlib

# Kod dosyasını çalıştırın
python sıfırdanpython.py


