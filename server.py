from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import threading
import os


# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))  # base directory
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# db class
class POST(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(100))
    close = db.Column(db.Float)

    def __init__(self, id, time, close):
        self.id = id
        self.time = time
        self.close = close


# Schema
class PostSchema(ma.Schema):
    class Meta:
        fields = ('close', 'time')


# Init schema
post_schema = PostSchema()
posts_schema = PostSchema(many=True)


def background():
    """Function that collects and stores all 4 hour closes in database
    """

    # background process
    """while True:
        
    """
    pass


@app.route('/data1', methods=['GET'])
def currentclose():
    candle = db.session.query(POST).order_by(POST.id.desc()).first()
    return post_schema.jsonify(candle)


@app.route('/data2', methods=['GET'])
def fourhourclose():
    data = db.session.query(POST).all()
    return posts_schema.jsonify(data)

@app.route('/data3', methods=['GET'])
def fourhourclose():
    data = db.session.query(POST).all()
    return posts_schema.jsonify(data)


def main():
    threading.Thread(target=background).start()
    threading.Thread(target=app.run(host='0.0.0.0', port=8080,
                     debug=True, threaded=True)).start()


# run api endpoint
if __name__ == '__main__':
    main()