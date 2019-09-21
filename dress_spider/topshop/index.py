# -*- coding: utf-8 -*-
'''
@Author: zhou
@Date : 2019/9/7 下午11:49
@Desc :
'''
from datetime import datetime

from flask import Flask, render_template, flash, redirect, url_for, abort, request
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'topshop',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine(app)

class Clothing(db.DynamicDocument):
    name = db.StringField(required=True, max_length=200)
    unitPrice = db.StringField()
    seoUrl = db.StringField()
    productBaseImageUrl = db.StringField()
    content = db.StringField()
    outfitBaseImageUrl = db.StringField()
    created_at = db.DateTimeField(default=datetime.now())

    meta = {
        'collection': 'clothing',
        'ordering': ['-created_at']
    }

    def __repr__(self):
        return '<News %r>' % self.title


@app.route("/")
@app.route("/<int:page>")
def index(page=None):
    if page is None:
        page = 1
    page_data = Clothing.objects.paginate(page=page, per_page=12)
    return render_template("index.html", page_data=page_data,page=page)


if __name__ == "__main__":
    app.run(debug=True)
