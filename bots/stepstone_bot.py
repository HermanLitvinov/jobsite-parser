from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bots import constants as const
from additional.helpers import random_sleep

class IndeedBot(webdriver.Chrome):
    def __init__(self, teardown=False):
        chr_options = ChromeOptions()
        chr_options.add_experimental_option("detach", True)
        super(IndeedBot, self).__init__(options=chr_options, service=ChromeService(ChromeDriverManager().install()))
        self.implicitly_wait(10)
        self.maximize_window()
        self.teardown = teardown

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def process_query(self, query: str):
        url_query = query.replace(" ", "-")
        return url_query

    def get_jobs(self, query: str):
        self.get(const.STEPSTONE_URL_CONFABLE.format(query=self.process_query(query)))