from flask import Flask,render_template
from bucket import bucket_api
from comments import comments_api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(bucket_api, url_prefix='/bucket')
app.register_blueprint(comments_api, url_prefix='/comments')



@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run('0.0.0.0', port=5050, debug=True)