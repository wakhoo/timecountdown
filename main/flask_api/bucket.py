from flask import render_template, request, jsonify,Blueprint
from db import db
bucket_api = Blueprint('bucket_api', __name__,template_folder='templates',static_folder='static')



@bucket_api.route('/')
def home():
    return render_template('bucket.html',)


@bucket_api.route("/", methods=["POST"])
def bucket_post():
    bucket_receive = request.form["bucket_give"]


    count = list(db.bucket.find({}, {'_id': False}))
    num = len(count) + 1


    doc = {
        'num': num,
        'bucket': bucket_receive,
        'done': 0
    }


    db.bucket.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


@bucket_api.route("/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '버킷완료'})


@bucket_api.route("/list", methods=["GET"])
def bucket_get():
    buckets_list = list(db.bucket.find({},{'_id':False}))
    return jsonify({'buckets':buckets_list})

