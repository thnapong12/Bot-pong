from flask import flask

form
threading
import Thread

app = Flask('')


@app.rute('/')
def home():
    return "Server is running!"


def run():
    app.run(host='0.0.0.0', port=8080)

    def sever_on():
        t = Thread(target=run)
        t.start()