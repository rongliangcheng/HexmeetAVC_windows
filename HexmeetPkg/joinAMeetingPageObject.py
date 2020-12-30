import uiautomation as auto
from time import sleep
import logging
from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from HexmeetPkg.Common import CallType
from HexmeetPkg.Common import MicStatus
from HexmeetPkg.Common import CameraStatus
from HexmeetPkg.OperateInMeetingPageObject import OperateInMeeting

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class JoinAMeeting:

    def __init__(self):
        # print("__init__")
        self.hexMeetWindow = HexmeetWindowSingleton().getHexmeetWindow()

    def go_to_meeting_page(self):
        log.info("Go to the meeting page")
        self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar").ListControl(
            searchDepth=2, ClassName="ev_app::custom_controls::CHomeMenuListView").Click()
        x, y = auto.GetCursorPos()
        auto.Click(x, y - 70)

    def mute_mic(self, micstatus=MicStatus.MUTE):
        log.info("Mute Umute the Miccrophone")
        join_window = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CHomeDlg").WindowControl(
            searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg")
        mic_checkbox = join_window.CheckBoxControl(searchDepth=2,
                                                   AutomationId="CHomeDlg.CJoinConfDlg.verticalWidget_2.m_pChkBoxDisableMic")
        if micstatus == MicStatus.UMUTE and mic_checkbox.GetTogglePattern().ToggleState == 1:
            mic_checkbox.Click()
        elif micstatus == MicStatus.MUTE and mic_checkbox.GetTogglePattern().ToggleState == 0:
            mic_checkbox.Click()

    def mute_camera(self, camerastatus=CameraStatus.UMUTE):
        log.info("Mute/Umute Camera")
        join_window = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CHomeDlg").WindowControl(
            searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg")
        camera_checkbox = join_window.CheckBoxControl(searchDepth=2,
                                                      AutomationId="CHomeDlg.CJoinConfDlg.verticalWidget_2.m_pChkBoxDisableCamera")
        if camerastatus == CameraStatus.MUTE and camera_checkbox.GetTogglePattern().ToggleState == 0:
            camera_checkbox.Click()
        elif camerastatus == CameraStatus.UMUTE and camera_checkbox.GetTogglePattern().ToggleState == 1:
            camera_checkbox.Click()

    def make_call(self, calltype=CallType.Video, micstatus=MicStatus.UMUTE, camerastatus=CameraStatus.UMUTE):
        log.info("Combination video/Audio call with Mic/Camera with Mute/Umute")
        join_window = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CHomeDlg").WindowControl(
            searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg")
        video_call = join_window.ButtonControl(searchDepth=3,
                                               AutomationId="CHomeDlg.CJoinConfDlg.verticalWidget_2.horizontalWidget.m_pBtnVideoJoin")
        audio_call = join_window.ButtonControl(searchDepth=3,
                                               AutomationId="CHomeDlg.CJoinConfDlg.verticalWidget_2.horizontalWidget.m_pBtnAudioJoin")
        self.mute_mic(micstatus)
        self.mute_camera(camerastatus)

        if calltype == CallType.Video:
            log.info("Video call")
            video_call.Click()
        else:
            log.info("Audio call")
            audio_call.Click()

    def make_call_and_drop(self, calltype=CallType.Video, micstatus=MicStatus.UMUTE, camerastatus=CameraStatus.UMUTE):
        log.info("Combination video/Audio call with Mic/Camera with Mute/Umute")
        join_window = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CHomeDlg").WindowControl(
            searchDepth=1, AutomationId="CHomeDlg.CJoinConfDlg")
        video_call = join_window.ButtonControl(searchDepth=3,
                                               AutomationId="CHomeDlg.CJoinConfDlg.verticalWidget_2.horizontalWidget.m_pBtnVideoJoin")
        audio_call = join_window.ButtonControl(searchDepth=3,
                                               AutomationId="CHomeDlg.CJoinConfDlg.verticalWidget_2.horizontalWidget.m_pBtnAudioJoin")
        self.mute_mic(micstatus)
        self.mute_camera(camerastatus)
        operate_in_meeting = OperateInMeeting()
        if calltype == CallType.Video:
            log.info("Video call")
            video_call.Click()
            sleep(20)
            operate_in_meeting.hangup_call()
        else:
            log.info("Audio call")
            audio_call.Click()
            sleep(20)
            operate_in_meeting.audio_only_hangup()

    def join_now_meeting_from_panel(self, calltype=CallType.Video, micstatus=MicStatus.UMUTE,
                                    camerastatus=CameraStatus.UMUTE):
        log.info("Make a call from the panel")
        self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").TextControl(searchDepth=8, Name="加入会议").Click()
        self.make_call(calltype, micstatus, camerastatus)

    def join_now_meeting_from_top_menu(self, calltype=CallType.Video, micstatus=MicStatus.UMUTE,
                                       camerastatus=CameraStatus.UMUTE):
        log.info("Make a call from top menu")
        self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtTitleBar").ButtonControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtTitleBar.m_pBtnJoinConf").Click()
        self.make_call(calltype, micstatus, camerastatus)

    def join_now_meeting_from_top_menu_hangup(self, calltype=CallType.Video, micstatus=MicStatus.UMUTE,
                                              camerastatus=CameraStatus.UMUTE):
        log.info("Make a call from top menu")
        self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtTitleBar").ButtonControl(
            searchDepth=1, AutomationId="CHomeDlg.m_pWgtTitleBar.m_pBtnJoinConf").Click()
        self.make_call_and_drop(calltype, micstatus, camerastatus)

    def join_now_meeting_from_reserved_item(self, calltype=CallType.Video, micstatus=MicStatus.UMUTE,
                                            camerastatus=CameraStatus.UMUTE):
        log.info("Make a call from reserved meeting itself")
        self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").CustomControl(
            searchDepth=12, Name="加入会议").Click()
        self.make_call(calltype, micstatus, camerastatus)

    def join_now_meeting_from_reserved_item_and_hangup(self, calltype=CallType.Video, micstatus=MicStatus.UMUTE,
                                            camerastatus=CameraStatus.UMUTE):
        log.info("Make a call from reserved meeting itself")
        self.hexMeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").CustomControl(
            searchDepth=12, Name="加入会议").Click()
        self.make_call_and_drop(calltype, micstatus, camerastatus)

    def is_in_meeting(self):
        return auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg").WindowControl(
            searchDepth=1, ClassName="ev_app::views::CLayoutCoverDlg") \
            .GroupControl(searchDepth=2,
                          AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutCellCoverDlg.m_pWgtContent").Exists()
