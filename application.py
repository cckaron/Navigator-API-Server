#!/usr/bin/env python3
import connexion
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import AwsConfig as config

import urllib.request
import urllib.parse
from urllib.error import URLError

from api import tasks

# Create the application instance
application = connexion.App(__name__, specification_dir=config.CONNEXION_DIR)

# Read the swagger.yml file to configure the endpoints
application.add_api(config.CONNEXION_YAML, pythonic_params=True)

#specify db config
flaskApp = application.app
flaskApp.config.from_object(config())

#SQLAlchemy
db = SQLAlchemy(flaskApp)
#Migration tool
migrate = Migrate(flaskApp, db)



# Create a URL route in our application for "/"
@application.route('/', methods=['GET', 'POST'])
def home():
    def SMS_publish(dstaddr, smbody):
        data = {}
        # data['username'] = 'cckaron28'
        data['id'] = 'cckaron28'
        data['password'] = 'Chaosin003'
        data['longsms'] = 1
        # data['dstaddr'] = dstaddr
        data['tel'] = dstaddr
        # data['smbody'] = smbody
        data['msg'] = smbody
       
        url_values = urllib.parse.urlencode(data)
        # url='https://api.kotsms.com.tw/kotsmsapi-1.php'
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

    if request.method == 'POST':
        import googlemaps
        
        #Google Maps
        gmaps = googlemaps.Client(key='AIzaSyBAHYSAVo_NiC6S6IMFx4-G7jSZI1GXyak')
        
        #addTask
        body = {}

        #Departure Point
        departure = request.values['departure']
        departure_query = gmaps.geocode(departure)
        body['departure_latitude'] = departure_query[0]['geometry']['location']['lat']
        body['departure_longitude'] = departure_query[0]['geometry']['location']['lng']

        #Accident Point
        accident = request.values['accident']
        accident_query = gmaps.geocode(accident)
        body['accident_latitude'] = accident_query[0]['geometry']['location']['lat']
        body['accident_longitude'] = accident_query[0]['geometry']['location']['lng']
        
        #Hospital Point
        hospital = request.values['hospital']
        hospital_query = gmaps.geocode(hospital)
        body['hospital_latitude'] = hospital_query[0]['geometry']['location']['lat']
        body['hospital_longitude'] = hospital_query[0]['geometry']['location']['lng']
        
        #call Api
        rtn = tasks.addTask(body)
        taskId = rtn['taskId']

        print(taskId)

        #導航app
        # nav_str = '救護車駕駛您好！\n性別女/26歲/呼吸喘\n點選下方連結顯示導航路線:\n' + 'kwnaviking3d://navigation?taskid=' + taskId
        nav_str = 'New Case: ' + 'kwnaviking3d://navigation?taskId=' + taskId + " [119 Center] "
        # SMS_publish('0966013000', nav_str)
        # SMS_publish('0909827671', nav_str)


        #網站app
        # web_str = '親愛的市民您好!救災救護車已在前往案發地點途中,請耐心等候並於到達時協助引導, 若有任何問題亦請再撥打119, 並可利用視訊119App報案,以利本局掌握現場概況,台北市政府消防局關心您！點選下方連結可檢視消防車輛所在位置：\n' + 'https://wv-hackathon.azurewebsites.net/?taskId=' + taskId
        web_str = 'New Case: '+'https://wv-hackathon.azurewebsites.net/?taskId=' + taskId + " [119 Center] "
        req_url = 'https://wv-hackathon.azurewebsites.net/?taskId=' + taskId
        print(request.values['phone'])
        SMS_publish(request.values['phone'], web_str)

        return redirect(req_url)

    else:
        return render_template('input_page.html')   

#testing
@application.route('/test')
def index():
    task = tasks.findLatest()
    url = 'kwnaviking3d://navigation?taskId='+ task.id
    print(url)
    print(task.id)
    return redirect(url)

if __name__ == '__main__':
    application.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)    