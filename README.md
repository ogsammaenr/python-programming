# Python Programlama Ödevleri Repo Rehberi

Bu depo, Helsinki Üniversitesi'nin [University of Helsinki MOOC](https://programming-25.mooc.fi) kapsamında sunduğu Python programlama kursuna ait çözüm ödevlerini içermektedir.

## 📌 Proje Hakkında Önemli Bilgiler

* **Ders Kaynağı:** Bu projede yer alan soruların ve egzersizlerin tamamı **[https://programming-25.mooc.fi](https://programming-25.mooc.fi)** adresindeki resmi Python kursundan alınmıştır.
* **Kapsam:** Depoda kursun tüm bölümlerinin çözümleri **bulunmamaktadır**. Sadece **Part 8 ve sonraki bölümlere** (Nesne Yönelimli Programlama - OOP, Fonksiyonel Programlama, Düzenli İfadeler, Pygame vb.) ait çözümler mevcuttur.

---

## 🛠️ Kurulum ve Gereksinimler

Projedeki özellikle görsel ve oyun tabanlı ödevleri (Part 13 ve Part 14) çalıştırabilmek için sisteminizde **Pygame** kütüphanesinin kurulu olması gerekmektedir.

Pygame kütüphanesi sistem genelinde kurulu değilse, terminalinizden aşağıdaki komutu çalıştırarak kullanıcı bazlı kurulum yapabilirsiniz:

```
python3 -m pip install -U pygame --user
```

---

## 🚀 Projeyi Çalıştırma Kılavuzu

Projedeki dosyaları (özellikle görsel varlıklar içeren **Part 13** ve **Part 14** altındaki Pygame uygulamalarını) çalıştırarken yolların doğru çözümlenebilmesi için **kesinlikle projenin kök dizininde (root directory)** bulunmalısınız.

### Doğru Çalıştırma Örneği

Proje ana dizinindeyken terminal üzerinden şu komut şablonuyla çalıştırma yapmalısınız:

```
python part_14/main.py
```

*Eğer ilgili klasörün içine (`cd part_14`) girip `python main.py` şeklinde çalıştırırsanız, 'robot.bmp' veya 'assets/' altındaki görseller yüklenirken yol hataları ('FileNotFoundError') alabilirsiniz.*

---

## 📝 Kod Yapısı ve İçerik Özeti

Depoda yer alan bazı önemli konu başlıkları ve örnek dosyalar şu şekildedir:

* **Part 8 & 9:** Sınıf (Class) ve Metot tanımlamaları, Kapsülleme (Encapsulation) mantığı ('car.py', 'recording.py'), Sınıf Nitelikleri ('postcodes.py').
* **Part 10:** Sınıf Hiyerarşileri ve Miras Alma (Inheritance) yapısı ('areas.py', 'laptop_computer.py', 'word_game.py').
* **Part 11:** List Comprehensions ('begin_with_a_vowel.py'), İleri Seviye Yineleme ve Özyineleme (Recursion) algoritmaları ('recursive_sum.py', 'greatest_node.py').
* **Part 12:** Fonksiyonlerin Argüman Olarak Kullanımı, Üreticiler (Generators - 'prime_numbers.py'), Fonksiyonel Programlama ('reduce', 'filter', 'map') ve Düzenli İfadeler (Regex - 'regular_expressions.py').
* **Part 13 & 14:** Pygame ile Temel Grafik/Animasyon İşlemleri ('bouncing_ball.py', 'robot_invasion.py') ve Flappy Bird benzeri modüler mini oyun uygulaması ('main.py', 'player.py', 'pipes.py').

---

<sub>**Not:** Kod içindeki yorum satırlarında Türkçe karakterlerin nadir olmasının sebebi kullandığım klavye düzeni ile ilgilidir.</sub>
