from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


stations = pd.read_csv("data_small/stations.txt", skiprows = 17)
stations = stations[['STAID', 'STANAME                                 ']]

@app.route("/")
def home():
    # return render_template("translator.html")
    return render_template("home.html", data = stations.to_html())

@app.route("/app/v1/<station>")
def weather_data_station(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) +".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df = df[["    DATE",'   TG']]
    df = df.to_dict(orient="records")
    return df

@app.route("/app/v1/yearly/<station>/<year>")
def weather_data_year(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))]
    result = result.to_dict(orient="records")
    return result


@app.route("/app/v1/<station>/<date>")
def weather_data(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) +".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]['   TG'].squeeze()/10
    return {"station": station,
            "date": date,
            "temperature": temperature}

# @app.route("/contact/")
# def contact():
#     return render_template("contact.html")

@app.route("/app/v1/<word>")
def translator(word):
    filename = "data_small/dictionary.csv"
    df = pd.read_csv(filename)
    meaning = df.loc[df['word'] == word]['definition'].squeeze()
    # meaning = word.upper()
    return {"word": word,
            "meaning": meaning}

if __name__ == "__main__":
    app.run(debug=True)