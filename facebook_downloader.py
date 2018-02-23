import requests, bs4, os
from selenium import webdriver

link = "https://m.facebook.com/479753488786510/photos/a.480062335422292.1073741828.479753488786510/1616462925115555/"

driver = webdriver.Chrome()
driver.get(link)

elem = driver.find_elements_by_class_name("sec")
image_link = elem[1].get_attribute("href")

print(image_link)


res = requests.get(image_link)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

imageFile = open("image.jpg", 'wb')

for chunk in res.iter_content(100000):
    imageFile.write(chunk)

imageFile.close()

