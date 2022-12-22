from flask import Flask

app = Flask(__names__)

@app.route("/")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()

