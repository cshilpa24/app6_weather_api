from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/app/v1/<station>/<date>")
def weather_data(station, date):
    temperature = 23
    return {"station": station,
            "date" : date,
            "temperature": temperature}

# @app.route("/contact/")
# def contact():
#     return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)