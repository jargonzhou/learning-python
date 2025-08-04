# 配置项

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """配置类"""
    # JWT密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # 邮箱服务器
    # Google: https://support.google.com/a/answer/176600?hl=en
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in [
        'true', '1', 'on']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    APP_MAIL_SUBJECT_PREFIX = '[example_app]'
    APP_MAIL_SENDER = 'Admin <example_app@example.com>'
    APP_ADMIN = os.environ.get('APP_ADMIN')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 记录查询
    SQLALCHEMY_RECORD_QUERIES = True
    # 数据库慢查询时间
    APP_SLOW_DB_QUERY_TIME = 0.5

    # 帖子分页大小
    APP_POSTS_PER_PAGE = 10
    # 帖子评论分页大小
    APP_COMMENTS_PER_PAGE = 10
    # 关注人分页大小
    APP_FOLLOWERS_PERPAGE = 10

    @staticmethod
    def init_app(app):
        """初始化应用"""
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # 日志
        import logging
        from logging import StreamHandler

        file_handler = StreamHandler()
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        format = '%(asctime)s [%(levelname)s] [%(processName)s %(threadName)s %(taskName)s] %(pathname)s %(funcName)s: %(message)s'
        logging.basicConfig(level=logging.DEBUG,
                            format=format,
                            handlers=[file_handler])
        app.logger.addHandler(file_handler)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class DockerConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # 日志
        import logging
        from logging import StreamHandler
        from pythonjsonlogger.json import JsonFormatter

        file_handler = StreamHandler()
        # JSON格式
        formatter = JsonFormatter(
            "{asctime}{levelname}{message}", style="{",
            rename_fields={"levelname": "LEVEL"})
        file_handler.setFormatter(formatter)
        # file_handler.setLevel(logging.INFO)
        logging.basicConfig(level=logging.INFO, handlers=[file_handler])
        # app.logger.handlers = []
        app.logger.addHandler(file_handler)


# 配置实例
config = {
    # 开发配置
    'development': DevelopmentConfig,
    # 测试配置
    'testing': TestingConfig,
    # 生产配置
    'production': ProductionConfig,
    # Docker配置
    'docker': DockerConfig,
    # 默认配置
    'default': DevelopmentConfig
}
