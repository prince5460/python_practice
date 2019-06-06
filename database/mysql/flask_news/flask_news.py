# coding=utf-8
from datetime import datetime

from flask import Flask, render_template, flash, redirect, url_for, abort, request
from flask_sqlalchemy import SQLAlchemy

from forms import NewsForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:zhou123@localhost:3306/net_news'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a random string'

db = SQLAlchemy(app)


class News(db.Model):
    """ 新闻模型 """
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    types = db.Column(db.String(10), nullable=False)
    image = db.Column(db.String(300), )
    author = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/')
def index():
    """ 新闻首页 """
    news_list = News.query.filter_by(is_valid=1)
    return render_template("index.html", news_list=news_list)


@app.route('/cat/<name>/')
def cat(name):
    """ 新闻类别页面 """
    news_list = News.query.filter(News.types == name)
    return render_template('cat.html', name=name, news_list=news_list)


@app.route('/detail/<int:pk>/')
def detail(pk):
    """ 新闻详情页 """
    news_obj = News.query.get(pk)
    return render_template('detail.html', news_obj=news_obj)


@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    """ 后台管理首页 """
    news_list = News.query.filter_by(is_valid=1).paginate(page=page, per_page=5)
    return render_template("admin/index.html", news_list=news_list)


@app.route('/admin/add/', methods=['GET', 'POST'])
def add():
    """ 新增新闻 """
    form = NewsForm()
    if form.validate_on_submit():
        # 获取数据
        new_obj = News(
            title=form.title.data,
            content=form.content.data,
            types=form.types.data,
            image=form.image.data,
            created_at=datetime.now()
        )
        # 保存数据
        db.session.add(new_obj)
        db.session.commit()
        flash('添加成功')
        return redirect(url_for('admin'))
    return render_template("admin/add.html", form=form)


@app.route('/admin/update/<int:pk>/', methods=['GET', 'POST'])
def update(pk):
    """ 修改新闻 """
    obj = News.query.get(pk)
    if not obj:
        return redirect(url_for('admin'))
    form = NewsForm(obj=obj)
    if form.validate_on_submit():
        obj.title = form.title.data
        obj.content = form.content.data
        obj.types = form.types.data
        obj.image = form.image.data

        db.session.add(obj)
        db.session.commit()
        flash('修改成功')
        return redirect(url_for('admin'))

    return render_template("admin/update.html", form=form)


@app.route('/admin/delete/<int:pk>/', methods=['POST'])
def delete(pk):
    '''删除新闻'''
    new_obj = News.query.get(pk)
    if not new_obj:
        return 'no'
    new_obj.is_valid = False
    db.session.add(new_obj)
    db.session.commit()
    # flash('删除成功')
    # return redirect(url_for('admin'))
    return 'yes'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
