from flask import request, render_template
from sqlalchemy import desc

from ..models.all_models import Article, Dynamic
from . import web


#面对生活页
@web.route('/life/')
def life():
    page = request.args.get('page', 1, type=int)
    if Article.query.order_by('read_times').first():
        context = {
            'pagination': Article.query.filter(Article.label=='面对生活').order_by(desc(Article.create_time)).
                paginate(page,per_page=5,error_out=False),
            'articles': Article.query.filter(Article.label=='面对生活').order_by(desc(Article.create_time)).
                paginate(page,per_page=5,error_out=False).items,
            'num_article': Article.query.filter(Article.label == '技术分享').count(),
            'num_project': Article.query.filter(Article.label == '随笔杂谈').count(),
            'num_life': Article.query.filter(Article.label == '面对生活').count(),
            'num_2022': Article.query.filter(Article.create_time >= '2022-01-01').filter(
                Article.create_time <= '2022-12-31').count(),
            'num_read': Article.query.order_by(desc(Article.read_times))[0:5],
            'activity': Dynamic.query.order_by(desc(Dynamic.id)).first().content
        }
        return render_template('index.html',**context)
    else:
        return render_template('zero_index.html')