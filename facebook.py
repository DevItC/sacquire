import os
import requests
import json
from selenium import webdriver


def get_link(driver):
	try:
		elem = driver.find_element_by_xpath("//div[@class='widePic']/div").get_attribute("data-store")
		link = json.loads(elem)["src"]
		# driver.get(link)
		dirname = "videos"
	except:
		elem = driver.find_elements_by_class_name("sec")
		link = elem[1].get_attribute("href")
		# driver.get(link)
	dirname = "images"
	# driver.close()
	title = link.split("?")[0].split("/")[-1]
	return [title, link]

def download(driver):
    try:
        elem = driver.find_element_by_xpath("//div[@class='widePic']/div").get_attribute("data-store")
        link = json.loads(elem)["src"]
        # driver.get(link)
        dirname = "videos"
    except:
        elem = driver.find_elements_by_class_name("sec")
        link = elem[1].get_attribute("href")
        # driver.get(link)
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

def get_preview(driver):
	try:
		elem = driver.find_element_by_xpath("//div[@class='widePic']/div/i").get_attribute("style")
		url_type = "video"
	except:
		url_type = "image"
		elem = driver.find_elements_by_xpath("//div[@id='page']//i")[2].get_attribute('style')

	# print (elem)
	# print ()
	url = elem.split("\"")[1]
	return [url_type, url]

def open_link(url):
	options = webdriver.ChromeOptions()
	options.add_argument("headless")
	options.add_argument('--no-sandbox')
	driver = webdriver.Chrome()
	return driver
	


def main():
    url = input("[*] Enter file URL: ")
    driver = open_link(url)
    url = "m".join(url.split("www"))
    driver.get(url)

    preview = get_preview(driver)
    print (preview)
    link = get_link(driver)
    # print("[*] File saved as {}".format(filename))
    print (link)



if __name__ == "__main__":
    main()
