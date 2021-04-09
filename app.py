from flask import Flask, request, jsonify, render_template
from predict import predict


app = Flask(__name__)

###############################################################################
#                       SETTING UP APP ROUTES                                 #
###############################################################################


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/response", methods=["GET", "POST"])
def response():

    if request.method == "POST":
        snippet = request.form["fsnippet"]
        # Testing with predict.py
        personality_type = predict(snippet)
    return render_template("response.html", name=personality_type, string=snippet)




###############################################################################
#                                   MAIN                                      #
###############################################################################

if __name__ == "__main__":
    app.run(debug=True)