from flask import render_template
from . import web


# 旅行页
@web.route('/selfie')
def selfie():
    return render_template('404.html')
