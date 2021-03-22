from selenium import webdriver
from time import sleep
from login_cred import fb_username, fb_password
from math import inf
import random

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    # automated fb login
    def fb_login(self):
        # load webpage
        self.driver.get("http://www.tinder.com")

        sleep(2)

        # click on login button
        login_btn = self.driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        login_btn.click()
        sleep(2)

        # open fb login popup
        fb_login_option = self.driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_login_option.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        # login to fb
        username_field = self.driver.find_element_by_xpath('//*[@id="email"]')
        username_field.send_keys(fb_username)

        password_field = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_field.send_keys(fb_password)

        sleep(2)

        btn_container = self.driver.find_element_by_xpath('//*[@id="buttons"]')
        fb_login_btn = btn_container.find_element_by_name('login')
        fb_login_btn.click()

        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.set_window_size(960, 720)

    # swipe right
    def swipe_right(self):
        right_btn = self.driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        right_btn.click()
    
    # swipe left
    def swipe_left(self):
        left_btn = self.driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
        left_btn.click()

    # swipe right x times unconditional
    def swipe_right_inf_times(self):
        self.swipe_on(lambda _ : True, inf)

    # swipe right x times unconditional
    def swipe_right_x_times(self, x):
        self.swipe_on(lambda _ : True, x)

    # swipes on times number of profiles and only swiping right when heuristic function returns true
    def swipe_on(self, heuristic, times):
        count = 1
        while (count <= times or times == inf):

            rand_wait = random.uniform(1, 3)
            sleep(rand_wait)

            p = self.get_profile()
            _ = self.swipe_right() if heuristic(p) else self.swipe_left()

            count += 1

    # returns profile of current profile as a dict
    def get_profile(self):
        return


b = Bot()
b.fb_login()
