from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AlertsPromptsConfirmations:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/alerts"
        self.alert_bttn_xpath = "//*[@id='alertButton' and @type='button' and text()='Click me']"
        self.alert_delay_xpath = "//*[@id='timerAlertButton' and @type='button' and text()='Click me']"
        self.alert_confirm_xpath = "//*[@id='confirmButton' and @type='button' and text()='Click me']"
        self.alert_prompt_xpath = "//*[@id='promtButton' and @type='button' and text()='Click me']"
        self.confirmation_msg_xpath = "//*[@id='confirmResult']"

    def launch_url(self):
        self.driver.get(self.url)

    def accept_alert(self):
        self.driver.find_element_by_xpath(self.alert_bttn_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        text = alert.text
        alert.accept()

    def accept_delayed_alert(self):
        self.driver.find_element_by_xpath(self.alert_delay_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        text = alert.text
        print("Text in Alert Box" + text)
        alert.accept()

    def accept_confirmation(self):
        self.driver.find_element_by_xpath(self.alert_confirm_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        text_msg = self.driver.find_element_by_xpath(self.confirmation_msg_xpath).text
        print(text_msg)

    def dismiss_confirmation(self):
        self.driver.find_element_by_xpath(self.alert_confirm_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert.dismiss()
        text_msg = self.driver.find_element_by_xpath(self.confirmation_msg_xpath).text
        print(text_msg)

    def prompt_confirmation(self):
        self.driver.find_element_by_xpath(self.alert_prompt_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert.send_keys("Ayush")
        print("Entered Value in prompt")
        alert.accept()
        print("Prompt Accepted")

    def prompt_dismiss(self):
        self.driver.find_element_by_xpath(self.alert_prompt_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert.dismiss()
        print("Prompt cancelled")
