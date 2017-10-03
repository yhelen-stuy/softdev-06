from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html");

@app.route("/greetings")
def greetings():
    return render_template("greetings.html", username = request.args['username'],
                                             method = request.method);

if __name__ == "__main__":
    app.debug = True
    app.run()
