#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 14:24
# @Author  : yxChen

from login import Login
import requests
from config import Config

class Main:
    def __init__(self):
        session_admin = requests.Session()
        self.session_admin: requests.Session = Login(session_admin, Config.admin_user).get_login_session()
        session_tester = requests.Session()
        self.session_tester: requests.Session = Login(session_tester, Config.test_user).get_login_session()

    def start(self):
        pass

    def clean(self):
        pass




if __name__ == '__main__':
    Main()

