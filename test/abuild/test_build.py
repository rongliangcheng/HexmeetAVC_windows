import subprocess
from time import sleep

import pytest
import allure
import sys
import os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))))
from HexmeetPkg.AppVersion import AppVersion
from HexmeetPkg.BuildVersion import BuildVersion
from HexmeetPkg.HexmeetWindowsSingleton import HexmeetWindowSingleton
from HexmeetPkg.Common import CommonClass
import re

projectName = "swep-evsdk-win-avc-qt-2.6.1"
hjt_singleton = HexmeetWindowSingleton()


def setup_module():
    hjt_singleton.start_hexmeet()


def teardown_module():
    hjt_singleton.close_hexmeet()

@pytest.mark.flaky(rerun=1, reruns_delay=2)
@allure.feature("测试HEXMEET APP的设置界面")
@allure.parent_suite("应用设置")
@allure.story("创建遍历带宽会议并入会")
def test_install_build():
    appVersion = AppVersion()
    buildVersion = BuildVersion()

    current_version = appVersion.getAppVersion()
    build_version = buildVersion.last_build_version(projectName)

    if current_version.__contains__(str(build_version)):
        pass
    else:
        hjt_singleton.close_hexmeet()
        build_file_url = buildVersion.get_build_file_name(projectName, "exe")
        print(build_file_url)
        buildVersion.download_build(build_file_url, "HexmeetQt.exe")
        buildVersion.install_build()
        sleep(60)

        matchObj = re.search(r'2\.6\.1\.([0-9]+)', build_file_url, re.I)
        CommonClass().createEnvironmentFile("../allure-results/Environment.xml", matchObj.group())
        hjt_singleton.start_hexmeet()
        sleep(10)
        current_version = AppVersion().getAppVersion()

    assert current_version.__contains__(str(build_version))


if __name__ == '__main__':
    pytest.main(["-s", "test_build.py", "--alluredir=reports"])
