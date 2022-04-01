from flask import request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from ..models.all_models import Commenary
from . import web

db = SQLAlchemy()


#评论功能
@web.route('/commentaries/',methods=['POST'])
def commentaries():
    name = request.form.get('name')
    article_id = request.form.get('article_id')
    if Commenary.query.filter(Commenary.name == name).first():
        flash('名字重复，请重新输入')
        return redirect(url_for('web.detail', article_id=article_id))
    else:
        content = request.form.get('commentary')
        comments = Commenary(name = name,content = content,article_id = article_id)
        db.session.add(comments)
        db.session.commit()
        flash('评论保存成功')
        return redirect(url_for('web.detail',article_id = article_id))