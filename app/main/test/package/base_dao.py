import traceback
import pymysql
import pandas as pd
from pymysql import MySQLError
# from app.main.db_pool import adb_pool
from app.main.test.package.db_pool import adb_pool


class BaseDao:
    """封装数据库操作基础类"""

    @staticmethod
    def select_one(sql, params=None, db_pool=adb_pool):
        conn = None
        cursor = None
        try:
            conn = db_pool.connection()
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            return cursor.fetchone()
        except Exception as e:
            raise MySQLError
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

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

    @staticmethod
    def executemany(sql, params=None, db_pool=adb_pool):
        conn = None
        cursor = None
        try:
            conn = db_pool.connection()
            cursor = conn.cursor()
            if params:
                cursor.executemany(sql, params)
            else:
                cursor.executemany(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise MySQLError
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def execute_many_sql(sql_list, params, db_pool=adb_pool):
        conn = None
        cursor = None
        try:
            conn = db_pool.connection()
            cursor = conn.cursor()
            cursor.execute(sql_list[0])
            cursor.executemany(sql_list[1], params)
            conn.commit()
        except Exception as e:
            traceback.print_exc()
            conn.rollback()
            raise MySQLError
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @staticmethod
    def select_all_to_pd(sql, db_pool=adb_pool):
        conn = None
        try:
            conn = db_pool.connection()
            return pd.read_sql(sql, conn)
        except Exception as e:
            traceback.print_exc()
            conn.rollback()
            raise MySQLError
        finally:
            if conn:
                conn.close()
