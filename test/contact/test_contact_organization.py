import pytest
import allure
from time import sleep
from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from HexmeetPkg.ContactPageObject import Contact
from HexmeetPkg.Common import CallType
from HexmeetPkg.ReserveMeetingPageObject import ReserveMeeting

hjt_singleton = HexmeetWindowSingleton()
contact = Contact()
contact_user = "hexautotest5"


def setup_module():
    hjt_singleton.start_hexmeet()
    sleep(5)
    ReserveMeeting().clear_reserved_meeting()


def teardown_module():
    hjt_singleton.close_hexmeet()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("通讯录")
@allure.feature("测试HEXMEET APP的通讯录操作")
@allure.suite("从组织架构中查找联系人")
@allure.story("从组织架构中查找联系人")
def test_video_call_from_organization():
    sleep(5)
    contact.go_to_contact_organization_page_search(contact_user)
    contact.call_from_organization(contact_user)

@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("通讯录")
@allure.feature("测试HEXMEET APP的通讯录操作")
@allure.suite("从组织架构中查找联系人")
@allure.story("从组织架构中查找联系人")
def test_audio_call_from_organization():
    sleep(5)
    contact.call_from_organization(contact_user, call_type=CallType.Audio)



if __name__ == '__main__':
    pytest.main(["-s", "test_contact_organization.py"])
