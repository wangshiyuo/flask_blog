from flask import render_template
from . import web


# 食物页
@web.route('/food')
def food():
    return render_template('food.html')
