from flask import Flask
from flask_cors import CORS

def create_app(): 
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    CORS(app)

    from .sort import sort
    app.register_blueprint(sort, url_prefix='/')


    return app