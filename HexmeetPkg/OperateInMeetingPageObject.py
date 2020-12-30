import logging
import uiautomation as auto
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class OperateInMeeting:

    def __init__(self):
        self.HexmeetMeetingWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg")
        self.meetingWindowControl = self.HexmeetMeetingWindow.GroupControl(searchDepth=1,
                                                                           AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar")
        self.meetingLabel = self.meetingWindowControl.TextControl(searchDepth=1,
                                                                   AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar.m_pLblConfNumber")
        self.meetingControlToolBar = self.HexmeetMeetingWindow.WindowControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg")

    def click_meetingLabel(self):
        log.info("Click the meeting number to call the toolbar")
        x, y = auto.GetCursorPos()
        self.meetingLabel.Click()
        auto.SetCursorPos(x, y)

    def show_media_statistics(self):
        log.info("show media statistics")
        self.meetingWindowControl.ButtonControl(searchDepth=2,
                                                AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar.m_pLeftWidget.m_pBtnNetworkQuality").Click()
        # 点击完后，把鼠标移到视频，以便移到鼠标调出工具条
        x, y = auto.GetCursorPos()
        auto.Click(x, y + 40)

    def close_media_statistics(self):
        log.info("Close media statistics")
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CMediaStatisticsDlg") \
            .ButtonControl(searchDepth=2,
                           AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CAudioModeWidget.CLayoutToolbarDlg.CMediaStatisticsDlg.m_pWgtTitleBar.m_pBtnClose").Click()

    def umte_umute_audio(self):
        """解除静音"""
        log.info("mute umute audio")
        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.CheckBoxControl(searchDepth=1,
                                                   AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnEnableMic").Click()

    def mute_umute_camera(self):
        """停止视频"""
        log.info("mute umute camera")
        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.CheckBoxControl(searchDepth=1,
                                                   AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnEnableCamera").Click()

    def share_content_sound_highframerate(self):
        """分享屏幕 共享声音 流畅度优先"""
        log.info("Share content with voice and high framerate")
        shareContentWindow = self.HexmeetMeetingWindow.WindowControl(searchDepth=2, ClassName="ev_app::views::CSelectShareContent")
        contentInSharingWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CbackgroundWidget")

        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, Name="分享").Click()
        time.sleep(1)
        shareContentWindow.CheckBoxControl(searchDepth=2, Name="共享电脑声音").Click()
        shareContentWindow.CheckBoxControl(searchDepth=2, Name="流畅度优先").Click()
        time.sleep(2)
        shareContentWindow.ButtonControl(searchDepth=2, Name="分享").Click()
        time.sleep(30)
        contentInSharingWindow.TextControl(searchDepth=7, Name="停止分享").Click()
        time.sleep(2)
        contentInSharingWindow.ButtonControl(searchDepth=4, Name="是").Click()

    def share_content(self):
        """分享屏幕 不共享声音 1080P"""
        log.info("Share content with 1080P")
        shareContentWindow = self.HexmeetMeetingWindow.WindowControl(searchDepth=2, ClassName="ev_app::views::CSelectShareContent")
        contentInSharingWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CbackgroundWidget")

        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, Name="分享").Click()

        time.sleep(2)
        shareContentWindow.ButtonControl(searchDepth=2, Name="分享").Click()
        time.sleep(30)
        contentInSharingWindow.TextControl(searchDepth=7, Name="停止分享").Click()
        time.sleep(2)
        contentInSharingWindow.ButtonControl(searchDepth=4, Name="是").Click()

    def change_volume(self):
        """调节音量"""
        log.info("Change volume")
        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.CheckBoxControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnVolume").Click()
        auto.PressKey(auto.Keys.VK_UP * 5)
        auto.PressKey(auto.Keys.VK_DOWN * 5)

    def maximise_window(self):
        """最大化窗口"""
        log.info("Maximise the window")
        time.sleep(10)
        self.meetingWindowControl.ButtonControl(searchDepth=2,
                                                AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar.m_pRightWidget.m_pBtnMax").Click()

    def restore_window_from_maximise(self):
        """恢复先前视窗"""
        log.info("Restore the window")
        time.sleep(10)
        self.meetingWindowControl.ButtonControl(searchDepth=2,
                                                AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar.m_pRightWidget.m_pBtnRestore").Click()

    def video_fullscreen(self):
        """视频全屏"""
        log.info("Fullscreen view")
        time.sleep(10)
        self.meetingWindowControl.ButtonControl(searchDepth=2,
                                                AutomationId="CLayoutBackgroundDlg.m_pWgtTitleBar.m_pRightWidget.m_pBtnFullScreen").Click()

    def video_restore_from_fullscreen(self):
        """恢复先前视频窗口"""
        log.info("Restore from fullscreen view")
        time.sleep(10)
        x, y = auto.GetCursorPos()
        auto.Click(x - 1000, y + 400)
        self.HexmeetMeetingWindow.WindowControl(searchDepth=3,
                                                AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pWgtTitleBar") \
            .ButtonControl(searchDepth=2,
                           AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pWgtTitleBar.m_pRightWidget.m_pBtnFullScreen_Exit").Click()
        auto.Click(x - 100, y + 50)

    def hangup_call(self):
        """挂断"""
        log.info("Video call drop")
        time.sleep(10)
        self.click_meetingLabel()
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg").WindowControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg").ButtonControl(searchDepth=1,
                                                 AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnHangup").Click()
        time.sleep(2)
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(searchDepth=2, Name="离开会议").Click()


    def audio_only_hangup(self):
        """挂断"""
        log.info("Audio call drop")
        time.sleep(10)
        self.click_meetingLabel()
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CAudioModeWidget").ButtonControl(searchDepth=2,
                                                                                              AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CAudioModeWidget.CLayoutToolbarDlg.m_pBtnHangup").Click()
        time.sleep(2)
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CAudioModeWidget.CLayoutToolbarDlg.AlertDlg.m_bottomWidget.m_button1").Click()


    def terminate_call(self):
        """结束会议"""
        log.info("Terminate the call")
        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.ButtonControl(searchDepth=1,
                                                 AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnHangup").Click()
        time.sleep(2)
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(searchDepth=2,
                                                                                             Name="结束会议").Click()

    def terminate_call_in_full_mode(self):
        """结束会议"""
        log.info("Terminate the call in fullscreen view mode")
        time.sleep(10)
        x, y = auto.GetCursorPos()
        # Normal PC auto.Click(x+800, y-300)
        # High DPI
        auto.Click(x + 800, y - 300)
        self.meetingControlToolBar.ButtonControl(searchDepth=1,
                                                 AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnHangup").Click()
        time.sleep(2)
        auto.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(searchDepth=2,
                                                                                             Name="离开会议").Click()

    def minimise_local_video(self):
        """本地视频最小化"""
        log.info("Minimise local video")
        self.meetingControlToolBar.ButtonControl(searchDepth=3,
                                            AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.CLayoutFloatingCellsDlg.m_pWgtTopTitleBar.pBtMin").Click()

    def maximise_local_video(self):
        """恢复本地视频"""
        log.info("Restore the minimised local video")
        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.widget.m_pBtnShowPic").Click()

    '''
    def share_whiteboard(self):
        """共享白板"""
        shareContentWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg") \
            .WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutCoverDlg") \
            .WindowControl(searchDepth=1, ClassName="ev_app::views::CSelectShareContent")
        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnShare").Click()
        time.sleep(2)
        shareContentWindow.TextControl(searchDepth=7, Name="白板").Click()
        time.sleep(2)
        shareContentWindow.ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CSelectShareContent.toolbar.pBtShare").Click()
        time.sleep(30)
        white_board_window = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::WhiteBoardDlg")
        white_board_window.GroupControl(searchDepth=1, ClassName="ev_app::views::WhiteBoardTopWidget").TextControl(searchDepth=4, Name="停止分享").Click()
        exit_white_board_button = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::WhiteBoardDlg").WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg")\
            .ButtonControl(searchDepth=3, Name="是")
        if exit_white_board_button.Exists():
            exit_white_board_button.Click()

    def switch_video_layout(self):
        """分屏切换"""
        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.CheckBoxControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnSwitchLayout").Click()

    def __change_name_window(self, rename_window):
        """ 调出更名窗口 """
        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnMore").Click()
        time.sleep(1)
        self.meetingControlToolBar.ButtonControl(searchDepth=2, Name="改名").Click()
        time.sleep(2)
        rename_window.EditControl(searchDepth=2, AutomationId="CChangeNameWidget.verticalWidget_2.m_pInputNewNameEdit").Click()

    def rename(self, new_name):
        """改名"""
        rename_window = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CChangeNameWidget")
        self.__change_name_window(rename_window)
        time.sleep(1)
        rename_window.EditControl(searchDepth=2, AutomationId="CChangeNameWidget.verticalWidget_2.m_pInputNewNameEdit").SendKeys(new_name)
        rename_window.ButtonControl(searchDepth=2, AutomationId="CChangeNameWidget.m_pBottomView.m_pSureButton").Click()

    def rename_enter_key(self, new_name):
        """改名 === 名字里面包含 {ENTER}"""
        rename_window = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CChangeNameWidget")
        self.__change_name_window(rename_window)
        time.sleep(1)
        rename_window.EditControl(searchDepth=2, AutomationId="CChangeNameWidget.verticalWidget_2.m_pInputNewNameEdit").SendKeys(new_name)

    def audio_only(self):
        """切换到语音模式"""
        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.ButtonControl(searchDepth=1, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.m_pBtnMore").Click()
        time.sleep(1)
        self.meetingControlToolBar.ButtonControl(searchDepth=2, Name="切到语音模式").Click()

    def av_escalation(self):
        """切换到视频模式"""
        avEscalationWindow = auto.WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutBackgroundDlg") \
            .WindowControl(searchDepth=1, ClassName="ev_app::views::CLayoutCoverDlg")
        avEscalationWindow.ButtonControl(searchDepth=2, Name="退出语音模式").Click()

    def minimise_local_video(self):
        """本地视频最小化"""
        self.meetingControlToolBar.ButtonControl(searchDepth=3,
                                            AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.CLayoutFloatingCellsDlg.m_pWgtTopTitleBar.pBtMin").Click()

    def maximise_local_video(self):
        """恢复本地视频"""
        time.sleep(10)
        self.click_meetingLabel()
        self.meetingControlToolBar.ButtonControl(searchDepth=2, AutomationId="CLayoutBackgroundDlg.CLayoutPeopleSettingDlg.CLayoutCoverDlg.CLayoutToolbarDlg.widget.m_pBtnShowPic").Click()

    '''
