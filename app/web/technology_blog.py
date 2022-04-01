from flask import request, render_template
from app.libs.get_content import get_technology_blog
from . import web


# 技术分享页
@web.route('/technology_blog/')
def technology_blog():
    page = request.args.get('page', 1, type=int)
    context = get_technology_blog(page)
    if context:
        return render_template('index.html',**context)
    else:
        return render_template('zero_index.html')
