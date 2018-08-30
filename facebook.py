import json
import os
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class SAcquire:
    def __init__(self, url=None):
        self.driver = self.__webdriver()
        self.__media = None
        if url:
            self.URL = url

    @staticmethod
    def __webdriver():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        return driver

    @property
    def URL(self):
        return self.__url

    @URL.setter
    def URL(self, value):
        self.data = self.process(value)
        self.__url = value

    @property
    def media(self):
        if self.data['media_type'] == 'private':
            return 'Can not download private media!'
        if not self.__media:
            self.__download()
        return self.__media

    def __download(self):
        res = requests.get(self.data['media_url'])
        res.raise_for_status()

        dirname = self.data['media_type']
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        with open(os.path.join(dirname, self.data['media_title']), 'wb') as file:
            for chunk in res.iter_content(100000):
                file.write(chunk)
        self.__media = os.path.join(dirname, self.data['title'])


class FBAcquire(SAcquire):
    def process(self, url):
        url = 'm'.join(url.split('www'))
        self.driver.get(url)
        data = {}
        try:
            data['media_type'] = self.driver.find_element_by_xpath('//meta[@property="og:type"]').get_property('content')
            data['media_preview'] = self.driver.find_element_by_xpath('//meta[@property="og:image"]').get_property(
                'content')
            data['media_url'] = self.driver.find_element_by_xpath('//meta[@property="og:video"]').get_property('content')
        except NoSuchElementException:
            try:
                data['media_preview'] = self.driver.find_elements_by_xpath('//div[@id="page"]//i')[2].get_attribute('style').split('"')[1]
            except IndexError:
                data['media_type'] = 'private'
                return data
            data['media_type'] = 'image'
            data['media_url'] = self.driver.find_element_by_xpath('//meta[@property="og:image"]').get_property(
                'content')

        data['media_title'] = self.driver.find_element_by_xpath('//meta[@property="og:title"]').get_property('content')
        return data


def main():
    url = input('[*] Enter file URL: ')
    driver = open_link(url)

    preview = get_preview(driver)
    print(preview)
    link = get_link(driver)
    print(link)
    # print("[*] File saved as {}".format(filename))
    print(link)


if __name__ == "__main__":
    main()
