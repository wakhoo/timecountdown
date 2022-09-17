from flask import render_template, request, jsonify,Blueprint
from db import db
comments_api = Blueprint('comments_api', __name__,
                        template_folder='templates')


@comments_api.route('/')
def home():
   return render_template('comments.html')

@comments_api.route("/", methods=["POST"])
def homework_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.homework.insert_one(doc)
    return jsonify({'msg':'응원 완료!'})

@comments_api.route("/list", methods=["GET"])
def homework_get():
    comment_list = list(db.homework.find({},{'_id':False}))
    return jsonify({'comments':comment_list})


