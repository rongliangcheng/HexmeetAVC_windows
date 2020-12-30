import subprocess
import os
import uiautomation as auto
from time import sleep


class HexmeetWindowSingleton:
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            print(auto.GetRootControl())
            subprocess.Popen("C:\\Program Files (x86)\\HexMeet\\HexMeet.exe")
        return cls.__instance

    @staticmethod
    def getHexmeetWindow() -> auto.WindowControl:
        return auto.WindowControl(searchDepth=1, ClassName='ev_app::views::CHomeDlg')

    @staticmethod
    def close_hexmeet():
        """关闭程序"""
        try:
            hexmeetWindow = auto.WindowControl(searchDepth=1, ClassName='ev_app::views::CHomeDlg')
            if hexmeetWindow.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(
                    searchDepth=3, Name="确定").Exists(1):
                hexmeetWindow.WindowControl(searchDepth=1, ClassName="ev_app::views::AlertDlg").ButtonControl(
                    searchDepth=3, Name="确定").Click()
            sleep(3)
            hexmeetWindow.GroupControl(searchDepth=1, AutomationId="CHomeDlg.m_pWgtTitleBar").ButtonControl(
                searchDepth=1, AutomationId="CHomeDlg.m_pWgtTitleBar.m_pBtnClose").Click()
            sleep(3)
            hexmeetWindow.WindowControl(searchDepth=1, AutomationId="CHomeDlg.AlertDlg").ButtonControl(searchDepth=3,
                                                                                                          Name="确定").Click()
            sleep(3)

            cmd = 'taskkill /F /IM HexMeet.exe'
            os.system(cmd)
        # if hexmeetWindow.Exists():
        except:
            cmd = 'taskkill /F /IM HexMeet.exe'
            os.system(cmd)

    @staticmethod
    def start_hexmeet():
        """重启应用"""
        sleep(5)
        if not auto.WindowControl(searchDepth=1, ClassName='ev_app::views::CHomeDlg').Exists():
            subprocess.Popen("C:\\Program Files (x86)\\HexMeet\\HexMeet.exe")


if __name__ == '__main__':
    HexmeetWindowSingleton().start_hexmeet()
    sleep(5)
    HexmeetWindowSingleton.close_hexmeet()
