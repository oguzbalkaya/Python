#imdb top 250
import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top"
response = requests.get(url)
icerik = response.content
soup = BeautifulSoup(icerik,"html.parser")
isimler = soup.find_all("td",{"class":"titleColumn"})
oylar = soup.find_all("td",{"class":"ratingColumn imdbRating"})
yeni = zip(isimler,oylar)
for i,j in yeni:
    baslik = i.text
    puan = j.text
    baslik = baslik.strip()
    puan = puan.strip()
    baslik = baslik.replace("\n","")
    puan = puan.replace("\n","")
    print("Film Adı : "+baslik+" Puanı : "+puan)

