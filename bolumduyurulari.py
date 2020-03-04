#Çanakkale Onsekiz Mart Üniversite Bilgisayar Mühendisliği bölümünün internet sitesinden duyuruları çeker.
import requests
from bs4 import BeautifulSoup
link = "http://ce.muhendislik.comu.edu.tr/arsiv/duyurular"
icerik = requests.get(link)
icerik = icerik.content
icerik=BeautifulSoup(icerik,"html.parser")
icerik = icerik.find_all("td")
i=1
while(i<len(icerik)):
    print(icerik[i].text)
    i+=4
