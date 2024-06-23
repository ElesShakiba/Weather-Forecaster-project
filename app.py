import requests
from flask import Flask ,request,render_template
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index ():
    if request.method == 'POST':
        city = request.form['city']
        api_key = '00edc2ccf69244eaf25aa870ba0db7af'
        base_url = 'https://api.openweathermap.org/data/2.5/weather?'
        params = {'q': city, 'appid': api_key, 'units': 'metric'}
        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if data["cod"] == 200:
               weather_description = data['weather'][0]['description']
               temp = data['main']['temp']
               humidity = data['main']['humidity']
               wind_speed = data['wind']['speed'] 

               weather_info={
                   'description':weather_description,
                   'temperature':temp,
                   'humidity':humidity,
                   'wind_speed':wind_speed,
                   'city':city
               }    
               return render_template ('index.html',weather=weather_info)
            else:
                error_message=data['message']
                return render_template('index.html',error=error_message)
        except Exception as e:
            error_message = str(e)
            return render_template ('index.html',error=error_message)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
              

