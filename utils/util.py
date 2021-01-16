class GenericFunctions:
    """
    This class contains generic functions that can be used across the Framework
    Author - Ayush Tewari
    Modified Date - 10/01/2021
    """

    @classmethod
    def generic_func(cls):
        cls.whoami()
        cls.current_time()
        cls.exception_file_lineno()

    @staticmethod
    def whoami():
        """:return: File and Function names that calls this function """
        import inspect
        return inspect.stack()[1][3]


    @staticmethod
    def current_time():
        from datetime import datetime
        return datetime.now().strftime("%d%m%Y_%H%M%S")

    @staticmethod
    def exception_file_lineno():
        """:return: List of Filename and current Line number  """
        import os, sys
        excep_type, excep_obj, excep_tb = sys.exc_info()
        fname = os.path.split(excep_tb.tb_frame.f_code.co_filename)[1]
        return [excep_type, fname, excep_tb.tb_lineno]

    @staticmethod
    def log_exception_details(exception):
        print("==========================An Error has Occurred===========================")
        print(str(exception.__class__.__name__) + " has occurred while execution of script")
        print("Error Description: " + str(exception))
        print("Error Occurred in Module: " + str(GenericFunctions.exception_file_lineno()[1]))
        print("Error Occurred at line number: " + str(GenericFunctions.exception_file_lineno()[2]))
        raise e

    @staticmethod
    def take_screenshot():
        pass
