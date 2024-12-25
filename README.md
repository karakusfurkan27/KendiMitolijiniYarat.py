## README: Türk Mitolojisi Yaratıcı Uygulaması

### Tanım
Bu uygulama, Türk mitolojisi ve tarihindeki kahramanları tanıtmayı, rastgele hikaye ve etkinlikler oluşturmayı, karakter bilgilerini görüntülemeyi ve kullanıcıların yeni karakterler eklemesine olanak tanıyan bir grafiksel kullanıcı arayüzü (GUI) sunar. Türk tarihinden Alparslan, Fatih Sultan Mehmet, Battal Gazi gibi önemli figürlerin yer aldığı bu program, kullanıcıların mitolojik bir evren yaratmasını sağlar.

### Özellikler
1. **Rastgele Hikaye Gösterimi**: Mitolojiye ait bir hikaye rastgele seçilerek kullanıcıya gösterilir.
2. **Rastgele Etkinlik Oluşturma**: Keşif, savaş, ihanet gibi rastgele olaylar oluşturulur.
3. **Karakter Etkileşimi**: Seçili karakterler arasında bir saldırı etkileşimi gerçekleşir ve sonuç gösterilir.
4. **Karakter Bilgilerini Görüntüleme**: Mitolojideki mevcut karakterlerin bilgileri ve geçmişleri kullanıcıya sunulur.
5. **Yeni Karakter Ekleme**: Kullanıcı, uygulamaya yeni karakterler ekleyebilir. Karakter adı, rolü, güçleri ve arka plan bilgileri girilebilir.

### Gereksinimler
- **Python 3.x**
- **Tkinter** (Python'un standart kütüphanesi ile gelir)
- **random** modülü (Python'un standart kütüphanesi ile gelir)

### Kurulum ve Çalıştırma
1. Python 3.x yüklü olduğundan emin olun.
2. Kodun bulunduğu dizine gidin.
3. Terminal veya komut satırında şu komutu çalıştırarak uygulamayı başlatın:
   ```bash
   python <dosya_adı>.py
   ```
4. Uygulama çalıştığında bir pencere açılacaktır ve Türk Mitolojisi Yaratıcı'nın ana ekranı görüntülenecektir.

### Kullanım
- **Rastgele Hikaye Göster**: "Rastgele Hikaye Göster" butonuna tıklayın. Rastgele bir hikaye, bir bilgi kutusunda gösterilir.
- **Rastgele Etkinlik Oluştur**: "Rastgele Etkinlik Oluştur" butonuna tıklayın. Oluşan etkinlik bilgi kutusunda gösterilir.
- **Karakter Etkileşimi Göster**: "Karakter Etkileşimini Göster" butonuna tıklayın. İki karakter arasındaki bir etkileşim simüle edilir ve sonuç bilgi kutusunda görüntülenir.
- **Karakter Bilgilerini Göster**: "Karakter Bilgilerini Göster" butonuna tıklayın. Tüm karakterlerin bilgileri bir liste halinde görüntülenir.
- **Yeni Karakter Ekle**: "Yeni Karakter Ekle" butonuna tıklayın. Yeni bir pencere açılır ve burada karakter bilgilerini doldurarak kaydedebilirsiniz.

### Uygulamanın Yapısı
- **Character Sınıfı**: Karakterlerin temel özelliklerini (ad, rol, güçler, sağlık, vb.) ve işlemlerini (saldırı, iyileştirme, seviye atlama) tanımlar.
- **Mythology Sınıfı**: Mitolojiye ait karakterler, yerler ve hikayeleri saklar. Rastgele hikaye ve etkinlikler oluşturur.
- **MythologyApp Sınıfı**: Tkinter ile oluşturulmuş ana uygulama sınıfıdır. Kullanıcı arayüzünü ve olayları yönetir.

### Geliştirme Fikirleri
- Yeni yerler ve hikayeler eklenebilir.
- Karakterler arasında farklı türde etkileşimler oluşturulabilir.
- Oyuncuların mitolojik dünyada ilerlemelerini sağlayacak bir seviye sistemi eklenebilir.
- Daha fazla görsel iyileştirme ve temalar uygulanabilir.
