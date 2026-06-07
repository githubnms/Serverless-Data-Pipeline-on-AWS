from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL="https://YOUR_API_GATEWAY_URL/dev/submit"

@app.route("/",methods=["GET","POST"])

def home():

    if request.method=="POST":

        data={

            "id":request.form["id"],

            "name":request.form["name"],

            "email":request.form["email"],

            "phone":request.form["phone"],

            "address":request.form["address"],

            "country":request.form["country"],

            "city":request.form["city"],

            "zipcode":request.form["zipcode"],

            "message":request.form["message"]

        }

        response=requests.post(
            API_URL,
            json=data
        )

        return response.text

    return render_template(
        "index.html"
    )


app.run(
host="0.0.0.0",
port=5000
)