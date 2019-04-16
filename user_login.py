"""



"""

print("""

KULLANICI GİRİŞİ

""")


sys_kullanici_adi = "MrYasin"

sys_parola = "244466666"


kullanici_adi = input("Kullanıcı adı: ")
parola = input("Parola: ")


if kullanici_adi == sys_kullanici_adi and parola != sys_parola:

    print("Parola Hatalı!")

elif kullanici_adi != sys_kullanici_adi and parola == sys_parola:

    print("Kullanıcı Adı Hatalı!")

elif kullanici_adi != sys_kullanici_adi and parola != sys_parola:

    print("Kullanıcı adı ve Parola Hatalı!")

else:

    print("Giriş Başarılı!")



