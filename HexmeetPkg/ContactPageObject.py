from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from HexmeetPkg.OperateInMeetingPageObject import OperateInMeeting
from HexmeetPkg.Common import CallType
from time import sleep
import uiautomation as auto
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class Contact:
    def __init__(self):
        self.hexMeetWindow = HexmeetWindowSingleton().getHexmeetWindow()
        self.contact_page = self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext")

    def __contact_page_click(self):
        self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar").ListControl(
            searchDepth=2, AutomationId="CHomeDlg.m_pWgtOperationBar.verticalWidget_4.m_pLvMenus").Click()

    def __meeting_page_click(self):
        self.__contact_page_click()
        x, y = auto.GetCursorPos()
        auto.Click(x, y-70)

    def go_to_contact_organization_page_search(self,name):
        self.__meeting_page_click()
        self.__contact_page_click()
        self.contact_page.RadioButtonControl(searchDepth=11, Name="组织机构").Click()
        sleep(1)
        self.contact_page.EditControl(searchDepth=11, Name="请输入名称").SendKeys(name+"{ENTER}")

    def return_from_person_info_page(self):
        log.info("Return from person info page")
        self.contact_page.TextControl(searchDepth=9, Name="用户详情").Click()
        x, y = auto.GetCursorPos()
        auto.Click(x-302, y)

    def call_from_favorite(self, name, call_type=CallType.Video):
        log.info("call_from_favorite")
        self.__meeting_page_click()
        self.__contact_page_click()
        self.contact_page.TextControl(searchDepth=13, Name=name).Click()
        sleep(1)
        operate_in_meeting = OperateInMeeting()
        if call_type == CallType.Video:
            log.info("Video call")
            self.contact_page.TextControl(searchDepth=11, Name="视频呼叫").Click()
            sleep(20)
            operate_in_meeting.hangup_call()
        else:
            log.info("Audio call")
            self.contact_page.TextControl(searchDepth=11, Name="语音呼叫").Click()
            sleep(20)
            operate_in_meeting.audio_only_hangup()
        # self.return_from_person_info_page()



    def call_from_organization(self, name, call_type=CallType.Video):
        log.info("call_from_organization")
        # 点击会议，再点击通讯录，返回通讯录的原始页面
        self.contact_page.TextControl(searchDepth=12, Name="中创软件测试中心").Click()
        sleep(1)
        operate_in_meeting = OperateInMeeting()
        if call_type == CallType.Video:
            log.info("Video call")
            self.contact_page.TextControl(searchDepth=11, Name="视频呼叫").Click()
            sleep(20)
            operate_in_meeting.hangup_call()
        else:
            log.info("Audio call")
            self.contact_page.TextControl(searchDepth=11, Name="语音呼叫").Click()
            sleep(20)
            operate_in_meeting.audio_only_hangup()
        # self.return_from_person_info_page()
