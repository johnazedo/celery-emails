from selenium import webdriver
import os

class Selenium(object):

    def __init__(self):
        self.url = 'https://www.instagram.com/coachdefracassos/'
        firefox = webdriver.Chrome(executable_path='core/management/commands/chromedriver')
        firefox.get(self.url)

        elem = firefox.find_element_by_tag_name('img')
        attribute = elem.get_attribute('src').replace('?', '\?').replace('&', '\&').replace('=', '\=')
        command = f'wget --output-document=image.jpg {attribute}'
        os.system(command)

selenium = Selenium()