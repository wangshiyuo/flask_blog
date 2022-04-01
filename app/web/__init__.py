from flask import Blueprint


web = Blueprint('web', __package__)
from app.web import index
from app.web import personal
from app.web import search
from app.web import technology_blog
from app.web import project
from app.web import life
from app.web import detail
from app.web import commentaries
from app.web import manage
from app.web import food
from app.web import travel
from app.web import selfie