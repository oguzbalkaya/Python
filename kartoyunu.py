import random
class Kart():
    def __init__(self,karttur,kartno):
        self.tur=karttur
        self.numara=kartno
deste=[]
for i in range(0,2):
    for j in range(1,11):
        if(i==0):
            karttur="Kırmızı"
        else:
            karttur="Siyah"
        deste.append(Kart(karttur,j))
#rastgele 5 er kart dağıtalım.
oyuncu1=[]
oyuncu2=[]
for i in range(0,5):
    rastgele=random.randint(0,len(deste)-1)
    oyuncu1.append(deste[rastgele])
    deste.pop(rastgele)
    rastgele2=random.randint(0,len(deste)-1)
    oyuncu2.append(deste[rastgele2])
    deste.pop(rastgele2)
oyuncu1puan=0
oyuncu2puan=0

print("1.Oyuncunun kartları")
for i in oyuncu1:
    print(i.tur,i.numara)
print("\n2. Oyuncunun kartları")
for i in oyuncu2:
    print(i.tur,i.numara)
for i in range (5):
    if(oyuncu1[i].tur==oyuncu2[i].tur):
        if(oyuncu1[i].numara>oyuncu1[i].numara):
            oyuncu1puan+=5
        else:
            oyuncu2puan+=5
    else:
        if(oyuncu1[i].tur=="Kırmızı"):
            oyuncu1puan+=10
        else:
            oyuncu2puan+=10
if(oyuncu1puan>oyuncu2puan):
    print("Oyunu toplam",oyuncu1puan,"ile 1. oyuncu kazandı.")
elif(oyuncu1puan<oyuncu2puan):
    print("Oyunu toplam",oyuncu2puan,"ile 2. oyuncu kazandı.")
else:
    print("İki oyuncuda toplam",oyuncu1puan,"puan kazandı.Oyun berabere.")
