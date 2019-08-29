# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 19-7-16 下午5:54
@Desc :
'''

from sanic import Sanic
from sanic.log import logger
from sanic.response import text

app = Sanic('test')


@app.route('/')
async def test(request):
    logger.info('Here is your log')
    return text('Hello World!')


if __name__ == "__main__":
    app.run(debug=True, access_log=True)
