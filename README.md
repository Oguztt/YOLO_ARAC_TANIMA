Kullanım Kılavuzu
Bu bölümde, projenin nasıl çalıştırılacağı adım adım açıklanmıştır.

Gereksinimler
Projeyi çalıştırmadan önce aşağıdaki bileşenlerin sisteminizde kurulu olduğundan emin olun:

Python 3.x

OpenCV kütüphanesi

YOLOv4 konfigürasyon dosyaları ve pre-trained ağırlıklar (weights)

OpenCV'yi terminal üzerinden aşağıdaki komutla kurabilirsiniz:

nginx
Kopyala
Düzenle
pip install opencv-python
Veri Girişi (Input Video)
Proje klasörü içinde data/ adlı bir klasör bulunmaktadır. Analiz etmek istediğiniz video dosyasını bu klasöre yerleştirmeniz gerekmektedir. Ardından, Python dosyasında yer alan video_path değişkenini kendi bilgisayarınızdaki tam dosya yoluna göre düzenleyin:


video_path = "C:/Users/oguz/Desktop/car-brand-detection-main/data/bmw.mp4"
Çıktı Yolu Tanımlama
İşlenmiş videonun kaydedileceği dizini output_path değişkeni ile belirtmelisiniz. Örnek:


output_path = "C:/Users/oguz/Desktop/car-brand-detection-main/output_video/bmw.avi"
Eğer bu klasörler mevcut değilse, manuel olarak oluşturulmalıdır.

Programı Çalıştırma
Tüm yollar tanımlandıktan sonra Python dosyasını çalıştırarak sistemi başlatabilirsiniz:


python detect.py
Program, video dosyasını kare kare analiz eder, araçları tespit eder ve marka adını video üzerine yazar. İşlem süresi videonun uzunluğuna ve çözünürlüğüne göre değişebilir.

Çıktı
İşlem tamamlandığında işlenmiş video output_video/ klasörüne .avi formatında kaydedilir. Kullanıcı, bu dosyayı oynatarak tespit edilen araç markalarını inceleyebilir.

Olası Hatalar ve Çözümler

"Video okunamıyor" hatası → Dosya yolunu kontrol edin, video mevcut olmalıdır.

"Modül bulunamadı" hatası → Gerekli kütüphanelerin yüklü olduğundan emin olun (örn: OpenCV).

Yavaş işleme → Video çözünürlüğü yüksekse işlem süresi uzayabilir.

TEKNİK DETAYLAR
Teknik Detaylar
Bu projede, araç markalarını tespit etmek amacıyla YOLOv4 (You Only Look Once) nesne tanıma algoritması kullanılmıştır. YOLOv4, görüntüyü tek bir aşamada analiz ederek yüksek doğruluk ve hız ile nesne tespiti yapabilen derin öğrenme tabanlı bir modeldir. Proje Python dili ile geliştirilmiş, görüntü işleme işlemleri için OpenCV kütüphanesi kullanılmıştır.

Sistem, önceden kaydedilmiş bir video dosyasını kare kare analiz ederek içerisindeki araçları tespit eder ve bu araçların markalarını sınıflandırır. Sınıflandırma işlemi, daha önce Kaggle üzerinden temin edilen ve 10 farklı araç markasını içeren bir veri setiyle eğitilmiş önceden hazır (pre-trained) ağırlık dosyaları ile gerçekleştirilmiştir. Bu sayede eğitim süreci atlanarak doğrudan tespit ve sınıflandırma işlemi yapılmaktadır.

Araç tespiti gerçekleştikten sonra, tanınan markalar görüntü üzerinde çerçeve ve yazı ile belirtilmekte, işlenmiş kareler birleştirilerek AVI formatında bir çıktı videosu oluşturulmaktadır. Tüm bu işlemler sonucunda çıktı, output_video klasörüne otomatik olarak kaydedilmektedir.

Projenin temel yapısı:

YOLOv4 modelinin yüklenmesi

Video dosyasının OpenCV ile karelere ayrılması

Her karenin YOLOv4 ile analiz edilmesi

Tespit edilen araçların markalarının belirlenmesi

Sonuçların görselleştirilerek kaydedilmesi

Kullanılan araçlar:

Python 3.x

OpenCV

YOLOv4 (Darknet altyapısı)

Kaggle araç marka veri seti

Pre-trained ağırlık dosyaları

Sistem %99 doğrulukla araç markası tespiti yapabilmektedir. Başarılı sonuçlar, veri setinin kalitesi ve kullanılan modelin yüksek performansı sayesinde elde edilmiştir.
