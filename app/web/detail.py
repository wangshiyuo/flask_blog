from flask import session, render_template
from app.libs.get_content import get_detail
from app.models.all_models import db
from ..models.all_models import Article
from . import web


#文章详细页
@web.route('/detail/<int:article_id>')
def detail(article_id):
    #游客每次点击阅读原文，阅读数加1
    if session.get('user_id') != 1:
        article1 = Article.query.filter(Article.id == article_id).first()
        article1.read_times += 1
        db.session.commit()

    context = get_detail(article_id)
    return render_template('detail.html',**context)