import ctypes
import sys

import jenkins
import requests
import os
import time
import logging


class BuildVersion:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.buildUrl = "http://172.27.0.12:8080/login?from=%2F"
        self.server = jenkins.Jenkins(self.buildUrl, username="chengrl", password="123456")

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False



    def last_build_version(self, projectName):
        self.log.debug("last_build_version")
        projectJobs = self.server.get_all_jobs()
        for job in projectJobs:
            if job['fullname'] == projectName:
                info = self.server.get_job_info(projectName)
                return info['lastSuccessfulBuild']['number']
        return None

    def get_build_file_name(self, projectName, fileNameRegi):
        self.log.debug("get_build_file_name")
        build_base_url = "http://172.27.0.12:8080/view/HexMeet%20AVC/job/swep-evsdk-win-avc-qt-2.6.1/lastSuccessfulBuild/"
        build_info = self.server.get_build_info(projectName, self.last_build_version(projectName))
        build_url = ""
        for artifact in build_info['artifacts']:
            if (fileNameRegi in artifact['fileName']):
                build_url = build_base_url + 'artifact/' + artifact['relativePath']
        return build_url

    def download_build(self, fileurl, target):
        self.log.debug("download_build")
        s = requests.session()
        fileContent = s.get(fileurl, auth=('chengrl', '123456'))
        with open(target, 'wb') as content:
            content.write(fileContent.content)

    def install_build(self):
        if self.is_admin():
            self.log.debug("install_build")
            install_command = "cmd.exe /c  HexmeetQt.exe /s /v/qn"
            del_command = "cmd.exe /c del HexmeetQt.exe "
            os.system(install_command)
            os.system(del_command)
            self.log.debug("finished")
        else:
            if sys.version_info[0] == 3:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


if __name__ == '__main__':
    projectName = "swep-evsdk-win-avc-qt-2.6.1"
    build_version = BuildVersion()
    build_file_url = build_version.get_build_file_name(projectName, "exe")
    build_version.download_build(build_file_url, "HexmeetQt.exe")
    build_version.install_build()

