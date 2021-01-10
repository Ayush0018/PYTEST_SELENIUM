from selenium.webdriver.common.action_chains import ActionChains

from utils.util import GenericFunctions as GF


class Element:
    func_name = GF.whoami
    current_time = GF.current_time

    def __init__(self, driver):
        self.driver = driver
        self.text_box_elem_xpath = "//*[@id='item-0']/span[contains(text(),'Text Box1')]"
        self.full_name_xpath = "//*[@id='userName']"
        self.email_id_xpath = "//*[@id='userEmail']"
        self.current_address_id = "currentAddress"
        self.permanent_address_id = "permanentAddress"
        self.submit_button_xpath = "//*[@id='submit' and @type='button']"
        self.url = "https://demoqa.com/text-box"

    def launch_webpage(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            print("Exception Type: " + str(e.__class__.__name__))
            print("Exception Message" + str(e))
            self.driver.get_screenshot_as_file(r"C:\Users\lenovo\PycharmProjects\SELENIUM\Screenshots\Exception_" +
                                               str(GF.whoami()) + "_" + str(GF.current_time()) + ".png")
            raise e

    def click_to_text_box_element(self):
        try:
            self.driver.find_element_by_xpath(self.text_box_elem_xpath).click()
        except Exception as e:
            print("Exception Type: " + str(e.__class__.__name__))
            print("Exception Message" + str(e))
            print("Exception Message" + str(e))
            self.driver.get_screenshot_as_file(r"C:\Users\lenovo\PycharmProjects\SELENIUM\Screenshots\Exception_" +
                                               str(GF.whoami()) + "_" + str(GF.current_time()) + ".png")
            raise e

    def enter_full_name(self):
        try:
            self.driver.find_element_by_xpath(self.full_name_xpath).send_keys("Ayush Tewari")
        except Exception as e:
            print("Exception Type: " + str(e.__class__.__name__))
            print("Exception Message" + str(e))
            self.driver.get_screenshot_as_file(r"C:\Users\lenovo\PycharmProjects\SELENIUM\Screenshots\Exception_" +
                                               str(GF.whoami()) + "_" + str(GF.current_time()) + ".png")
            raise e

    def enter_email_id(self):
        try:
            self.driver.find_element_by_xpath(self.email_id_xpath).send_keys("abc@xyz.com")
        except Exception as e:
            print("Exception Type: " + str(e.__class__.__name__))
            print("Exception Message" + str(e))
            self.driver.get_screenshot_as_file(r"C:\Users\lenovo\PycharmProjects\SELENIUM\Screenshots\Exception_" +
                                               str(GF.whoami()) + "_" + str(GF.current_time()) + ".png")
            raise e

    def enter_current_address(self):
        try:
            self.driver.execute_script(
                "document.getElementById('currentAddress').value='Address Line 1 Address Line 2 City Line 1'")
        except Exception as e:
            print("Exception Type: " + str(e.__class__.__name__))
            print("Exception Message" + str(e))
            self.driver.get_screenshot_as_file(r"C:\Users\lenovo\PycharmProjects\SELENIUM\Screenshots\Exception_" +
                                               str(GF.whoami()) + "_" + str(GF.current_time()) + ".png")
            raise e

    def enter_permanent_address(self):
        try:
            self.driver.execute_script(
                "document.getElementById('permanentAddress').value='Address Line 1 Address Line 2 City Line 1'")
        except Exception as e:
            print("Exception Type: " + str(e.__class__.__name__))
            print("Exception Message" + str(e))
            self.driver.get_screenshot_as_file(r"C:\Users\lenovo\PycharmProjects\SELENIUM\Screenshots\Exception_" +
                                               str(GF.whoami()) + "_" + str(GF.current_time()) + ".png")
            raise e

    def click_submit_button(self):
        try:
            element = self.driver.find_element_by_xpath(self.submit_button_xpath)

            # self.driver.execute_script("arguments[0].click();", element)

            # self.driver.find_element_by_xpath(self.submit_button_xpath).click()

            # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            # self.driver.find_element_by_xpath(self.submit_button_xpath).click()

            ActionChains(self.driver).move_to_element(element).click(element).perform()

        except Exception as e:
            print("Exception Type: " + str(e.__class__.__name__))
            print("Exception Message" + str(e))
            self.driver.get_screenshot_as_file(r"C:\Users\lenovo\PycharmProjects\SELENIUM\Screenshots\Exception_" +
                                               str(GF.whoami()) + "_" + str(GF.current_time()) + ".png")
            raise e
