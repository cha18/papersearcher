from flask import Flask
from flask_cors import CORS
from flaskystuff import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


