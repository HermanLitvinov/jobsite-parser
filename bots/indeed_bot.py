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

    def indeed_function_wrapper(self, function, do_sleep=True):
        if do_sleep: random_sleep()
        try:
            function()
        except Exception as e:
            print(e)

    def process_query(self, query: str):
        url_query = query.replace(" ", "+")
        return url_query

    def get_jobs(self, query: str):
        self.get(const.INDEED_URL_CONFABLE.format(query=self.process_query(query)))

    def reject_cookies(self, do_sleep=True):
        funct = lambda: self.find_element(By.ID, "onetrust-reject-all-handler").click()
        self.indeed_function_wrapper(funct, do_sleep)

    def iterate_through_page(self, do_sleep=True):
        if do_sleep: random_sleep()
        postings = self.find_elements(By.ID, "mosaic-provider-jobcards")
        for posting in postings:
            print(posting.text)

    def click_next_page(self, do_sleep=True):
        funct = lambda: self.find_element(By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]').click()
        self.indeed_function_wrapper(funct, do_sleep)

    def close_contact_popup(self, do_sleep=True):
        funct = lambda: WebDriverWait(self, 5)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="schließen"]'))).click()
        self.indeed_function_wrapper(funct, do_sleep)