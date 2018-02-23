import requests
from selenium import webdriver



def download(url):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=options)

    url = "m".join(url.split("www"))
    driver.get(url)
    elem = driver.find_elements_by_class_name("sec")
    image_link = elem[1].get_attribute("href")
    driver.close()

    res = requests.get(image_link)
    res.raise_for_status()
    title = image_link.split("?")[0].split("/")[-1]
    image_file = open(title, "wb")
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()
    return title


def main():
    url = input("[*] Enter image URL: ")
    filename = download(url)
    print("[*] Image saved as {}".format(filename))


if __name__=="__main__":
	main()
