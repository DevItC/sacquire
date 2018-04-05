import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download_link(url):
	driver = webdriver.Chrome()
	driver.get('https://www.ssyoutube.com/'+url.split('/')[-1])
	wait = WebDriverWait(driver, 30)
	wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'link-download')))
	link = driver.find_element_by_class_name('link-download').get_attribute('href')
	driver.close()
	return link



def preview(url):
	video_id = url.split('=')[-1]
	return "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(video_id)

def get_title(url):
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'lxml')
	elem = soup.select('h1')
	text = elem[1].getText()
	return "".join(text.split("\n"))


def download(url, title):
	if not os.path.isdir("videos"):
		os.makedirs("videos")
	res = requests.get(url)
	with open(os.path.join('videos', title+".mp4"), "wb") as file:
		for chunk in res.iter_content(100000):
			file.write(chunk)
	return os.path.join('videos', title)

def main():
    url = input("[*] Enter file URL: ")
    image_url = preview(url)
    video_url = download_link(url)
    title = get_title(url)
    print ("[*] Downloading song: {}".format(title))
    download(video_url, title)


if __name__ == "__main__":
    main()
