from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from HexmeetPkg.AppSettingPageObject import AppSetting
from time import sleep


class AppVersion:
    def __init__(self):
        self.hexMeetHJTWindow = HexmeetWindowSingleton().getHexmeetWindow()
        self.app_setting = AppSetting()


    def getAppVersion(self):
        self.app_setting.go_to_setting_page()
        sleep(1)
        setting_form_page = self.hexMeetHJTWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtContext").GroupControl(searchDepth=2, AutomationId="CHomeDlg.m_pWgtContext.m_pStackedWgtContent.CSettingsForm")
        setting_form_page.ListItemControl(searchDepth=3, Name="关于").Click()
        sleep(1)
        version = setting_form_page.TextControl(searchDepth=7, AutomationId="CHomeDlg.m_pWgtContext.m_pStackedWgtContent.CSettingsForm.twgtSettingsPages.qt_tabwidget_stackedwidget.tabSettingsAbout.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.m_pLabVersion").Name
        return version.split("：", 1)[1]


if __name__ == '__main__':
    print(AppVersion().getAppVersion())

