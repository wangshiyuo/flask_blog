from . import web
from flask import render_template, request
from app.libs.get_content import get_index


# 首页
@web.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    context = get_index(page)
    if context:
        return render_template('index.html', **context)
    else:
        return render_template('zero_index.html')
