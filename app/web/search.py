from flask import request, render_template, flash, redirect, url_for
from sqlalchemy import or_, desc
from . import web
from ..models.all_models import Article


# 查找功能
@web.route('/search/')
def search():
    q = request.args.get('q')
    # 标题或内容
    if Article.query.filter(or_(Article.title.contains(q.strip()), Article.content.contains(q.strip()))).first():
        context = {
            'articles': Article.query.filter(or_(Article.title.contains(q), Article.content.contains(q))).order_by(
                desc(Article.create_time)).all(),
            'num_article': Article.query.filter(Article.label == '技术像').count(),
            'num_project': Article.query.filter(Article.label == '随笔杂谈').count(),
            'num_life': Article.query.filter(Article.label == '面对生活').count(),
            'num_read': Article.query.order_by(desc(Article.read_times))[0:5]
        }
        return render_template('search.html', **context)
    else:
        flash('搜索内容不存在')
        return redirect(url_for('web.index'))
