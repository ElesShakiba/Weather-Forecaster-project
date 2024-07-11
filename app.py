import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city1 = request.form['city1']
        city2 = request.form['city2']
        api_key = '00edc2ccf69244eaf25aa870ba0db7af'
        base_url = 'https://api.openweathermap.org/data/2.5/weather?'
        params1 = {'q': city1, 'appid': api_key, 'units': 'metric'}
        params2 = {'q': city2, 'appid': api_key, 'units': 'metric'}

        weather_info = {}

        try:
            response1 = requests.get(base_url, params=params1)
            data1 = response1.json()
            response2 = requests.get(base_url, params=params2)
            data2 = response2.json()

            if data1["cod"] == 200 and data2["cod"] == 200:
                weather_info['city1'] = {
                    'description': data1['weather'][0]['description'],
                    'temperature': data1['main']['temp'],
                    'humidity': data1['main']['humidity'],
                    'wind_speed': data1['wind']['speed'],
                    'name': city1
                }
                weather_info['city2'] = {
                    'description': data2['weather'][0]['description'],
                    'temperature': data2['main']['temp'],
                    'humidity': data2['main']['humidity'],
                    'wind_speed': data2['wind']['speed'],
                    'name': city2
                }
                return render_template('index.html', weather=weather_info)
            else:
                error_message = data1.get('message', 'Error') if data1["cod"] != 200 else data2.get('message', 'Error')
                return render_template('index.html', error=error_message)
        except Exception as e:
            error_message = str(e)
            return render_template('index.html', error=error_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
