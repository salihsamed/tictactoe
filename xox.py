import random
tahta=[" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "]
tahta2=["___","___","___","___","___","___","___","___","___"]
bot_h_kumesi=[1,2,3,4,5,6,7,8,9]

print("""
#############################################
        X-O-X OYUNUNA HOŞ GELDİN
         X VEYA O'DAN BİRİNİ SEÇ
HAMLE YAPMAK İSTEDİĞİN BÖLÜMÜN NUMARASINI YAZ
#############################################
""")

print(tahta[0],tahta[1],tahta[2],sep="   ",end="\n\n")
print(tahta[3],tahta[4],tahta[5],sep="   ",end="\n\n")
print(tahta[6],tahta[7],tahta[8],sep="   ",end="\n\n")

oyuncu_isaret=input("X Mİ OLMAK İSTİYORSUNUZ O'MU ?(x,o)?:").upper()
oyuncu_isaret=" "+oyuncu_isaret+" "

if oyuncu_isaret==" X ":
    bot_isaret=" O "
else:
    bot_isaret=" X "

for i in range(5):
    oyuncu_hamle=int(input("Oyuncu hamle sırası:",))
    print("\n")
    bot_h_kumesi.remove(oyuncu_hamle)
    tahta2[oyuncu_hamle-1]=oyuncu_isaret
    print("################")
    print(tahta2[0], tahta2[1], tahta2[2], sep="   ", end="\n\n")
    print(tahta2[3], tahta2[4], tahta2[5], sep="   ", end="\n\n")
    print(tahta2[6], tahta2[7], tahta2[8], sep="   ", end="\n\n")
    print("################")
    if tahta2[0]==tahta2[1]==tahta2[2]:
        if tahta2[0]==oyuncu_isaret:
            print("Oyuncu kazandı!")
            break
        elif tahta2[0] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[3]==tahta2[4]==tahta2[5]:
        if tahta2[3]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[3] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[6]==tahta2[7]==tahta2[8]:
        if tahta2[6]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[6] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[0]==tahta2[3]==tahta2[6]:
        if tahta2[0]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[0] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[1]==tahta2[4]==tahta2[7]:
        if tahta2[1]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[1] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[2]==tahta2[5]==tahta2[8]:
        if tahta2[2]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[2] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[0]==tahta2[4]==tahta2[8]:
        if tahta2[0]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[0] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[2]==tahta2[4]==tahta2[6]:
        if tahta2[2]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[2] ==bot_isaret:
            print("Bot kazandı !")
            break
    if i==4:
        print("Berabere")
        break

    bot_hamle=random.choice(bot_h_kumesi)
    tahta2[bot_hamle-1]=bot_isaret
    bot_h_kumesi.remove(bot_hamle)
    print("################")
    print(tahta2[0], tahta2[1], tahta2[2], sep="   ", end="\n\n")
    print(tahta2[3], tahta2[4], tahta2[5], sep="   ", end="\n\n")
    print(tahta2[6], tahta2[7], tahta2[8], sep="   ", end="\n\n")
    print("################")
    if tahta2[0]==tahta2[1]==tahta2[2]:
        if tahta2[0]==oyuncu_isaret:
            print("Oyuncu kazandı!")
            break
        elif tahta2[0] == bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[3]==tahta2[4]==tahta2[5]:
        if tahta2[3]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[3] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[6]==tahta2[7]==tahta2[8]:
        if tahta2[6]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[6] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[0]==tahta2[3]==tahta2[6]:
        if tahta2[0]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[0] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[1]==tahta2[4]==tahta2[7]:
        if tahta2[1]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[1] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[2]==tahta2[5]==tahta2[8]:
        if tahta2[2]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[2] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[0]==tahta2[4]==tahta2[8]:
        if tahta2[0]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[0] ==bot_isaret:
            print("Bot kazandı !")
            break

    if tahta2[2]==tahta2[4]==tahta2[6]:
        if tahta2[2]==oyuncu_isaret:
            print("Oyuncu kazandı !")
            break
        elif tahta2[2] ==bot_isaret:
            print("Bot kazandı !")
            break

