import math

def calculate_impermanent_loss(price_change_ratio):
    # Formul: IL = 2 * sqrt(k) / (1+k) - 1, burada k fiyat değişim oranıdır.
    il = (2 * math.sqrt(price_change_ratio)) / (1 + price_change_ratio) - 1
    return abs(il) * 100 # Yüzde olarak döndür

if __name__ == "__main__":
    # Örnek: ETH fiyatı havuza koyduğunuzdan beri 2 katına çıktı (%100 arttı)
    fiyat_degisimi = 2.0
    kayip = calculate_impermanent_loss(fiyat_degisimi)
    print(f"Fiyat {fiyat_degisimi} kat değiştiğinde Kalıcı Kayıp: %{kayip:.2f}")

    # Örnek: Fiyat %50 düştü
    fiyat_degisimi = 0.5
    kayip = calculate_impermanent_loss(fiyat_degisimi)
    print(f"Fiyat {fiyat_degisimi} kat değiştiğinde Kalıcı Kayıp: %{kayip:.2f}")