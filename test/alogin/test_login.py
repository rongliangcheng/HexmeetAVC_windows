import pytest
import allure
import sys
import os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))))
from HexmeetPkg.LoginPageObject import UserLogin
from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from time import sleep

user_login = UserLogin()
hjt_singleton = HexmeetWindowSingleton()

server_addr="172.25.0.9"
user_name="hexautotest5"
password="123456"

def setup_module():
    hjt_singleton.start_hexmeet()


def teardown_module():
    hjt_singleton.close_hexmeet()


def __user_login(server_addr, account, password):
    user_login.fill_in_server_address(server_addr)
    user_login.fill_in_account(account)
    user_login.fill_in_password(password)
    user_login.user_login_commit()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("登录")
@allure.suite("回到登录界面")
@allure.feature("测试HEXMEET APP的登录界面的操作")
@allure.story("回到登录界面")
def test_go_to_login_page():
    sleep(3)
    user_login.go_to_login_page()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("登录")
@allure.suite("以错误账号登陆")
@allure.feature("测试HEXMEET APP的登录界面的操作")
@allure.story("以错误账号登陆")
def test_login_with_wrong_account():
    __user_login("172.25.0.9", "hjtautotes", "123456")
    user_login.login_fail_commit()


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("登录")
@allure.suite("登录不正确的服务器")
@allure.feature("测试HEXMEET APP的登录界面的操作")
@allure.story("登录不正确的服务器")
def test_login_with_wrong_server_address():
    __user_login("loudbeta.hexmeet.com", "hjtautotest6", "123456")
    user_login.login_fail_commit()


# @pytest.mark.flaky(rerun=1, rerun_delay=2)
# @allure.parent_suite("登录")
# @allure.suite("尝试5遍被锁5分钟")
# @allure.feature("测试HEXMEET APP的登录界面的操作")
# @allure.story("尝试5遍被锁5分钟")
# def test_login_with_5_times_wrong_password():
#     for i in range(6):
#         __user_login("172.25.0.9", "hexautotest6", "12346")
#         sleep(1)
#         user_login.login_fail_commit()
#         sleep(10)


@pytest.mark.flaky(rerun=1, rerun_delay=2)
@allure.parent_suite("登录")
@allure.suite("正常登录成功")
@allure.feature("测试HEXMEET APP的登录界面的操作")
@allure.story("正常登录成功")
def test_login_with_normal():
    # sleep(300)
    __user_login("172.25.0.9", "hexautotest6", "123456")


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
