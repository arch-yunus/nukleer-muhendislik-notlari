# Örnek Hesap: Radyoaktif Bozunma (Basit)

Radyoaktif bozunma için temel denklem:

$$N(t)=N_0 e^{-\lambda t}$$

Burada $\lambda$ bozunma sabiti, $N_0$ başlangıç nüfusu.

## Örnek: 1 g saf izotop, yarı-ömür T1/2 = 30 gün
- $\lambda = \ln 2 / T_{1/2} \approx 0.0231\;\text{gün}^{-1}$
- 10 gün sonra kalan: $N(10)=N_0 e^{-0.0231\times10}\approx 0.796 N_0$

Bu hesapların Python uygulaması `scripts/decay_calculator.py` içinde örneklenmiştir.