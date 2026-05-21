# Nükleer Enerji Mühendisliği Notları — Genişletilmiş

Bu dosya, depoda yeni eklenen teknik içeriklerin ve çalıştırma yönergelerinin daha detaylı bir özetini içerir.

## Eklenen örnek içerikler

- `notes/intro.md` — kısa giriş notu
- `notes/reactor-physics.md` — reaktör fiziği özet
- `notes/heat-transfer.md` — ısı transferi kısa notları
- `notes/example-calculation.md` — basit radyoaktif bozunma örneği
- `notes/kinetics.md` — noktasal reaktör kinetiği özeti
- `scripts/decay_calculator.py` — basit hesaplama aracı
- `scripts/decay_plot.py` — bozunma grafiği oluşturucu (matplotlib)
- `requirements.txt` — çizim için `matplotlib`
- `diagrams/reactor_core.svg` — basit reaktör çekirdeği şeması

## Görseller

Tüm görseller `diagrams/` klasöründe. `scripts/decay_plot.py` çalıştırıldığında `diagrams/decay_plot.png` oluşturulur.

## Nasıl çalıştırılır

1. Bağımlılıkları kurun:

```bash
pip install -r requirements.txt
```

2. Örnek bozunma grafiğini oluşturun:

```bash
python scripts/decay_plot.py
```

3. Basit hesaplayıcıyı çalıştırın:

```bash
python scripts/decay_calculator.py
```

## İleri adımlar

- Daha fazla teknik içerik (türevler, örnek problemler) ekleyebilirim.
- SVG diyagramları geliştirebilir, yeni PNG/PDF çıktıları üretebilirim.

İstediğiniz bir öncelik varsa söyleyin; ben eklemeye devam ederim.