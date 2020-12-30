import pytest
import allure
from time import sleep
from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from HexmeetPkg.ContactPageObject import Contact
from HexmeetPkg.Common import CallType

hjt_singleton = HexmeetWindowSingleton()
contact = Contact()
contact_user = "hexautotest5"


def setup_module():
    hjt_singleton.start_hexmeet()


def teardown_module():
    hjt_singleton.close_hexmeet()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("通讯录")
@allure.feature("测试HEXMEET APP的通讯录操作")
@allure.story("视频呼叫常用联系人")
def test_video_call_from_favorite():
    sleep(5)
    contact.call_from_favorite(contact_user)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("通讯录")
@allure.feature("测试HEXMEET APP的通讯录操作")
@allure.story("音频呼叫常用联系人")
def test_audio_call_from_favorite():
    sleep(5)
    contact.call_from_favorite(contact_user, call_type=CallType.Audio)



if __name__ == '__main__':
    pytest.main(["-s", "test_contact_favorite.py"])
