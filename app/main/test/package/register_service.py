# -*- coding: utf-8 -*-
# Description: 
# Created: jjunf 2021/8/26 20:00
from app.main.test.package.user_dao import UserDao


def register_service(user):
    # 保存注册用户
    UserDao().save_register_user_information(user)
    if 1 == 1:
        return 2
