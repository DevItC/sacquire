import requests, bs4, os, webbrowser

# link = "https://www.facebook.com/photo.php?fbid=1788821858089808&set=a.1477983132507017.1073741830.100008860326603&type=3&theater"
link = "https://m.facebook.com/479753488786510/photos/a.480062335422292.1073741828.479753488786510/1616462925115555/"
req = requests.get("https://m.facebook.com/grannyfacts/photos/a.1527687013943008.1073741828.1517259191652457/1753243824720658/")
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text, "html.parser")
elem = soup.select(".sec")

print (len(elem))
image_link = elem[1].get('href')

res = requests.get(image_link)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)

imageFile = open(os.getcwd()+"/photos/"+soup.title.text.split(" ")[0], 'wb')

for chunk in res.iter_content(100000):
    imageFile.write(chunk)

imageFile.close()

