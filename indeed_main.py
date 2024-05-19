from bots.indeed_bot import IndeedBot
from additional.helpers import random_sleep

with IndeedBot(teardown=False) as bot:
    bot.get_jobs("Python Developer")
    bot.reject_cookies()
    bot.iterate_through_page()
    bot.click_next_page()
    bot.close_contact_popup()