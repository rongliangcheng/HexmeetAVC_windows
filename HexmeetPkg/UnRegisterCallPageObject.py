import uiautomation as auto
from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class UnRegisterCall:
    def __init__(self):
        self.hjt_windows = HexmeetWindowSingleton().getHexmeetWindow()
        self.login_windows = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLoginDlg")
        self.login_page = self.login_windows.CustomControl(searchDepth=1, AutomationId="CLoginDlg.m_pStackedWgtContent")

    def go_to_unregister_call_page(self):
        self.hjt_windows.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar") \
            .ImageControl(searchDepth=3, AutomationId="CHomeDlg.m_pWgtOperationBar.m_pWgtLoginUserInfo.horizontalWidget.m_pLblAvatar").Click()
        self.hjt_windows.WindowControl(searchDepth=1, ClassName="ev_app::views::CMyInfoDlg").ButtonControl(searchDepth=2, Name="退出登录").Click()
        self.login_windows.ButtonControl(searchDepth=2, Name="返回").Click()
        self.login_page.ButtonControl(searchDepth=3, Name="加入会议").Click()

    def fill_in_server_address(self, server_address):
        server_address_edit = self.login_page.EditControl(searchDepth=3, AutomationId="CLoginDlg.m_pStackedWgtContent.CLoginJoinConfForm.verticalWidget.m_pEditServer")
        server_address_edit.SendKeys("{BACK}" * 40)
        server_address_edit.SendKeys(server_address)

    def fill_in_conference_id(self, conference_id):
        """暂时改变不了值"""
        self.login_windows.TextControl(searchDepth=2, Name="加入会议").Click()
        x, y = auto.GetCursorPos()
        # Normal PC auto.Click(x + 55, y + 95)
        # Hihg DPI
        auto.Click(x + 45, y + 75)
        auto.SendKeys("{BACK}" * 40)
        auto.SendKeys(conference_id)
        # conference_id_edit = self.login_page.ComboBoxControl(searchDepth=3, AutomationId="CLoginDlg.m_pStackedWgtContent.CLoginJoinConfForm.verticalWidget.m_pCmbBoxConfNumber")
        # conference_id_edit.SendKeys("{BACK}" * 40)
        # conference_id_edit.SendKeys(conference_id)

    def append_password(self, password):
        self.login_windows.TextControl(searchDepth=2, Name="加入会议").Click()
        x, y = auto.GetCursorPos()
        # Normal PC auto.Click(x + 55, y + 95)
        # Hihg DPI
        auto.Click(x + 45, y + 75)
        auto.SendKeys(password)

    def fill_in_display_name(self, display_name):
        display_name_edit = self.login_page.EditControl(searchDepth=3, AutomationId="CLoginDlg.m_pStackedWgtContent.CLoginJoinConfForm.verticalWidget.m_pEditDisplayName")
        display_name_edit.SendKeys("{BACK}" * 40)
        display_name_edit.SendKeys(display_name)

    def fill_in_password(self, password):
        fill_in_password = auto.WindowControl(searchInterval=1, ClassName="ev_app::views::CInputPasswordWidget").GroupControl(searchDepth=1, AutomationId="CInputPasswordWidget.verticalWidget_2") \
            .EditControl(searchDepth=1, AutomationId="CInputPasswordWidget.verticalWidget_2.m_pInputPasswordEdit")
        fill_in_password.Click()
        fill_in_password.SendKeys(password + "{ENTER}")

    def change_microphone_setting(self):
        self.login_page.CheckBoxControl(searchDepth=3, Name="关闭麦克风").Click()

    def change_camera_setting(self):
        self.login_page.CheckBoxControl(searchDepth=3, Name="关闭摄像头").Click()

    def user_join_commit(self):
        self.login_page.ButtonControl(searchDepth=3, Name="加入").Click()

    def login_fail_commit(self):
        self.login_windows.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(searchDepth=3, Name="确定").Click()

    def fill_in_conference_password(self, password):
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CInputPasswordWidget").EditControl(searchDepth=2, AutomationId="CInputPasswordWidget.verticalWidget_2.m_pInputPasswordEdit") \
            .SendKeys(password + "{ENTER}")

    def login_from_unregister_call_page(self):
        self.login_windows.ButtonControl(searchDepth=2, Name="返回").Click()
        sleep(1)
        self.login_windows.ButtonControl(searchDepth=4, Name="登录").Click()
        sleep(1)
        self.login_windows.ButtonControl(searchDepth=4, Name="登录").Click()

    def close_hjt(self):
        self.login_windows.GroupControl(searchDepth=1, AutomationId="CLoginDlg.m_pWgtTitlebar").ButtonControl(searchDepth=1, AutomationId="CLoginDlg.m_pWgtTitlebar.m_pBtnClose").Click()
