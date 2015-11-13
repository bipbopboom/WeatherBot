import forecastio
import time
import requests

api_key = <YOUR_API_KEY_HERE>
lat = <YOUR_LATITUDE_HERE>
lng =  <YOUR_LONGITUDE_HERE>

forecast = forecastio.load_forecast(api_key, lat, lng)
localtime = time.asctime(time.localtime(time.time()))
byDay = forecast.daily()
dailyData = byDay.data #A list of forecast objects for the next seven days
today = dailyData[0] #Today

date = localtime
result == (date)
result += ("\n"+today.summary+"\nHIGH: "+str(int(today.temperatureMax))+"\tLOW: "+str(int(today.temperatureMin)))
result += ("\nWIND: "+str(int(today.windSpeed))+" MPH")
#print(result)

url = <YOUR_URL_HERE>
payload={"text": result}
requests.post(url=url, data=None , json=payload)
