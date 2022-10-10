import requests

url = 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
road_type = 'ROAD'
road_type2 = 'PARCEL'
address = '&address='
keys = '&key='
primary_key = 'B441B44D-388E-3ED9-A964-68844EAF7946'

def request_geo(road):
    page = requests.get(url+params+road_type+address+road+keys+primary_key)
    json_data = page.json()
    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x, y
    else:
        x = 0
        y = 0
        return x, y

x, y = request_geo("경기도 시흥시 산기대학로 237 (정왕동, 한국산업기술대학교)")

print(f'x값: {x}')
print(f'y값: {y}')