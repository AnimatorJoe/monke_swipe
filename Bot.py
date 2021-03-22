from selenium import webdriver
from time import sleep
from login_cred import fb_username, fb_password

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def fb_ogin(self):
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
        
    def swipe_right(self):
        return
    
    def swipe_left(self):
        return


b = Bot()
b.fb_login()
