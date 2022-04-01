from flask import render_template
from . import web


# 旅行页
@web.route('/travel')
def travel():
    return render_template('travel.html')
