import time

import pytest

from Pages.Element import Element


@pytest.mark.usefixtures("test_setup")
class TestDemoqa():
    try:
        def test_fill_form(self):
            elem_pg = Element(self.driver)
            elem_pg.launch_webpage()
            elem_pg.click_to_text_box_element()
            elem_pg.enter_full_name()
            elem_pg.enter_email_id()
            elem_pg.enter_current_address()
            elem_pg.enter_permanent_address()
            time.sleep(5)
            elem_pg.click_submit_button()
    except Exception as e:
        print("Exception Type: " + str(e.__class__.__name__))
        print("Exception Message" + str(e))
