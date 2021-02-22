import os
import sys

import allure
import pytest

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))))
from HexmeetPkg.AppSettingPageObject import AppSetting
from HexmeetPkg.ReserveMeetingPageObject import ReserveMeeting
from HexmeetPkg.OperateInMeetingPageObject import OperateInMeeting
from HexmeetPkg.joinAMeetingPageObject import JoinAMeeting
from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from time import sleep
import os
import shutil

login_user = "hexautotest6"
remote_user = "hexautotest5"
screenshot_dir = "H:\\Autotest\\"
reserve_meeting = ReserveMeeting()
operate_meeting = OperateInMeeting()
join_meeting = JoinAMeeting()
app_setting = AppSetting()
hexmeet_singleton = HexmeetWindowSingleton()

bandwidth_list = ["384K", "512K", "768K", "1M", "1.5M", "3M", "4M", "2M"]


# bandwidth_list = ["2M"]

def setup_module():
    hexmeet_singleton.start_hexmeet()
    sleep(5)
    reserve_meeting.clear_reserved_meeting()


def teardown_module():
    hexmeet_singleton.close_hexmeet()


def __remove_screen_files():
    del_list = os.listdir(screenshot_dir)
    for f in del_list:
        file_path = os.path.join(screenshot_dir, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def __count_screen_files():
    file_list = os.listdir(screenshot_dir)
    print(file_list)
    return len(file_list)


def __invite_self():
    reserve_meeting.go_to_meeting_page()
    reserve_meeting.reserve_meeting_from_panel()
    reserve_meeting.choose_now()
    reserve_meeting.choose_participants(login_user)
    reserve_meeting.reserve_confirm()
    sleep(20)
    operate_meeting.terminate_call()


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HEXMEET APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("改变语言")
@allure.story("改变语言")
def test_change_language():
    app_setting.chang_language("English")
    sleep(10)
    app_setting.chang_language("简体中文")


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HEXMEET APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("改变白板保持路径")
@allure.story("改变白板保持路径")
def test_change_screen_shot_path():
    app_setting.change_snapshot_path()


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HEXMEET APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("设置自动接听，并建会拉入")
@allure.story("设置自动接听，并建会拉入")
def test_change_auto_answer():
    app_setting.change_auto_answer()
    __invite_self()
    app_setting.change_auto_answer()


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HEXMEET APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("设置入会后全屏模式")
@allure.story("设置入会后全屏模式")
def test_change_to_full_mode_meeting():
    app_setting.change_to_full_mode_meeting()

    JoinAMeeting().join_now_meeting_from_top_menu()
    sleep(20)
    operate_meeting.terminate_call_in_full_mode()
    app_setting.change_to_full_mode_meeting()


@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HEXMEET APP的设置界面")
@allure.parent_suite("应用设置")
@allure.suite("创建遍历带宽会议并入会")
@allure.story("创建遍历带宽会议并入会")
def test_remove_reserved_meeting():
    reserve_meeting.go_to_meeting_page()
    sleep(5)
    reserve_meeting.clear_reserved_meeting()


if __name__ == '__main__':
    pytest.main(["-s", "test_appsetting.py", "--alluredir=reports"])
