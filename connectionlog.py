from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from time import sleep
import time
from sense_hat import SenseHat

sense = SenseHat()
G = (0, 50, 0)
R = (255,0,0)
X = (0,0,0)

sense.set_rotation(180)
up = [
    X, X, G, G, G, G, X, X,
    X, G, X, X, X, X, G, X,
    G, X, G, X, X, G, X, G,
    G, X, X, X, X, X, X, G,
    G, X, G, X, X, G, X, G,
    G, X, X, G, G, X, X, G,
    X, G, X, X, X, X, G, X,
    X, X, G, G, G, G, X, X,
    ]

down = [
    X, X, R, R, R, R, X, X,
    X, R, R, R, R, R, R, X,
    R, R, R, R, R, R, R, R,
    R, X, X, X, X, X, X, R,
    R, X, X, X, X, X, X, R,
    R, R, R, R, R, R, R, R,
    X, R, R, R, R, R, R, X,
    X, X, R, R, R, R, X, X,
    ]

req = Request("http://www.google.com")
outage = 0


while True:
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        outage += 1
        sense.set_pixels(down)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        outage += 1
        sense.set_pixels(down)
    else:
        print ('Connected')
        if outage >= 1:
            print ('No connection for: ' + str(outage) + 'min at '+ time.strftime("%d/%m/%Y %H:%M"))
            myfile = open('outage_log.txt','a')
            myfile.write('No connection for: ' + str(outage) + ' min at '+ time.strftime("%d/%m/%Y %H:%M"))
            myfile.write('\n')
            myfile.close()
        sense.set_pixels(up)
        outage = 0
    sleep(60)
