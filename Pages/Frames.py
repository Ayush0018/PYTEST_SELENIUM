class Frames:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/frames"
        self.iframe1_xpath = "//*[@id='frame1']"
        self.iframe2_xpath = "//*[@id='frame2']"
        self.sample_heading_iframe1_xpath = "//*[@id='sampleHeading']"

    def launch_frames(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            print("Exception Type: " + str(e.__class__.__name__))
            print("Exception Message" + str(e))
            self.driver.get_screenshot_as_file(r"C:\Users\lenovo\PycharmProjects\SELENIUM\Screenshots\Exception_" +
                                               str(GF.whoami()) + "_" + str(GF.current_time()) + ".png")
            raise e

    def switch_to_frame1(self):
        try:
            iframe1 = self.driver.find_element_by_xpath(self.iframe1_xpath)
            self.driver.switch_to.frame(iframe1)
            text1 = self.driver.find_element_by_xpath(self.sample_heading_iframe1_xpath).get_attribute("h1")
            print(text1)

        except Exception as e:
            print("Exception Type: " + str(e.__class__.__name__))
            print("Exception Message" + str(e))
            self.driver.get_screenshot_as_file(r"C:\Users\lenovo\PycharmProjects\SELENIUM\Screenshots\Exception_" +
                                               str(GF.whoami()) + "_" + str(GF.current_time()) + ".png")
            raise e
