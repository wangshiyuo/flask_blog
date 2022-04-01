from flask import render_template
from app.libs.get_content import get_index
from . import web


# 个人主页
@web.route('/personal/')
def personal():
    context = get_index(1)
    return render_template('personal.html', **context)
