# Nükleer Enerji Mühendisliği Notları

Bu depo, kişisel nükleer enerji mühendisliği notlarımı, örnek hesapları ve görselleri düzenlemek için oluşturuldu.

## Kısa hedefler

- Ders notları ve özetler (Markdown)
- Hesap örnekleri ve formüller
- Kaynak linkleri ve referanslar

## Önerilen klasör yapısı

- `notes/` — konu bazlı notlar ve özetler
- `diagrams/` — diyagramlar, görseller
- `scripts/` — hesaplama veya dönüştürme araçları

## Katkıda bulunma

1. Yeni bir konu ekleyin: `notes/konu-adi.md`
2. Değişiklik yapmadan önce bir branch oluşturun: `git checkout -b feature/konu-adi`
3. Commit ve push sonrası pull request açın.

---

## Eklenen örnek içerikler

- `notes/intro.md`
- `notes/reactor-physics.md`
- `notes/heat-transfer.md`
- `notes/example-calculation.md`
- `notes/kinetics.md`
- `scripts/decay_calculator.py`
- `scripts/decay_plot.py`
- `requirements.txt`
- `diagrams/reactor_core.svg`

## Görseller

Tüm görseller `diagrams/` klasöründe. `scripts/decay_plot.py` çalıştırıldığında `diagrams/decay_plot.png` oluşturulur.

## Hızlı kullanım

Bağımlılıkları kurun:

```bash
pip install -r requirements.txt
```

Grafik oluşturun:

```bash
python scripts/decay_plot.py
```

Basit hesaplayıcı örneği:

```bash
python scripts/decay_calculator.py
```

İleri adımlar: daha fazla ders, örnek problem ve teknik diyagram ekleyebilirim. İsterseniz ben devam edeyim.

## Lisans

Bu depo MIT lisansı altında yayınlanmaktadır — detaylar için `LICENSE` dosyasına bakın.