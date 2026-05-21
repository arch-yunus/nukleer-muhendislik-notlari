
# Nükleer Mühendislik Notları ⚛️
![CI](https://github.com/arch-yunus/nukleer-muhendislik-notlari/actions/workflows/ci.yml/badge.svg?branch=main) ![Release](https://img.shields.io/github/v/release/arch-yunus/nukleer-muhendislik-notlari)

Bu depo (`nukleer-muhendislik-notlari`), nükleer enerji mühendisliğinin temel kavramlarını, reaktör sistem mimarilerini, nükleer güvenlik felsefelerini ve ileri teknoloji nükleer konseptleri bir araya getiren kapsamlı, açık kaynaklı bir eğitim ve araştırma dokümantasyonudur.

Nükleer teknoloji; fizik, termodinamik, malzeme bilimi ve sistem mühendisliğinin kesiştiği, "sıfır hata" toleransıyla ve yüksek güvenlik standartlarıyla çalışan multidisipliner bir alandır. Bu repodaki dokümanlar, nükleer enerjinin sadece nasıl üretildiğini değil, aynı zamanda bu üretim sürecinin tasarım aşamasından (Security by Design) atık yönetimine kadar nasıl güvenli hale getirildiğini adım adım incelemektedir.

> *"Nükleer tesislerin güvenliği, hiçbir zaman tek bir bileşenin kusursuzluğuna bağlanamaz; güvenlik, birbirini tamamlayan ve destekleyen ardışık bariyerlerin oluşturduğu bir mimaridir."* 
> — Derinlemesine Savunma (Defence in Depth) Felsefesi

---

## 🎯 Projenin Amacı ve Hedef Kitlesi

Bu açık kaynaklı projenin temel hedefleri şunlardır:
- Nükleer enerji sistemleri hakkında bilimsel, tarafsız ve güncel bilgileri Türkçe olarak sunmak.
- Uluslararası Atom Enerjisi Ajansı (IAEA) standartları çerçevesinde güvenlik ve emniyet konseptlerini netleştirmek.
- Geleneksel sistemlerin (PWR, BWR, CANDU) yanı sıra 4. Nesil (Gen IV) ve SMR (Küçük Modüler Reaktörler) gibi geleceğin teknolojilerini analiz etmek.

**Hedef Kitlesi:** Mühendislik öğrencileri, araştırmacılar, enerji sektörü profesyonelleri ve nükleer teknolojiye ilgi duyan herkes.

---

## 📚 Dokümantasyon Modülleri

İçerik, kavramsal bir bütünlük oluşturması amacıyla temel fizikten başlayarak sistem mimarilerine ve atık yönetimine doğru uzanan 4 ana modüle ayrılmıştır:

### Modül 1: Temel Kavramlar ve Nötronik
Bu bölüm, fisyon reaksiyonlarının temel mekaniklerini ele alır.
*   **Fisyon ve Zincirleme Reaksiyon:** Ağır çekirdeklerin nötron yutarak bölünmesi ve açığa çıkan enerjinin termodinamiği.
*   **Nötron Moderasyonu:** Hızlı nötronların termal nötronlara dönüştürülme süreci ve moderatör (yavaşlatıcı) tipleri (Hafif su, ağır su, grafit).

### Modül 2: Reaktör Mimarileri (Geleneksel ve İleri Sistemler)
Reaktörlerin soğutucu ve moderatör tercihlerine göre sınıflandırılması ve operasyonel farkları.
*   **Hafif Su Reaktörleri (LWR):** 
    *   *Basınçlı Su Reaktörleri (PWR):* İki döngülü yapı, buhar jeneratörleri ve yüksek basınç toleransı.
    *   *Kaynar Su Reaktörleri (BWR):* Tek döngülü yapı, reaktör içi buharlaşma ve türbin döngüsü.
*   **Ağır Su Reaktörleri (PHWR / CANDU):** Doğal uranyum kullanımı, düşük nötron yutma kapasiteli ağır su ($D_2O$) moderasyonu ve operasyon sırasında yakıt değişimi (on-power refuelling).
*   **Küçük Modüler Reaktörler (SMR):** Modüler üretim ve standartlaşma sayesinde inşaat süresi ve maliyet belirsizliklerinin azaltılması.
*   **4. Nesil Sistemler (Gen IV):** Ergimiş Tuz Reaktörleri (MSR) ve çevrimiçi yakıt işleme (online reprocessing) gibi ileri güvenlikli, yüksek verimli mimariler.

### Modül 3: Nükleer Güvenlik ve Emniyet Standardizasyonu
Nükleer kazaların ve dış tehditlerin önlenmesine yönelik global felsefeler.
*   **Derinlemesine Savunma (Defence in Depth):** Fiziksel ve sistemsel ardışık bariyerler (yakıt matrisi, zirkonyum kılıf, reaktör basınç kabı, sızdırmazlık koruma binası).
*   **Safety vs. Security:** 
    *   *Safety (Güvenlik):* Kasıt dışı arızalar, doğal afetler (deprem, tsunami vb.) ve insan hatalarına karşı koruma.
    *   *Security (Emniyet):* Sabotaj, terörizm, hırsızlık ve siber saldırı gibi kasıtlı eylemlere karşı koruma.

### Modül 4: Yakıt Çevrimi ve Atık Yönetimi
Uranyumun madenden çıkarılmasından atık olarak bertaraf edilmesine kadar geçen sürecin analizi.
*   **Zenginleştirme ve Yakıt Üretimi:** Uranyum-235 oranının artırılması süreçleri.
*   **Toryum Yakıt Çevrimi:** Toryum-232'nin nükleer yakıt (Uranyum-233) olarak kullanılabilmesi için gereken reaksiyonlar ve mühendislik zorlukları.
*   **Derin Jeolojik Depolama (Deep Geological Repository):** Yüksek seviyeli atıkların yerin yüzlerce metre altındaki stabil kaya oluşumlarında izolasyonu (Örn: Finlandiya, *Onkalo* projesi).

---

## 📂 Klasör ve Dosya Yapısı

Depoyu bilgisayarınıza indirdiğinizde karşılaşacağınız yapı şu şekildedir:

```text
nukleer-muhendislik-notlari/
├── docs/
│   ├── 01_temel_fizik_ve_notronik/
│   ├── 02_reaktor_mimarileri/
│   │   ├── pwr_ve_bwr_sistemleri.md
│   │   ├── candu_ve_agir_su.md
│   │   └── smr_ve_msr_gelecek_konseptleri.md
│   ├── 03_guvenlik_ve_emniyet/
│   │   ├── derinlemesine_savunma.md
│   │   └── safety_vs_security.md
│   └── 04_yakit_ve_atik_yonetimi/
│       ├── uranyum_ve_toryum_cevrimi.md
│       └── derin_jeolojik_depolama_onkalo.md
├── quizzes/
│   └── bilgi_testleri.md
├── assets/
│   └── gorseller_ve_semalar/
├── README.md
├── CONTRIBUTING.md
└── LICENSE

```

---

## 🤝 Nasıl Katkıda Bulunabilirsiniz?

Bu repo kolektif bir bilgi havuzudur ve her türlü bilimsel katkıya açıktır. Repoya destek olmak için:

1. Bu repoyu hesabınıza **Fork** edin.
2. Üzerinde çalışacağınız konu için yeni bir dal (branch) açın:
`git checkout -b ozellik/yeni-dokuman-adi`
3. Eklemek veya düzenlemek istediğiniz metinleri Markdown standartlarına uygun şekilde hazırlayın. Değişikliklerinizi kaydedin (Commit):
`git commit -m "Eklenti: CANDU reaktörlerinin nötron ekonomisi hakkında detay eklendi"`
4. Dalınızı uzak sunucuya gönderin:
`git push origin ozellik/yeni-dokuman-adi`
5. Bir **Pull Request (PR)** açarak değişikliklerin incelenmesini talep edin.

> Lütfen açtığınız PR'larda eklediğiniz bilginin kaynağını (makale, ders kitabı, IAEA raporu vb.) belirtmeye özen gösterin.

---

## 📄 Lisans

Bu proje, açık kaynaklı öğrenimi ve paylaşımı desteklemek amacıyla **MIT Lisansı** altında lisanslanmıştır. Kaynak göstererek dilediğiniz gibi kullanabilir, çoğaltabilir ve projelerinizde yer verebilirsiniz. Detaylar için `LICENSE` dosyasına göz atın.

```

```