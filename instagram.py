import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download(driver):
	try:
		elem = driver.find_element_by_class_name('_l6uaz').get_attribute("src")
		link = elem
		dirname = "videos"
	except:
		elem = driver.find_element_by_class_name('_2di5p').get_attribute('src')
		link = elem
		dirname = "images"
	driver.close()

	res = requests.get(link)
	res.raise_for_status()
	title = link.split("/")[-1]

	if not os.path.isdir(dirname):
		os.makedirs(dirname)

	with open(os.path.join(dirname, title), "wb") as file:
		for chunk in res.iter_content(100000):
			file.write(chunk)

	return os.path.join(dirname, title)



def get_preview(driver):
	try:
		element = driver.find_element_by_class_name('_l6uaz').get_attribute("poster")
		url = element
		url_type = "video"
	except:
		url_type = "image"
		element = driver.find_element_by_class_name('_2di5p').get_attribute("srcset")
		url = elememt.split(".jpg")[0] + ".jpg"
	return [url_type, url]
		

def open_link(url):
	options = webdriver.ChromeOptions()
	options.add_argument("headless")
	options.add_argument('--no-sandbox')
	driver = webdriver.Chrome()
	driver.get(url)
	return driver

def main():
    url = input("[*] Enter URL for picture/video: ")
    driver = open_link(url)
    
    preview = get_preview(driver)
    print (preview)

    link = download(driver)


if __name__ == "__main__":
    main()
