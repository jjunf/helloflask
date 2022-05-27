# -*- coding: utf-8 -*-
# Description: 
# Created: jjunf 2021/8/26 20:42
from pymysql import MySQLError
import pymysql
from DBUtils.PooledDB import PooledDB

adb_pool = PooledDB(
    pymysql,
    2,
    host='localhost',
    port=3306,
    user='root',
    passwd='jjf',
    db='db_model',
    charset='utf8'
)


class UserDao:

    @staticmethod
    def select_all(sql, params=None, db_pool=adb_pool):
        conn = None
        cursor = None
        try:
            conn = db_pool.connection()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            raise MySQLError
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def execute(sql, params=None, db_pool=adb_pool):
        conn = None
        cursor = None
        try:
            conn = db_pool.connection()
            cursor = conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise MySQLError
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def save_register_user_information(self, user):
        sql = """
            INSERT INTO db_model.t_user(user_name, pass_word, create_date)
            VALUES ('{}', '{}', '{}')
        """
        sql = sql.format(user['user_name'], user['pass_word'], user['create_date'])
        self.execute(sql)


class UserService:
    def register_service(self, user):
        # 保存注册用户
        UserDao().save_register_user_information(user)
        return 2
