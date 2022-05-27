# -*- coding: utf-8 -*-
# Description: 
# Created: jjunf 2021/8/26 20:14
from app.main.test.package.base_dao import BaseDao


class UserDao(BaseDao):
    def save_register_user_information(self, user):
        sql = """
            INSERT INTO db_model.t_user(user_name, pass_word, create_date)
            VALUES ('{}', '{}', '{}')
        """
        sql = sql.format(user['user_name'], user['pass_word'], user['create_date'])
        self.execute(sql)
