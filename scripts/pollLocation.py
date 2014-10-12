import json
import requests
import time

url = 'https://10.10.20.11/api/contextaware/v1/location/clients'
user = 'learning'
pwd = 'learning'
headers = {
    'Content-type' : 'application/json',
    'Accept' : 'application/json'
}
zones = [30.74,51.42,90.74]
zonefile = open('zones.txt', 'w')
while True:
    zonefile = open('zones.txt', 'w')
    req = requests.get(url,headers=headers,verify=False,auth=(user,pwd))
    data = json.loads(req.content)
    for loc in data:
        entries = data[loc]['entries']
        # print entries
        zone1 = []
        zone2 = []
        zone3 = []
        for obj in entries:
            coord = obj['MapCoordinate']['y']
            if coord > zones[2]:
                continue
            elif coord > 0 and coord < 22:
                zone1.append(coord)
            elif coord > 22 and coord < 42:
                zone2.append(coord)
            elif coord > 42 and coord < 91:
                zone3.append(coord)
    zonefile.write('Zone 1: '+ str(len(zone1)))
    zonefile.write('\n')
    zonefile.write('Zone 2: '+ str(len(zone2)))
    zonefile.write('\n')
    zonefile.write('Zone 3: '+ str(len(zone3)))
    print len(zone1)
    print len(zone2)
    print len(zone3)
    zonefile.close()
    time.sleep(5)