from flask import Flask
from flask_cors import CORS
from pastpaperapi import create_app
import time
from keep_alive import keep_alive
import threading

app = create_app()

def background_task():
    while True:
        keep_alive()
        time.sleep(600)

if __name__ == '__main__':
    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()

    app.run(debug=True)
