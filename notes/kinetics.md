# Reaktör Kinetiği (Point Kinetics) — Özet

Point kinetics (noktasal kinetik) reaktörün zamana bağlı güç değişimlerini basitleştirilmiş bir modelle açıklar. Temel denklem:

$$\frac{dn(t)}{dt} = \frac{\rho(t)-\beta}{\Lambda}n(t) + \sum_{i=1}^m \lambda_i C_i(t)$$

Burada:
- $n(t)$: zamana bağlı nötron yoğunluğu (veya güç ile orantılı)
- $\rho(t)$: reaktivite (birimsiz: $\Delta k / k$)
- $\beta$: toplam gecikmeli nötron fraksiyonu
- $\Lambda$: etkin prompt nötron ömrü (prompt neutron generation time)
- $C_i(t)$: i'inci gecikmeli nötron grubunun konsantrasyonu
- $\lambda_i$: i'inci gecikmeli grup için bozunma sabiti

Gecikmeli nötron grupları için:

$$\frac{dC_i(t)}{dt} = \frac{\beta_i}{\Lambda} n(t) - \lambda_i C_i(t), \quad i=1\ldots m$$

Basit durum: sabit reaktivite $\rho$ için çözümler karakteristik denklemin köklerine bağlıdır. Kritiklik durumları:
- Subkritik: $\rho < 0$ (güç azalır)
- Kritik: $\rho = 0$ (sabit)
- Süperkritik: $\rho > 0$ (güç artar)

Reaktör yanıtının zaman ölçekleri prompt ve gecikmeli bileşenlerle belirlenir — gecikmeli nötronlar kontrol edilebilir büyüme sağlar.

Detaylı türevler ve numerik örnekler ileride örnek hesap notunda eklenecek.