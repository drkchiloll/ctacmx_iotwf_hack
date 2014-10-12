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
# zonefile = open('../documents/zones.txt', 'w')
# zonecoordsfile = open('../documents/zonecords.txt','w')
while True:
    req = requests.get(url,headers=headers,verify=False,auth=(user,pwd))
    data = json.loads(req.content)
    zonefile = open('../documents/zones.txt', 'w')
    zonecoordsfile = open('../documents/zonecords.txt','w')
    for loc in data:
        entries = data[loc]['entries']
        # print entries
        z1,z2,z3 = [],[],[]
        z1coords,z2coords,z3coords = [],[],[]
        # z2 = []
        # z3 = []
        for obj in entries:
            coordX = obj['MapCoordinate']['x']
            coordY = obj['MapCoordinate']['y']
            if coordY > zones[2]:
                continue
            elif coordY > 0 and coordY < 30:
                z1.append(coordY)
                z1coords.append('X: '+str(coordX)+' , Y: '+str(coordY))
                # zonecoordsfile.write('Zone 1 Coords.\n')
                # zonecoordsfile.write('X: '+str(coordX)+'\n'+'Y: '+str(coordY)+'\n')
            elif coordY > 30 and coordY < 51:
                z2coords.append('X: '+str(coordX)+' , Y: '+str(coordY))
                z2.append(coordY)
                # zonecoordsfile.write('Zone 2 Coords.\n')
                # zonecoordsfile.write('X: '+str(coordX)+'\n'+'Y: '+str(coordY)+'\n')
            elif coordY > 51 and coordY < 91:
                # zonecoordsfile.write('Zone 3 Coords.\n')
                # zonecoordsfile.write('X: '+str(coordX)+'\n'+'Y: '+str(coordY)+'\n')
                z3.append(coordY)
                z3coords.append('X: '+str(coordX)+' , Y: '+str(coordY))
    zonefile.write('Zone 1: '+ str(len(z1)))
    zonefile.write('\n')
    zonefile.write('Zone 2: '+ str(len(z2)))
    zonefile.write('\n')
    zonefile.write('Zone 3: '+ str(len(z3)))
    zonefile.close()
    print len(z1)
    print len(z2)
    print len(z3)
    zonecoordsfile.write('Zone 1:\n');
    for zcoord in z1coords:
        zonecoordsfile.write(zcoord)
        zonecoordsfile.write('\n');
    zonecoordsfile.write('Zone 2:\n');
    for zcoord in z2coords:
        zonecoordsfile.write(zcoord)
        zonecoordsfile.write('\n');
    zonecoordsfile.write('Zone 3:\n');
    for zcoord in z3coords:
        zonecoordsfile.write(zcoord)
        zonecoordsfile.write('\n');
    zonecoordsfile.close()
    time.sleep(5)