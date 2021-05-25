from django.http import request
from django.shortcuts import render
import requests
def key(id,dictn):
    for keys in dictn.keys():
        if id in dictn[keys]:
            return f"{keys}.jpg"


# Create your views here.
def home(request):

    if request.method == 'POST':

        city = request.POST['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=89d1672ad9365b31700615d1ffce5aa4'
        data = requests.get(url).json()

        id = str(data['weather'][0]['id'])
        back = {
            'storm':[str(i) for i in range(200,235)],
            'driz':[str(i) for i in range(300,322)],
            'rain':[str(i) for i in range(500,532)],
            'snow':[str(i) for i in range(600,670)],
            'mist':[str(i) for i in range(700,790)],
            'clear': '800',
            'cloud':['801','802','803','804'],
        }
        
        payload = {
            'city':data['name'],
            'weather': data['weather'][0]['main'],
            'img': key(id,back),
            'icon': data['weather'][0]['icon'],
            'kel_temp': data['main']['temp'],
            'cel_temp': int(data['main']['temp'])-273,
            'pressure' : data['main']['pressure'],
            'humidity' : data['main']['humidity'],
            'desc': (data['weather'][0]['description']).upper()
        }


        return render(request, 'city.html', {'datas':payload})

    else:

        chen = f'http://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=89d1672ad9365b31700615d1ffce5aa4'
        data_chen = requests.get(chen).json()

        mum = f'http://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=89d1672ad9365b31700615d1ffce5aa4'
        data_mum = requests.get(mum).json()

        payload = {
            'Chennai':{
                'city':data_chen['name'],
                'weather': data_chen['weather'][0]['main'],
                'icon': data_chen['weather'][0]['icon'],
                'cel_temp': int(data_chen['main']['temp'])-273,
            },
            'Mumbai':{
                'city':data_mum['name'],
                'weather': data_mum['weather'][0]['main'],
                'icon': data_mum['weather'][0]['icon'],
                'cel_temp': int(data_mum['main']['temp'])-273,
            }
            
        }

        return render(request, 'index.html', {'data':payload})   