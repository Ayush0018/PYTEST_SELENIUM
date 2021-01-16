from utils.util import GenericFunctions as GF


class BrowserWindows:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/browser-windows"
        self.new_tab_bttn_xpath = "//*[@id='tabButton']"
        self.new_win_bttn_xpath = "//*[@id='windowButton']"
        self.new_win_msg_bttn_xpath = "//*[@id='messageWindowButton']"

    def launch_url(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            GF.log_exception_details(e)

    def click_new_tab(self):
        try:
            self.driver.find_element_by_xpath(self.new_tab_bttn_xpath).click()
        except Exception as e:
            GF.log_exception_details(e)

    def click_new_win(self):
        try:
            self.driver.find_element_by_xpath(self.new_win_bttn_xpath).click()
        except Exception as e:
            GF.log_exception_details(e)

    def click_new_winmsg(self):
        try:
            self.driver.find_element_by_xpath(self.new_win_msg_bttn_xpath).click()
        except Exception as e:
            GF.log_exception_details(e)
