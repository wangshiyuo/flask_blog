from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

class Article(db.Model):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    label = Column(String(100), nullable=False)
    title = Column(String(1024),nullable=False)
    content = Column(Text,nullable=False)
    create_time = Column(DateTime,default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)
    read_times = Column(Integer,nullable=False)


class Dynamic(db.Model):
    __tablename__ = 'dynamic'
    id = Column(Integer,primary_key=True,autoincrement=True)
    content = Column(Text, nullable=False)
    create_time = Column(DateTime,default=datetime.now)


class Commenary(db.Model):
    __tablename__ = 'commenary'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(40), unique=True, nullable=False)
    content = Column(VARCHAR(255), nullable=False)
    create_time = Column(DateTime,default=datetime.now)
    article_id = Column(Integer,ForeignKey('article.id'))
    article = relationship('Article', backref=backref('commenarys',order_by = create_time.desc()))
