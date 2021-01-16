import time

import pytest

from Pages.AlertsPromptsConfirmations import AlertsPromptsConfirmations
from Pages.BrowserWindows import BrowserWindows
from Pages.Frames import Frames
from Pages.TextBoxes import TextBoxes
from utils.util import GenericFunctions as GF


@pytest.mark.usefixtures("test_setup")
class TestDemoqa:

    @pytest.mark.elements
    def test_fill_form(self):
        textbox_pg = TextBoxes(self.driver)
        textbox_pg.launch_webpage()
        textbox_pg.click_to_text_box_element()
        textbox_pg.enter_full_name()
        textbox_pg.enter_email_id()
        textbox_pg.enter_current_address()
        textbox_pg.enter_permanent_address()
        time.sleep(5)
        textbox_pg.click_submit_button()

    @pytest.mark.frames
    def test_select_frame(self):
        frames_pg = Frames(self.driver)
        frames_pg.launch_frames()
        frames_pg.switch_to_frame1()

    @pytest.mark.alerts
    def test_handle_alerts(self):
        alert_pg = AlertsPromptsConfirmations(self.driver)
        alert_pg.launch_url()
        handles1 = self.driver.window_handles
        time.sleep(3)
        alert_pg.accept_alert()
        time.sleep(3)
        handles2 = self.driver.window_handles
        print(handles1, handles2)
        alert_pg.accept_delayed_alert()
        alert_pg.accept_confirmation()
        time.sleep(5)
        alert_pg.dismiss_confirmation()
        time.sleep(5)
        alert_pg.prompt_confirmation()
        time.sleep(5)
        alert_pg.prompt_dismiss()
        time.sleep(5)

    @pytest.mark.browserwin
    def test_handle_browserwin(self):
        try:
            browsrwin_pg = BrowserWindows(self.driver)
            browsrwin_pg.launch_url()
            browsrwin_pg.click_new_tab()
            win_handles = self.driver.window_handles
            time.sleep(5)
            self.driver.switch_to.window(win_handles[0])
            browsrwin_pg.click_new_tab()
            time.sleep(5)
            win_handles = self.driver.window_handles
            self.driver.switch_towindow(win_handles[0])
            time.sleep(5)
            browsrwin_pg.click_new_win()
            win_handles = self.driver.window_handles
            self.driver.switch_to.window(win_handles[-1])
            self.driver.close()
            time.sleep(5)
        except Exception as e:
            GF.log_exception_details(e)
            print(e)
