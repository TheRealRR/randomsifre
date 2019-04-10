from random import choice

karakterler = ["a","b","c","d","h","z","n","j","k","l","ı","n","t","h","s","v","x","A""B","C","D","!","J",1,2,3,4,56,7,8,9,0]

print ("Sifre Uzunlugu Kaç Karakter Olsun... ?")
sifreuzunluk = int(input())

sifre = ""

for i in range(sifreuzunluk):
    sifre += str(choice(karakterler))

print(sifre)


print ("Şifreniz Oluşturulmuştur")
