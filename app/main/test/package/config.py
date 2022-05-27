import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """默认配置
    """
    # 应用参数
    APP_NAME = 'flask-web'
    SERVER_PORT = 9260
    #
    FLATPAGES_AUTO_RELOAD = True
    FLATPAGES_EXTENSION = '.md'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'can you guess it'
    DEBUG = True

    # sqlalchemy两个主要配置
    # 关闭数据库时是否自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 是否追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 是否开启任务调度器,默认不开启
    SCHEDULER_OPEN = False
    SCHEDULER_API_ENABLED = False
    # 任务调度器lock文件名称
    SCHEDULER_LOCK_FILE_NAME = 'scheduler-{}.lock'.format(APP_NAME)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """开发环境配置
    """
    ADB_HOST = 'localhost'
    ADB_PORT = 3306
    ADB_USER = 'root'
    ADB_PASSWD = 'JJF'
    ADB_DB = 'db_model'
    ADB_CHARSET = 'utf8'
    ADB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset={}'.format(ADB_USER, ADB_PASSWD, ADB_HOST, ADB_PORT, ADB_DB,
                                                                 ADB_CHARSET)
    # sqlalchemy ORM底层所访问数据库URI
    SQLALCHEMY_DATABASE_URI = ADB_URL


class TestConfig(Config):
    """测试环境配置
    """


class UatConfig(Config):
    """UAT环境配置
    """


class ProductionConfig(Config):
    """生产环境配置
    """


# 设置环境配置映射
config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'uat': UatConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


def get_active_config():
    """获取当前生效的环境配置类

    :return: 当前生效的环境配置类
    """
    config_name = os.getenv('FLASK_CONFIG') or 'default'
    return config[config_name]


def get_active_config_name():
    """获取当前生效的环境配置名称

    :return: 当前生效的环境配置名称
    """
    config_name = os.getenv('FLASK_CONFIG') or 'default'
    return config_name
