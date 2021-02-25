import pytest
import allure
from time import sleep
import uiautomation as auto

from HexmeetPkg.Common import CallType, MicStatus, CameraStatus
from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from HexmeetPkg.OperateInMeetingPageObject import OperateInMeeting
from HexmeetPkg.ReserveMeetingPageObject import ReserveMeeting
from HexmeetPkg.joinAMeetingPageObject import JoinAMeeting

hjt_singleton = HexmeetWindowSingleton()
reserve_meeting = ReserveMeeting()
join_a_meeting = JoinAMeeting()
remote_user = "hexautotest5"
password = "1234"

call_matrix = [
    (CallType.Video, MicStatus.MUTE, CameraStatus.MUTE),
    (CallType.Video, MicStatus.MUTE, CameraStatus.UMUTE),
    (CallType.Video, MicStatus.UMUTE, CameraStatus.MUTE),
    (CallType.Video, MicStatus.UMUTE, CameraStatus.UMUTE),
    (CallType.Audio, MicStatus.MUTE, CameraStatus.MUTE),
    (CallType.Audio, MicStatus.MUTE, CameraStatus.UMUTE),
    (CallType.Audio, MicStatus.UMUTE, CameraStatus.MUTE),
    (CallType.Audio, MicStatus.UMUTE, CameraStatus.UMUTE),
]


@allure.parent_suite("预约会议")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
def setup_module():
    hjt_singleton.start_hexmeet()
    sleep(5)


def teardown_module():
    hjt_singleton.close_hexmeet()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("点击入会")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("点击入会")
@allure.step("点击入会")
def test_click_reserve_meeting():
    sleep(3)
    reserve_meeting.clear_reserved_meeting()
    sleep(4)
    reserve_meeting.reserve_meeting_from_panel()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("点击入会")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("点击入会")
@allure.step("点击入会")
def test_choose_date():
    sleep(2)
    reserve_meeting.choose_date()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("选择时间")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("选择时间")
@allure.step("选择时间")
def test_choose_time():
    sleep(2)
    reserve_meeting.choose_time()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("选择时长")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("选择时长")
@allure.step("选择时长")
def test_choose_duration():
    sleep(2)
    reserve_meeting.choose_duration()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("输入密码")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("输入密码")
@allure.step("输入密码")
def test_fill_password():
    sleep(2)
    reserve_meeting.fill_password(password)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("加入备注")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("加入备注")
@allure.step("加入备注")
def test_fill_meeting_note():
    sleep(2)
    reserve_meeting.fill_meeting_notes("This is a reserved meeting")


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("选择与会者")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("选择与会者")
@allure.step("选择与会者")
def test_choose_participant():
    sleep(2)
    reserve_meeting.choose_participants(remote_user)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("相同分屏")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("相同分屏")
@allure.step("相同分屏")
def test_use_random_number_as_meeting_room():
    auto.WheelDown(6)
    sleep(2)
    reserve_meeting.same_layout()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("入会自动静音")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("入会自动静音")
@allure.step("入会自动静音")
def test_mute_when_join_meeting():
    sleep(2)
    reserve_meeting.mute_after_join()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("创建会议")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("创建会议")
@allure.step("创建会议")
def test_create_reserve_meeting():
    auto.WheelDown()
    sleep(2)
    reserve_meeting.reserve_confirm()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("对已经预约会议进行修改")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("对已经预约会议进行修改")
@allure.step("对已经预约会议进行修改")
def test_edit_and_return_from_reserve_meeting():
    sleep(3)
    reserve_meeting.edit_reserve_meeting()
    sleep(2)
    reserve_meeting.return_from_reserve_meeting()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("删除预约会议")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("删除预约会议")
@allure.step("删除预约会议")
def test_delete_reserve_meeting():
    reserve_meeting.delete_reserve_meeting()



@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("创建带密码的立即会议然后加入")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("创建带密码的立即会议然后加入")
def test_create_now_password_and_join():
    reserve_meeting = ReserveMeeting()
    join_a_meeting = JoinAMeeting()
    reserve_meeting.create_now_meeting_from_panel()
    sleep(1)
    reserve_meeting.fill_password(password)
    sleep(1)
    reserve_meeting.choose_participants(remote_user)
    sleep(1)
    reserve_meeting.reserve_confirm()
    sleep(15)
    join_a_meeting.join_now_meeting_from_reserved_item_and_hangup()
    # sleep(5)
    # reserve_meeting.return_from_reserve_meeting()
    sleep(5)
    join_a_meeting.join_now_meeting_from_reserved_item_and_hangup(CallType.Video, MicStatus.MUTE, CameraStatus.UMUTE)
    # sleep(5)
    # ReserveMeeting().terminate_now_meeting()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("创建即时会议")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("创建即时会议")
def test_create_now_meeting():
    reserve_meeting = ReserveMeeting()
    reserve_meeting.clear_reserved_meeting()
    sleep(2)
    reserve_meeting.reserve_meeting_from_panel()
    sleep(1)
    reserve_meeting.choose_now()
    reserve_meeting.reserve_confirm()
    sleep(3)
    reserve_meeting.return_from_reserve_meeting()
    sleep(1)


@pytest.mark.flaky(rerun=2, rerun_delay=2)
@allure.parent_suite("预约会议")
@allure.suite("音视频，麦克风，摄像头呼叫组合")
@allure.feature("测试HEXMEET APP的设置预约会议操作")
@allure.story("音视频，麦克风，摄像头呼叫组合")
@pytest.mark.parametrize('callmode, mic_status, camera_status', call_matrix)
def test_parametrize_call_mode_matrix(callmode, mic_status, camera_status):
    join_a_meeting.join_now_meeting_from_reserved_item_and_hangup(callmode, mic_status, camera_status)


# @pytest.mark.flaky(rerun=1, rerun_delay=2)
# @allure.parent_suite("预约会议")
# @allure.suite("音视频，麦克风，摄像头呼叫组合会议删除")
# @allure.feature("测试HEXMEET APP的设置预约会议操作")
# @allure.story("音视频，麦克风，摄像头呼叫组合会议删除")
# def test_terminate_reserved_now_call():
#     sleep(5)
#     reserve_meeting.terminate_now_meeting()
#


if __name__ == '__main__':
    pytest.main(["-s", "--instafail", "test_reservemeeting.py"])
