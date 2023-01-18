from flask import Flask, request

app = Flask("sample_web_app")


@app.route("/")
def homepage():
    return "<p style='color: red'>Hello, World!</p>"


@app.route("/<string:username>")
def get_user_data(username):
    return f"Hi, {username}!"


if __name__ == '__main__':
    app.run()
