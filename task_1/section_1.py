#Toplama, cikarma, carpma, bolme, mod ve us alma iceren bir hesap makinesi yapacagiz.

sayi_1 = float(input("Islem yapmak istediginiz birinci sayiyi girin: "))
sayi_2 = float(input("Islem yapmak istediginiz ikinci sayiyi girin: "))
operatorler = ("+","-","*","/","%","**")
islem_operatoru = input("---Yapmak istediginiz islemi girin:--- \nToplama icin +,\nCikarma icin -,"
                        "\nCarpma icin *,\nBolme icin /,\nMod alma icin %,\nUs alma icin **.\n "
                        "Yapmak istediginiz islem -> ")

if islem_operatoru not in operatorler:
    print("Gecersiz bir operator girdiniz. Tekrar bir operator giriniz: ")
    input(" Yapmak istediginiz islem -> ")
elif islem_operatoru in operatorler:
    if islem_operatoru == "+":
        print(" Toplama isleminizin sonucu = ",sayi_1 + sayi_2)
    elif islem_operatoru == "-":
        print(" Cikarma isleminizin sonucu = ",sayi_1 - sayi_2)
    elif islem_operatoru == "*":
        print(" Carpma isleminizin sonucu = ",sayi_1 * sayi_2)
    elif islem_operatoru == "/":
        if sayi_2 == 0:
            print("Gecersiz islem. ")
        else:
            print(" Bolme isleminizin sonucu = ",sayi_1 / sayi_2)
    elif islem_operatoru == "%":
        if sayi_2 == 0:
            print(" Gecersiz islem.")
        else:
            print(" Mod alma isleminizin sonucu = ",sayi_1 % sayi_2)
    elif islem_operatoru == "**":
        print(" Us alma isleminizin sonucu = ",sayi_1 ** sayi_2)
