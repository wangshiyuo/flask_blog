import datetime
import os
import random
from flask import request, render_template, session, redirect, url_for, make_response, flash
import secure
from . import web
from functools import wraps
from app.models.all_models import db
from ..models.all_models import Dynamic, Article, Commenary
from app.libs.get_content import get_index


# 登录限制的装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('web.login'))

    return wrapper


# 登录(账号密码信息已保存在配置信息中)
@web.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        # 验证登录信息(账号密码保存在参数文件中)
        if username and password:
            if username == secure.USERNAME_LOGIN and password == secure.PASSWORD_LOGIN:
                session['user_id'] = 1  # 保存用户id信息
                # session.permanent = True
                flash('登录成功！')
                return redirect(url_for('web.back_index'))
            else:
                flash('账号或密码错误，请重新输入！')
                return redirect(url_for('web.login'))
        else:
            flash('账号或密码不能为空！')
            return redirect(url_for('web.login'))


# 注销(退出登录状态)
@web.route('/logout/')
@login_required
def logout():
    session.clear()
    return redirect(url_for('web.index'))


# 后台首页
@web.route('/back_index/', methods=['GET', 'POST'])
@login_required
def back_index():
    if request.method == 'GET':
        context = get_index(1)
        return render_template('back_index.html', **context)
    else:
        content = request.form.get('content')
        dynamic = Dynamic(content=content)
        db.session.add(dynamic)
        db.session.commit()
        return redirect(url_for('web.back_index'))


# 后台列表页
@web.route('/back_list/')
@login_required
def back_list():
    context = get_index(1)
    return render_template('back_list.html', **context)


# 后台文章编辑页
@web.route('/back_edit/', methods=['GET', 'POST'])
@login_required
def back_edit():
    if request.method == 'GET':
        context = get_index(1)
        return render_template('back_edit.html', **context)
    else:
        label = request.form.get('label')
        title = request.form.get('title')
        content = request.form.get('editor1')
        read_times = 0
        article = Article(label=label, title=title, content=content, read_times=read_times)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('web.back_index'))


# 后台文章编辑功能
@web.route('/back_update/<article_id>', methods=['GET', 'POST'])
@login_required
def back_update(article_id):
    article1 = Article.query.filter(Article.id == article_id).first()
    if request.method == 'GET':
        return render_template('back_update.html', article1=article1)
    else:
        article1 = Article.query.filter(Article.id == article_id).first()
        article1.label = request.form.get('label')
        article1.title = request.form.get('title')
        article1.content = request.form.get('editor1')
        article1.create_time = article1.create_time
        article1.update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        article1.read_times = article1.read_times
        db.session.commit()
        flash('文章保存成功！')
    return redirect(url_for('web.back_list'))


# 后台文章删除功能
@web.route('/back_drop/<article_id>', methods=['GET', 'POST'])
@login_required
def back_drop(article_id):
    while Commenary.query.filter(Commenary.article_id == article_id).first():
        commentary1 = Commenary.query.filter(Commenary.article_id == article_id).first()
        db.session.delete(commentary1)  # 首先删除文章对应的评论

    article1 = Article.query.filter(Article.id == article_id).first()
    db.session.delete(article1)
    db.session.commit()
    flash('文章删除成功！')
    return redirect(url_for('web.back_list'))


# 文章图片上传命名函数
def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))


# CKEditor文本编辑器
@web.route('/ckupload/', methods=['POST', 'OPTIONS'])
def ckupload():
    """CKEditor file upload"""
    error = ''
    url = ''
    callback = request.args.get("CKEditorFuncNum")

    if request.method == 'POST' and 'upload' in request.files:
        fileobj = request.files['upload']
        fname, fext = os.path.splitext(fileobj.filename)
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)

        filepath = os.path.join(web.static_folder, 'upload', rnd_name)

        # 检查路径是否存在，不存在则创建
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
            except:
                error = 'ERROR_CREATE_DIR'
        elif not os.access(dirname, os.W_OK):
            error = 'ERROR_DIR_NOT_WRITEABLE'

        if not error:
            fileobj.save(filepath)
            url = url_for('static', filename='%s/%s' % ('upload', rnd_name))
    else:
        error = 'post error'

    res = """<script type="text/javascript">
  window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
</script>""" % (callback, url, error)

    response = make_response(res)
    response.headers["Content-Type"] = "text/html"
    return response


# 上下文处理器钩子函数(设置的是登录后显示用户名)
@web.context_processor
def my_context_processor():
    user_id = session.get('user_id')  # 如果存在user_id则已成功登录，返回用户名user
    if user_id:
        return {'user': 'ln'}
    return {}
