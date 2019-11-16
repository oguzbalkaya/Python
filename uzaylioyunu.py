import random
class Dunyali():
    def __init__(self,savunma):
        self.savunma=savunma
class Asker(Dunyali):
    def __init__(self,silahgucu,savunma):
        super().__init__(savunma)
        self.silahgucu=silahgucu
    def gucHesapla(self):
        return self.savunma*self.silahgucu

class Ciftci(Dunyali):
    def __init__(self,urunsayisi,savunma):
        super().__init__(savunma)
        self.urunsayisi=urunsayisi
    def gucHesapla(self):
        return self.urunsayisi
class Uzayli():
    def __init__(self,savunma):
        self.savunma=savunma
class Cyborg(Uzayli):
    def __init__(self,savunma,lazergucu):
        super().__init__(savunma)
        self.lazergucu=lazergucu
    def gucHesapla(self):
        return self.lazergucu*self.savunma
class Madenci(Uzayli):
    def __init__(self,savunma,madensayisi):
        super().__init__(savunma)
        self.madensayisi=madensayisi
    def gucHesapla(self):
        return self.madensayisi
dunyalilar=[]
uzaylilar=[]
for i in range (500):
    if(random.randint(1,2)==1):
        dunyalilar.append(Asker(random.randint(1,11),random.randint(1,11)))
    else:
        dunyalilar.append(Ciftci(random.randint(1,11),random.randint(1,11)))

    if(random.randint(1,2)==1):
        uzaylilar.append(Cyborg(random.randint(1,11),random.randint(1,11)))
    else:
        uzaylilar.append(Madenci(random.randint(1,11),random.randint(1,11)))

uzaylilaringucu=0
dunyalilaringucu=0
for i in range(500):
    uzaylilaringucu+=uzaylilar[i].gucHesapla()
    dunyalilaringucu+=dunyalilar[i].gucHesapla()
print("Dünyalıların toplam gücü : ",dunyalilaringucu,"\nUzaylıların toplam gücü",uzaylilaringucu)
if(uzaylilaringucu>dunyalilaringucu):
    print("Uzaylılar kazandı")
else:
    print("Dünyalılar kazandı")
