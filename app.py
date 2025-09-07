from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask in Docker on AWS EC2!"

if __name__ == "__main__":
    # Important: listen on 0.0.0.0 so it’s accessible outside container
    app.run(host="0.0.0.0", port=5000)

