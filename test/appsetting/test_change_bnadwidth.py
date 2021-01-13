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


def __join_and_quit_meeting():
    sleep(5)
    join_meeting.join_now_meeting_from_top_menu()
    sleep(10)
    operate_meeting.show_media_statistics()
    sleep(10)
    operate_meeting.hangup_call()


def __invite_self():
    reserve_meeting.go_to_meeting_page()
    reserve_meeting.reserve_meeting_from_panel()
    reserve_meeting.choose_now()
    reserve_meeting.choose_participants(login_user)
    reserve_meeting.reserve_confirm()
    sleep(20)
    operate_meeting.terminate_call()



def __invite_others_and_join_the_meeting():
    reserve_meeting.reserve_meeting_from_panel()
    reserve_meeting.choose_now()
    reserve_meeting.choose_participants(remote_user)
    reserve_meeting.reserve_confirm()
    sleep(3)



@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HEXMEET APP的设置界面")
@allure.parent_suite("应用设置")
@allure.story("创建遍历带宽会议并入会")
def test_prepare_all():
    sleep(5)
    reserve_meeting.clear_reserved_meeting()
    sleep(5)
    __invite_others_and_join_the_meeting()
    JoinAMeeting().join_now_meeting_from_reserved_item_and_hangup()
    # reserve_meeting.return_from_reserve_meeting()


@allure.feature("测试HEXMEET APP的设置界面")
@allure.parent_suite("应用设置")
@allure.story("改变带宽并入会")
@pytest.mark.parametrize('bandwidth', bandwidth_list)
def test_change_bandwidth(bandwidth):
    # for bandwidth in bandwidth_list:
    app_setting.chang_bandwidth(bandwidth)
    sleep(2)
    __join_and_quit_meeting()
    sleep(8)


# @pytest.mark.flaky(rerun=1, reruns_delay=2)
# @allure.feature("测试HEXMEET APP的设置界面")
# @allure.parent_suite("应用设置")
# @allure.story("结束带宽遍历会议")
# def test_terminate_the_meeting():
#     reserve_meeting.go_to_meeting_page()
#     reserve_meeting.terminate_now_meeting()


if __name__ == '__main__':
    pytest.main(["-s", "test_appsetting.py", "--alluredir=reports"])
