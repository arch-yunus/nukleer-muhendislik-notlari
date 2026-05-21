"""Basit radyoaktif bozunma grafiği oluşturucu.

Gereksinimler: matplotlib (requirements.txt içinde listelendi)

Kullanım:
    python scripts/decay_plot.py
"""
import math
import sys

try:
    import matplotlib.pyplot as plt
except Exception:
    print("matplotlib bulunamadı. Lütfen 'pip install -r requirements.txt' çalıştırın.")
    sys.exit(1)

def remaining_fraction(t, half_life):
    lam = math.log(2) / half_life
    return math.exp(-lam * t)

def plot_decay(half_life=30.0, days=100):
    xs = list(range(0, days+1))
    ys = [remaining_fraction(x, half_life) for x in xs]
    plt.figure(figsize=(8,4))
    plt.plot(xs, ys, '-o')
    plt.title(f'Yarı-ömür = {half_life} gün')
    plt.xlabel('Gün')
    plt.ylabel('Kalan Fraksiyon')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('diagrams/decay_plot.png')
    print('Grafik kaydedildi: diagrams/decay_plot.png')

def main():
    half_life = 30.0
    plot_decay(half_life=half_life, days=100)

if __name__ == '__main__':
    main()
