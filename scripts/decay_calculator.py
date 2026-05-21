"""Basit radyoaktif bozunma hesaplayıcısı.

Kullanım:
    python scripts/decay_calculator.py
"""
import math

def remaining_fraction(t, half_life):
    lam = math.log(2) / half_life
    return math.exp(-lam * t)

def main():
    N0 = 1.0
    half_life = 30.0  # gün
    t = 10.0
    frac = remaining_fraction(t, half_life)
    print(f"Başlangıç: {N0}, {t} gün sonra kalan: {N0*frac:.6f} ({frac*100:.2f}%)")

if __name__ == '__main__':
    main()
