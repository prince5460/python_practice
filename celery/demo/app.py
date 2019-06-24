# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-6-24 下午3:12
@Desc :
'''

from flask import Flask
from celery import Celery

from celeryconfig import broker_url

# 在 Flask 程序中初始化 Celery
# def make_celery(app):
#     celery = Celery(__name__, broker=broker_url)
#     celery.config_from_object('celeryconfig')
#
#     class ContextTask(celery.Task):
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return self.run(*args, **kwargs)
#
#     celery.Task = ContextTask
#     return celery
#
# app = Flask(__name__)
#
# celery = make_celery(app)


# 在使用工厂函数的 Flask 程序中初始化 Celery
celery = Celery(__name__, broker=broker_url)


def create_app():
    app = Flask(__name__)

    register_celery(app)
    return app


def register_celery(app):
    celery.config_from_object('celeryconfig')

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
