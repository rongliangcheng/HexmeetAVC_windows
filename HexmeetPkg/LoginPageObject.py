import uiautomation as auto
from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class UserLogin:
    def __init__(self):
        self.hjt_windows = HexmeetWindowSingleton().getHexmeetWindow()
        self.login_windows = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLoginDlg")
        self.login_page = self.login_windows.CustomControl(searchDepth=1, AutomationId="CLoginDlg.m_pStackedWgtContent")

    def go_to_login_page(self):
        self.hjt_windows.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar")\
            .ImageControl(searchDepth=3, AutomationId="CHomeDlg.m_pWgtOperationBar.m_pWgtLoginUserInfo.horizontalWidget.m_pLblAvatar").Click()
        self.hjt_windows.WindowControl(searchDepth=1, ClassName="ev_app::views::CMyInfoDlg").ButtonControl(searchDepth=2, Name="退出登录").Click()

    def fill_in_server_address(self, server_address):
        server_address_edit = self.login_page.EditControl(searchDepth=3, AutomationId="CLoginDlg.m_pStackedWgtContent.CLoginInfoForm.verticalWidget_3.m_pEditServer")
        server_address_edit.SendKeys("{BACK}"*40)
        server_address_edit.SendKeys(server_address)

    def fill_in_account(self, accout):
        accout_edit = self.login_page.EditControl(searchDepth=3, AutomationId="CLoginDlg.m_pStackedWgtContent.CLoginInfoForm.verticalWidget_4.m_pEditAccount")
        accout_edit.SendKeys("{BACK}"*40)
        accout_edit.SendKeys(accout)

    def fill_in_password(self, password):
        password_edit = self.login_page.EditControl(searchDepth=3, AutomationId="CLoginDlg.m_pStackedWgtContent.CLoginInfoForm.verticalWidget_5.m_pEditPassword")
        password_edit.SendKeys("{BACK}"*40)
        password_edit.SendKeys(password)

    def user_login_commit(self):
        self.login_page.ButtonControl(searchDepth=3, Name="登录").Click()

    def login_fail_commit(self):
        self.login_windows.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(searchDepth=3, Name="确定").Click()
