from flask import Flask
app = Flask(__name__)

#goes to domain
@app.route("/")

def home():
    return "Hello! Im going to die! <h1>AHH<h1>"

@app.route("/<name>")
def user(name):
    return "hello \"{name}\"!"

if __name__ == "__main__":
    app.run()

