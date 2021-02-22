from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from HexmeetPkg.joinAMeetingPageObject import JoinAMeeting
import logging
import uiautomation as auto
from time import sleep

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

favorite_user = "hexautotest5"


class ReserveMeeting:

    def __init__(self):
        self.hexMeetWindow = HexmeetWindowSingleton().getHexmeetWindow()
        self.reserve_meeting_page = self.hexMeetWindow.GroupControl(searchDepth=1,
                                                                    AutomationId="CHomeDlg.m_pWgtContext")
        self.participants_page = self.reserve_meeting_page.GroupControl(searchDepth=2,
                                                                        AutomationId="CHomeDlg.m_pWgtContext.m_pStackedWgtContent.CWebBrowserWrapperForm")
        self.join_meeting_page = self.hexMeetWindow.WindowControl(searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg")

    def __start_time_pos(self):
        self.hexMeetWindow.TextControl(searchDepth=10, Name="开始时间").Click()
        return auto.GetCursorPos()

    def __meeting_duration_pos(self):
        self.hexMeetWindow.TextControl(searchDepth=10, Name="会议时长").Click()
        return auto.GetCursorPos()

    def go_to_meeting_page(self):
        log.info("Go to the meeting page")
        self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar").ListControl(
            searchDepth=2, ClassName="ev_app::custom_controls::CHomeMenuListView").Click()
        x, y = auto.GetCursorPos()
        # auto.Click(x, y - 70)
        # high DPI
        auto.Click(x, y - 55)
        self.click_upgrade_notice

    def reserve_meeting_from_panel(self):
        log.info("Reserve  meeting from panel")
        self.go_to_meeting_page()
        sleep(2)
        self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").TextControl(
            searchDepth=9, Name="预约会议").Click()

    def create_now_meeting_from_panel(self):
        log.info("From panel, choose immediate meeting")
        self.go_to_meeting_page()
        sleep(2)
        self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").TextControl(
            searchDepth=8, Name="立即会议").Click()

    def choose_date(self):
        log.info("Change date")
        x, y = self.__start_time_pos()
        auto.Click(x + 160, y)

    def choose_time(self):
        log.info("Change time")
        x, y = self.__start_time_pos()
        auto.Click(x + 250, y)
        auto.SetCursorPos(x + 250, y + 80)
        auto.WheelDown(3)
        auto.Click(x + 500, y)

    def choose_now(self):
        log.info("Choose now")
        self.participants_page.TextControl(searchDepth=8, Name="现在").Click()

    def choose_duration(self):
        log.info("Change duration")
        x, y = self.__meeting_duration_pos()
        auto.Click(x + 160, y)
        auto.SetCursorPos(x + 120, y + 100)
        auto.WheelDown(3)
        sleep(1)
        auto.Click(x + 500, y)

    def fill_password(self, password):
        log.info("Fill in password:" + str(password))
        self.reserve_meeting_page.EditControl(searchDepth=9, Name="请输入会议密码").SendKeys(password)

    def same_layout(self):
        log.info("Choose same layout")
        self.reserve_meeting_page.TextControl(searchDepth=12, Name="相同分屏").Click()

    def auto_redial(self):
        log.info("Choose auto redial")
        self.reserve_meeting_page.TextControl(searchDepth=12, Name="自动重拨").Click()

    def mute_after_join(self):
        log.info("choose mute after join")
        self.reserve_meeting_page.TextControl(searchDepth=12, Name="入会自动静音").Click()

    def fill_meeting_notes(self, note):
        log.info("Fill in the meeting notes")
        self.reserve_meeting_page.EditControl(searchDepth=11, Name="请输入会议备注").SendKeys(note)

    def choose_favorite_contact(self):
        log.info("Choose favorite contact")
        self.reserve_meeting_page.TextControl(searchDepth=7, Name="添加与会者(0)").Click()
        self.reserve_meeting_page.TextControl(searchDepth=10, Name=favorite_user).Click()
        self.reserve_meeting_page.TextControl(searchDepth=8, Name="确定").Click()

    def choose_participants(self, name):
        log.info("Find a participant")
        self.reserve_meeting_page.TextControl(searchDepth=7, Name="添加与会者(0)").Click()
        self.participants_page.RadioButtonControl(searchDepth=8, Name="组织机构").Click()
        self.participants_page.EditControl(searchDepth=11, Name="请输入名称").SendKeys(name + "{ENTER}")
        sleep(1)
        self.participants_page.TextControl(searchDepth=10, Name="中创软件测试中心").Click()
        sleep(1)
        self.participants_page.TextControl(searchDepth=6, Name="确定").Click()

    def reserve_confirm(self):
        log.info("Confirm reservation")
        self.participants_page.ButtonControl(searchDepth=5, Name="确定").Click()

    def delete_reserve_meeting(self):
        log.info("Delete the reserved meeting")
        self.reserve_meeting_page.CustomControl(searchDepth=12, Name="删除会议").Click()
        sleep(2)
        self.reserve_meeting_page.ButtonControl(searchDepth=7, Name="确认 ").Click()

    def edit_reserve_meeting(self):
        log.info("Edit the reserved meeting")
        self.participants_page.TextControl(searchDepth=10, Name="编辑会议").Click()
        sleep(1)
        self.participants_page.ButtonControl(searchDepth=5, Name="确定").Click()

    def return_from_reserve_meeting(self):
        """无法取得返回的控件，只能通过像素点"""
        log.info("Go back the main reserve meeting page")
        self.participants_page.TextControl(searchDepth=7, Name="会议基本信息:").Click()
        x, y = auto.GetCursorPos()
        auto.Click(x - 60, y - 60)

    def terminate_now_meeting(self):
        log.info("Terminate the meeting")
        self.participants_page.CustomControl(searchDepth=10, Name="结束会议").Click()
        sleep(1)
        self.reserve_meeting_page.ButtonControl(searchDepth=7, Name="确认 ").Click()

    def create_a_now_meeting_and_join(self):
        log.info("Create an immediate meeting and join")
        self.go_to_meeting_page()
        self.reserve_meeting_page.TextControl(searchDepth=8, Name="立即会议").Click()
        sleep(3)
        self.reserve_confirm()
        sleep(2)
        self.return_from_reserve_meeting()
        JoinAMeeting().join_now_meeting_from_reserved_item()

    def meeting_control_after_create(self):
        log.info("Go to meeting control")
        self.participants_page.TextControl(searchDepth=8, Name="进入会控").Click()

    def meeting_control_from_panel(self):
        log.info("Go to meeting control from panel")
        self.participants_page.CustomControl(searchDepth=10, Name="控制会议").Click()

    def clear_reserved_meeting(self):
        log.info("Cleared un_deleted meetings")
        self.click_upgrade_notice
        while self.reserve_meeting_page.CustomControl(searchDepth=12, Name="结束会议").Exists(1):
            self.reserve_meeting_page.CustomControl(searchDepth=12, Name="结束会议").Click()
            sleep(2)
            self.reserve_meeting_page.ButtonControl(searchDepth=8, Name="确认 ").Click()
            sleep(3)

    def invite_others_control_now_meeting(self, name):
        sleep(1)
        self.reserve_meeting_page.ButtonControl(searchDepth=8, Name="邀请").Click()
        sleep(1)
        self.reserve_meeting_page.EditControl(searchDepth=11, Name="输入用户/终端名称").SendKeys(name)
        sleep(1)
        self.reserve_meeting_page.ButtonControl(searchDepth=7, Name="< 返回").Click()
        sleep(1)
        self.reserve_meeting_page.ButtonControl(searchDepth=7, Name="< 返回").Click()

    def click_upgrade_notice(self):
        sleep(2)
        try:
            HexmeetWindowSingleton().getHexmeetWindow().GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").ButtonControl(searchDepth=8, Name="确定").Click()
        except:
            print()
