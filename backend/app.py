from flask import Flask
from flask_cors import CORS
from pastpaperapi import create_app
import time
from keep_alive import keep_alive

app = create_app()

while True:
    keep_alive()
    time.sleep(600)

if __name__ == '__main__':
    app.run(debug=True)



# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


