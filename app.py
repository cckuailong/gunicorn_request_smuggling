from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "INDEX\n"

@app.route("/admin")
def admin():
    return "ADMIN\n"

@app.route("/forbidden")
def forbidden():
    return "FORBIDDEN\n"

if __name__ == "__main__":
    app.run()
