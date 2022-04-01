from flask import request, render_template
from app.libs.get_content import get_project
from . import web


#随笔杂谈页
@web.route('/projects/')
def projects():
    page = request.args.get('page', 1, type=int)
    context = get_project(page)
    if context:
        return render_template('index.html',**context)
    else:
        return render_template('zero_index.html')