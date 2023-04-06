vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

ortalama= int(ortalamaAsInteger)

if final < 40:
    print("Kaldı")

if ortalamaAsInteger < 50:
    print("Kaldı")

if (final*2) == vize:
    print("Kaldı")

else:
    print("Geçti")