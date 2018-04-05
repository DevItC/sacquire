import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_link(url):


def preview(url):
	url_token = url.split('/')[4]
	return "https://www.instagram.com/p/{}/".format(url_token)

def main():
    url = input("[*] Enter URL for picture/video: ")
    image_url = preview(url)


if __name__ == "__main__":
    main()
