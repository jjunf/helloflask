import pymysql
from DBUtils.PooledDB import PooledDB

# import config
from app.main.test.package import config

active_config = config.get_active_config()
adb_pool = None
adb_pool_prd = None

if hasattr(active_config, 'ADB_HOST'):
    # 创建数据库连接池。
    # 后续数据库操作应从连接池获取连接，并在操作完成后关闭归还连接。
    adb_pool = PooledDB(
        pymysql,
        2,
        host=active_config.ADB_HOST,
        port=active_config.ADB_PORT,
        user=active_config.ADB_USER,
        passwd=active_config.ADB_PASSWD,
        db=active_config.ADB_DB,
        charset=active_config.ADB_CHARSET
    )
