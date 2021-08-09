#!/usr/bin/python3
import time
import requests
  
URL= "http://api.open-notify.org/iss-now.json"
def main():
    # requests.get() sends GET request to the URL
    # .json() strips JSON off the response and translates into Python!
    resp= requests.get(URL).json()
    iss_time =  time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(resp['timestamp']))
    iss_pos = resp['iss_position']
    iss_lon = iss_pos['longitude']
    iss_lan = iss_pos['latitude']
    print(f""""CURRENT LOCATION OF THE ISS:
        Timestamp: {iss_time}
        Lon: {iss_lon}
        Lat: {iss_lan}
        City: Saint-Pierrerint(resp)""")
    
main()
