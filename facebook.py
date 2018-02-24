import os
import requests
import json
from selenium import webdriver



def download(url):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=options)

    url = "m".join(url.split("www"))
    driver.get(url)
    try:
        elem = driver.find_element_by_xpath("//div[@class='widePic']/div").get_attribute("data-store")
        link = json.loads(elem)["src"]
        dirname = "videos"
    except:
        elem = driver.find_elements_by_class_name("sec")
        link = elem[1].get_attribute("href")
        dirname = "images"
    driver.close()

    res = requests.get(link)
    res.raise_for_status()
    title = link.split("?")[0].split("/")[-1]
    
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
        
    with open(os.path.join(dirname, title), "wb") as file:
        for chunk in res.iter_content(100000):
            file.write(chunk)

    return os.path.join(dirname, title)


def main():
    url = input("[*] Enter file URL: ")
    filename = download(url)
    print("[*] File saved as {}".format(filename))


if __name__ == "__main__":
    main()
