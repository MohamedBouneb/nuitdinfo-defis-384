from flask import Flask, jsonify
from flask_cors import CORS
import requests
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
app = Flask(__name__)
@app.route("/weather")
def example():
    api_key = '543a4dc2583bb1b6f3575a77ddae6462'
    city = 'sousse'
    country_code = 'tn'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&appid={api_key}&units=metric'
    response = requests.get(url)
    d = str(datetime.today())
    today=int(d[8:10])
    aftertomrrow=today+2
    tempm=[]
    humm=[]
    temperature = 0  
    humidity = 0 
    def mean(dataset):
        return sum(dataset) / len(dataset)
    if response.ok:
        data = response.json()
        forecast_list = data['list']
        for forecast in forecast_list:
            date_time = forecast['dt_txt']
            date_time=int(date_time[8:11])
            if date_time<aftertomrrow and date_time>today:
                temperature = forecast['main']['temp']
                humidity = forecast['main']['humidity']
                winds= forecast['wind']['speed']
                windd= forecast['wind']['deg']
            if 'rain' in forecast:
                rainvol = forecast['rain']['3h']
            else:
                rainvol=0
            if 'snow' in forecast:
                snowvol = forecast['snow']['3h']
            else:
                snowvol=0 
            description = forecast['weather'][0]['description']
            tempm.append(temperature)
            humm.append(humidity)
    else:
        print('Erreur:', response.status_code, response.text)
    if response.ok :
        temperature=mean(tempm)
        humidity=mean(humm)
    dataset = pd.read_csv('fruits.csv')

    X = dataset[['Mean_Temp', 'Humidity']]
    y = dataset['Fruit'] 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)


    model.fit(X_train, y_train)

    new_weather_conditions = [[temperature,humidity]]
    predicted_fruits = model.predict(new_weather_conditions)
    for i in predicted_fruits:
        predicted_fruits_str=str(i)
    finalfruits = {'fruit': predicted_fruits_str}
    json_data = json.dumps(finalfruits)

    return jsonify(json_data)
CORS(app)
if __name__ == '__main__':
    app.run(debug=True)
