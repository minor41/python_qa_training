from selenium import webdriver
from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/index.php") and
                len(wd.find_elements_by_xpath("//img[@alt='Address book']")) > 0):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()