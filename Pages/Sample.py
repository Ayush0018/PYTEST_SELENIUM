class SampleClass:

    def __init__(self, driver):
        self.driver = driver
        self.elem_xpath = ""
        self.elem_xpath = ""
        self.elem_xpath = ""
        self.elem_xpath = ""
        self.url = ""

    def func_name(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            print("==========================An Error has Occurred===========================")
            print(str(e.__class__.__name__) + " has occurred while execution of script")
            print("Error Description" + str(e))
            self.driver.get_screenshot_as_file(r"C:\Users\lenovo\PycharmProjects\SELENIUM\Screenshots\Exception_" +
                                               str(GF.whoami()) + "_" + str(GF.current_time()) + ".png")
            print("Error Occurred in Function: " + str(GF.whoami()))
            print("Error Occurred at line number: " + str(GF.exception_file_lineno()[2]))
            raise e
