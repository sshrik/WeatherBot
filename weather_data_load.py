import urllib.request as urllib 
import json
 

def load_city(city_name):
    '''
    Args    : city_name - string of city name.
    Returns : main_data - temp, pressure, humidity, temp_min, temp_max + weather.
    '''
    j = get_data_with_city(city_name)
    main_data = []
    main_data.append(j["main"])
    main_data.append(j["weather"])

    return main_data

def load_city_all(city_name):
    '''
    Args    : city_name - string of city name.
    Returns : main_data - temp, pressure, humidity, temp_min, temp_max  + weather, Visibility
            :           - wind, wind_speed, wind_deg.
    '''
    j = get_data_with_city(city_name)
    main_data = []
    main_data.append(j["main"])
    main_data.append(j["weather"])
    return main_data

def get_data_with_city(city_name):
    '''
    Args    : city_name - string of city name.
    Returns : j         - json data.
    '''
    url = 'http://api.openweathermap.org/data/2.5/weather?q='
    api_key = '&appid=071397f1bec9748388ca67cc3532b503'

    url = url + city_name + api_key
    main_data = 0

    u = urllib.urlopen(url)
    data = u.read()

    j = json.loads(data.decode('utf-8'))

    return j
