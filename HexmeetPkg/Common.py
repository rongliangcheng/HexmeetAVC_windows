from enum import Enum
import logging

class CommonClass:
    def createEnvironmentFile(self, file, string):
        content1 = "<environment>\n   <parameter>\n       <key>HexMeet.version</key>\n     <value>"
        content2 = "</value>\n    </parameter>\n</environment>"

        with open(file, "w+") as f:
            f.truncate()
            f.write(content1 + string + content2)


class CallType(Enum):
    Video = 1,
    Audio = 2

class MicStatus(Enum):
    MUTE = 1,
    UMUTE = 2

class CameraStatus(Enum):
    MUTE = 1,
    UMUTE = 2

if __name__ == '__main__':
    CommonClass().createEnvironmentFile("allure-results/Environment.xml", "1.4.1.157")

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)