'''
Helen Ye
SoftDev pd7
HW06 Echo
2017-10-02
'''

#import necessities
from flask import Flask, render_template, request
app = Flask(__name__)

#Create a home route for the form
@app.route("/")
def home():
    return render_template("home.html");

#Give a response according to what was inputted
@app.route("/greetings")
def greetings():
    return render_template("greetings.html", username = request.args['username'],
                                             method = request.method);

if __name__ == "__main__":
    app.debug = True
    app.run()
