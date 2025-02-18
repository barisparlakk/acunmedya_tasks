#task2 - kullanicidan bir sayi alarak o sayiya kadar olan sayıların toplamını hesaplayan bir python prog.
"""
toplam = 0
num = int(input(" Hangi sayiya kadar olan sayilarin toplamini gormek istiyorsunuz? "))
for i in range(num):
    toplam += i
print(num, " Sayisina kadar olan sayilarin toplami: ",toplam)
"""
#task3 - 1 ile 100 arasindaki cift sayilari yazdiran kod
"""
for i in range(100):
    if i%2 == 0:
        print(i)
"""
#task4 - Kullanıcıdan alınan bir metni ters çeviren ve ekrana yazdıran bir Python programı yazın.
"""
sentence = input(" Ters cevirmek istediginiz metni giriniz: ")
rev_s = ""
for i in sentence:
    rev_s = i + rev_s
print(" Girdiginiz cumlenin ters cevrilmis hali: ", rev_s)
"""