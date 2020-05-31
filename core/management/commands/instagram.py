from selenium import webdriver

class Selenium(object):

    def __init__(self):
        self.url = 'https://www.instagram.com/coachdefracassos/'
        firefox = webdriver.Chrome(executable_path='./chromedriver')
        firefox.get(self.url)

selenium = Selenium()