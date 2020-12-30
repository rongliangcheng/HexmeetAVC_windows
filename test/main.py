import pytest

import sys
import os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))))

if __name__ == '__main__':
    # pytest.main(["-v", "-s", "./abuild/test_build.py", "./alogin/test_login.py"])
    pytest.main(["-v", "-s", "./abuild/test_build.py", "./alogin/test_login.py",  "./contact/test_contact_favorite.py", "./appsetting/test_appsetting.py",
                  "./operateinameetingtest/test_operatemeeting.py", "./reservemeetingtest/test_reservemeeting.py", "--alluredir=reports"])
