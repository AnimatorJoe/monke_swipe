from selenium import webdriver
from time import sleep
from login_cred import fb_username, fb_password
from heuristics import always_true, filter_blocked, favored_only, favored_and_not_blocked
from math import inf
from config import verbose
import random
import sys

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    # automated fb login
    def fb_login(self):
        # load webpage
        self.driver.get("http://www.tinder.com")
        self.driver.set_window_size(960, 720)

        sleep(2)

        # click on login button
        login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        login_btn.click()
        sleep(2)

        # open fb login popup
        fb_login_option = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
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

    # swipe right
    def swipe_right(self):
        right_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        right_btn.click()
    
    # swipe left
    def swipe_left(self):
        left_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
        left_btn.click()

    # swipe right inf times unconditional
    def swipe_right_inf_times_unconditional(self):
        self.swipe_on(always_true, inf)

    # swipe right x times unconditional
    def swipe_right_x_times(self, x):
        self.swipe_on(always_true, x)

    # swipe inf times on favored_and_not_blocked
    def swipe_right_inf_times_suboptimal(self):
        self.swipe_on(favored_and_not_blocked, inf)

    # swipes on times number of profiles and only swiping right when heuristic function returns true
    def swipe_on(self, heuristic, times):
        count = 1
        while (count <= times or times == inf):

            rand_wait = random.uniform(0, 1.5)
            sleep(rand_wait)

            favorable = True
            p = {}

            try:
                p = self.get_profile()
                favorable = heuristic(p)
            except Exception:
                pass

            try:
                if favorable:
                    if (verbose):
                        print("swipped right on")
                        print(p)
                    self.swipe_right()
                else:
                    if (verbose):
                        print("swipped left on")
                        print(p)
                    self.swipe_left()
                count += 1
            except Exception as e:
                print('Unable to swipe:')
                if (verbose):
                    print(str(e))

                self.close_popup('//*[@id="t-1483503441"]/div/div/div[2]/button[2]')


    # close popup
    def close_popup(self, xpath):
        btn = self.driver.find_element_by_xpath(xpath)
        btn.click()

    # returns profile of current profile as a dict
    def get_profile(self):
        # expand profile
        expand_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div[3]/button')
        expand_btn.click()

        # read profile
        dict = {}
        try:
            bio_container = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[2]/div')
            dict['bio'] = bio_container.text
        except Exception:
            pass
        
        try:
            info_container = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]')
            dict['info'] = info_container.text
        except Exception:
            pass
        
        print("parsed profile entry")
        print(dict)

        # close profile
        close_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a')
        close_btn.click()

        sleep(0.5)

        return dict

    # quit
    def quit(self):
        self.driver.quit()
        sys.exit()

b = Bot()
b.fb_login()

# run automated processes in the console
# ex: b.swipe_right_inf_times()
# the above is an example that will commence infinite swiping
