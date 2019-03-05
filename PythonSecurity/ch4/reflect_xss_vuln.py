#!/usr/bin/python

from bottle import route
from bottle import run
from bottle import request
# import html
# from bottle import response


@route('/')
def hello(user=''):
    username = request.query.get('user')
    username = '' if username is None else username
    # username = html.escape(username)  # エスケープ
    # XSSフィルタの有効化
    # response.set_header('X-XSS-Protection', '1; mode=block')
    # CSPを使用
    # response.set_header('Content-Security-Policy', "default-src 'self'")

    html = "<h2> Hello {name} </h2>".format(name=username)

    return html

run(host='0.0.0.0', port=8080, debug=True)
