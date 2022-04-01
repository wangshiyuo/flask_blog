from sqlalchemy import desc
from app.models.all_models import Article, Dynamic, Commenary


# 首页渲染内容
def get_index(page):
    if Article.query.order_by('read_times').first():
        context = {
            'pagination': Article.query.order_by(desc(Article.create_time)).paginate(page,
                                                                                     per_page=5, error_out=False),
            'articles': Article.query.order_by(desc(Article.create_time)).paginate(page,
                                                                                   per_page=5, error_out=False).items,
            'all_articles': Article.query.order_by(desc(Article.create_time)).all(),
            'num_article': Article.query.filter(Article.label == '技术分享').count(),
            'num_project': Article.query.filter(Article.label == '随笔杂谈').count(),
            'num_life': Article.query.filter(Article.label == '面对生活').count(),
            'num_2022': Article.query.filter(Article.create_time >= '2022-01-01').filter(
                Article.create_time <= '2022-12-31').count(),
            'num_read': Article.query.order_by(desc(Article.read_times))[0:5],
            'activity': Dynamic.query.order_by(desc(Dynamic.id)).first().content
        }
        return context


# 文章详情页渲染内容
def get_detail(article_id):
    context = {
        'article_model': Article.query.filter(Article.id == article_id).first(),
        'num_article': Article.query.filter(Article.label == '技术分享').count(),
        'num_project': Article.query.filter(Article.label == '随笔杂谈').count(),
        'num_life': Article.query.filter(Article.label == '面对生活').count(),
        'num_2022': Article.query.filter(Article.create_time >= '2022-01-01').filter(
            Article.create_time <= '2022-12-31').count(),
        'num_read': Article.query.order_by(desc(Article.read_times))[0:5],
        'activity': Dynamic.query.order_by(desc(Dynamic.id)).first().content
    }
    return context


# 技术分享页渲染内容
def get_technology_blog(page):
    if Article.query.order_by('read_times').first():
        context = {
            'pagination': Article.query.filter(Article.label=='技术分享').order_by(desc(Article.create_time)).
                paginate(page,per_page=5,error_out=False),
            'articles': Article.query.filter(Article.label=='技术分享').order_by(desc(Article.create_time)).
                paginate(page,per_page=5,error_out=False).items,
            'num_article': Article.query.filter(Article.label == '技术分享').count(),
            'num_project': Article.query.filter(Article.label == '随笔杂谈').count(),
            'num_life': Article.query.filter(Article.label == '面对生活').count(),
            'num_2022': Article.query.filter(Article.create_time >= '2022-01-01').filter(
                Article.create_time <= '2022-12-31').count(),
            'num_read': Article.query.order_by(desc(Article.create_time))[0:5],
            'activity': Dynamic.query.order_by(desc(Dynamic.id)).first().content
        }
        return context


# 随笔杂谈页渲染内容
def get_project(page):
    if Article.query.order_by('read_times').first():
        context = {
            'pagination': Article.query.filter(Article.label=='随笔杂谈').order_by(desc(Article.create_time)).
                paginate(page,per_page=5,error_out=False),
            'articles': Article.query.filter(Article.label=='随笔杂谈').order_by(desc(Article.create_time)).
                paginate(page,per_page=5,error_out=False).items,
            'num_article': Article.query.filter(Article.label == '技术分享').count(),
            'num_project': Article.query.filter(Article.label == '随笔杂谈').count(),
            'num_life': Article.query.filter(Article.label == '面对生活').count(),
            'num_2022': Article.query.filter(Article.create_time >= '2022-01-01').filter(
                Article.create_time <= '2022-12-31').count(),
            'num_read': Article.query.order_by(desc(Article.read_times))[0:5],
            'activity': Dynamic.query.order_by(desc(Dynamic.id)).first().content
        }
        return context

