class GenericFunctions:
    """
    This class contains generic functions that can be used across the Framework
    Author - Ayush Tewari
    Modified Date - 10/01/2021
    """

    @staticmethod
    def whoami():
        """:return: File and Function names that calls this function """
        import inspect
        return inspect.stack()[1][3]

    @staticmethod
    def current_time():
        from datetime import datetime
        return datetime.now().strftime("%d%m%Y_%H%M%S")
