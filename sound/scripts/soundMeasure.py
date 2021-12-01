import requests

ip_address = '' # Usually 192.168.212.X. Find X in oscilloscope settings

if (ip_address == ''):
    print('Setup ip-address of Tekronix oscilloscope')
    quit()

url = 'http://' + ip_address + '/Image.png'
r = requests.get(url, allow_redirects=True)

open('tektronix.png', 'wb').write(r.content)