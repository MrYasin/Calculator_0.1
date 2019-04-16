"""

UPDATED user_login.py

used while loop(duh)

"""

print("""

KULLANICI GİRİŞİ

""")


sys_kullanici_adi = "MrYasin"

sys_parola = "244466666"

giris_hakki = 3

sec_code = "6OO65"


while True:
    kullanici_adi = input("Kullanıcı Adı: ")
    parola = input("Şifre: ")

    if kullanici_adi != sys_kullanici_adi and parola == sys_parola:
        print("Kullanıcı adı hatalı!")
        giris_hakki -= 1

    elif kullanici_adi == sys_kullanici_adi and parola != sys_parola:
        print("Şifre hatalı!")
        giris_hakki -= 1

    elif kullanici_adi != sys_kullanici_adi and parola != sys_parola:
        print("Kullanıcı adı ve Şifre hatalı!")
        giris_hakki -= 1

    else:
        print("\nGiriş Başarılı!")
        break

    if giris_hakki == 0:
        print("Giriş hakkınız doldu!\n")
        conf = input("Kullanıcı adı veya şifrenizi mi unuttunuz? (Y - N)\n")
        if conf == "y":
            code = input("Güvenlik kodunuzu girin: ")
            if code == sec_code:
                print(sys_kullanici_adi)
                print(sys_parola)

            else:
                print("Güvenlik kodunu yanlış girdiniz.")
                break

        elif conf == "n":
            print("Program kapatılıyor.")
            break





