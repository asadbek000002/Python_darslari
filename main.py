import requests
url = 'http://api.weatherapi.com/v1'
r = requests.get(url + '/current.json', params={'key':'f32b2cd7fe364abd8d8182803230603', 'q': 'Tashkent'})
coin = r.json()

for i in coin:
    print(i,':')
    for key,value in coin[i].items():
        print(" ", key,value)

    print("\n")
