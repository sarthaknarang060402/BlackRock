#Python App to run chatbot 

from urllib import response
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
   return render_template("base.html")

@app.get("/pages/Mutual")
def index_get_mutual():
   return render_template("pages/Mutual.html")

@app.get("/pages/sip")
def index_get_sip():
    return render_template("pages/sip.html")

@app.get("/pages/MutualStory")
def index_get_mutual_story():
   return render_template("pages/MutualStory/index.html")

@app.get("/pages/SipStory")
def index_get_sip_story():
   return render_template("pages/SipStory/index.html")


@app.get("/pages/CashFlowJs")
def index_get_cash_flow_game():
   return render_template("pages/CashFlowJs/index.html")

@app.get("/pages/game")
def index_get_cash_flow_simple():
   return render_template("pages/game.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #TODO: check if text is valid 
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

#Used to host and direct IP address
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
