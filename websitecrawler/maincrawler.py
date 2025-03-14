from bs4 import BeautifulSoup

import requests

#bir sitede tıklanan her şeyi bulmak

target_url = "https://atilsamancioglu.com"
found_links = []

def make_request(url):
  response = requests.get(target_url)
  soup = BeautifulSoup(response.text, "html.parser")
  return soup

def crawl(url):
    links = make_request(url)
    for link in links.find_all("a"):
      found_link= link.get("href")
      if found_link:
        if "#" in found_link:
          found_link = found_link.split("#")[0]
        if  target_url in found_link and found_link not in found_links: #bununla her tıklanan şeyi bir defa görürüz.
          found_links.append(found_link)
          print(found_link)
          #recursive, fonksiyon içinde fonksiyon demektir.
          crawl(link) #mesela courses link'e geldi. Bu koda gelince bu sefer courses içine geliyor courses içindeki linkleri belirliyor varsa yazıyor yoksa yazmıyor.

crawl(target_url)
