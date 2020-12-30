import uiautomation as auto
from time import sleep
import logging
from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton


class AppSetting:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.info("AppSetting init --")
        self.hexMeetHJTWindow = HexmeetWindowSingleton().getHexmeetWindow()
        self.setting_page = self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").GroupControl(searchDepth=2,
                                                                                                                                  AutomationId="CHomeDlg.m_pWgtContext.m_pStackedWgtContent.CSettingsForm")

    def go_to_setting_page(self):
        self.log.info("go_to_setting_page")
        self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtOperationBar").ListControl(searchDepth=2,
                                                                                                                  ClassName="ev_app::custom_controls::CHomeMenuListView").Click()
        x, y = auto.GetCursorPos()
        auto.Click(x, y + 70)

    def chang_bandwidth(self, value):
        """
        values are
        384K,512K,768K,1M,1.5M,2M,3M,4M
        """
        self.log.info("chang_bandwidth")
        self.go_to_setting_page()
        sleep(3)
        self.setting_page.TextControl(searchDepth=9, Name="呼叫速率").Click()
        x, y = auto.GetCursorPos()
        auto.Click(x, y + 40)
        self.setting_page.ListItemControl(searchDepth=11, Name=value).Click()

    def chang_language(self, language):
        """
        languages are
        English,简体中文
        """
        self.log.info("chang_language")
        self.go_to_setting_page()
        sleep(3)
        if self.setting_page.TextControl(searchDepth=9, Name="语言").Exists():
            self.setting_page.TextControl(searchDepth=9, Name="语言").Click()
        else:
            self.setting_page.TextControl(searchDepth=9, Name="Language").Click()

        x, y = auto.GetCursorPos()
        auto.Click(x, y + 40)
        self.setting_page.ListItemControl(searchDepth=11, Name=language).Click()

    def change_snapshot_path(self):
        self.log.info("change_snapshot_path")
        sleep(3)
        self.go_to_setting_page()
        self.setting_page.ButtonControl(searchDepth=9, AutomationId="CHomeDlg.m_pWgtContext.m_pStackedWgtContent.CSettingsForm.twgtSettingsPages.qt_tabwidget_stackedwidget"
                                                                    ".tabSettingsGeneral.m_pScrollGeneral.qt_scrollarea_viewport.scaSettingsGeneral.scorllGeneralWidght"
                                                                    ".m_pWgtSnapshotPathPanel.m_pBtnChangeSnapshotPath").Click()
        sleep(1)
        self.hexMeetHJTWindow.WindowControl(searchDepth=1, Name="请选择截图文件存放位置:").ButtonControl(searchDepth=1, Name="选择文件夹").Click()

    def change_auto_login(self):
        self.log.info("change_auto_login")
        self.go_to_setting_page()
        self.setting_page.CheckBoxControl(searchDepth=9, Name="自动登录").Click()

    def change_auto_answer(self):
        self.log.info("change_auto_answer")
        self.go_to_setting_page()
        self.setting_page.CheckBoxControl(searchDepth=9, Name="自动应答").Click()


    def change_disable_prompt(self):
        self.log.info("change_disable_prompt")
        self.go_to_setting_page()
        self.setting_page.CheckBoxControl(searchDepth=10, Name="关闭提示").Click()

    def change_to_full_mode_meeting(self):
        self.log.info("change_to_full_mode_meeting")
        self.go_to_setting_page()
        self.setting_page.TextControl(searchDepth=9, Name="应用").Click()
        auto.WheelDown(5)
        self.setting_page.CheckBoxControl(searchDepth=9, Name="进入会议时全屏显示").Click()
        sleep(1)
        self.go_to_setting_page()
