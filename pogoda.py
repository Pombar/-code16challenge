import requests
api_key = "" # tu wklej API dostępny po rejestracji na openweathermap
miasto = input("W jakim mieście przebywasz? ") 
guest_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q=" + miasto 
dawid_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q=Corralejo"
guest_response = requests.get(guest_url) 
dawid_response = requests.get(dawid_url) 
guest_json = guest_response.json() 
dawid_json = dawid_response.json() 
guest = guest_json["main"] 
dawid = dawid_json["main"] 
if dawid["temp"]  > guest["temp"] :
    diff = round(dawid["temp"] - guest["temp"])
    print("U Dawida jest cieplej o {diff}{stopnie}C ;)".format(diff=diff, stopnie = u'\N{DEGREE SIGN}'))
else:
    print("Wow, musi Ci być całkiem ciepło!")
