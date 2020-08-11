import urllib.request
import urllib.parse
from urllib.error import URLError

def publish(dstaddr, smbody):
        data = {}
        data['id'] = 'cckaron28'
        data['password'] = 'Chaosin003'
        data['longsms'] = 1
        data['tel'] = dstaddr
        data['msg'] = smbody
       
        url_values = urllib.parse.urlencode(data)
        url = 'http://api.message.net.tw/send.php'
        full_url = url + '?' + url_values

        print(full_url)

        try:
            data = urllib.request.urlopen(full_url)
            print(data.read())
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)