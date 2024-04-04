from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from flask import Flask,request
import json

app = Flask(__name__)

@app.route("/",methods=["GET"])
def hello_world():
    # Longitude dan latitude  
    latitude = float(request.args.get('lat'))
    longitude = float(request.args.get('lng'))

    # Dapatkan zona waktu dari longitude dan latitude
    tf = TimezoneFinder()
    timezone_str = tf.certain_timezone_at(lng=longitude, lat=latitude)

    # Buat objek timezone
    tz = timezone(timezone_str) 

    # Dapatkan waktu lokal saat ini 
    local_datetime = datetime.now()

    # Konversi ke UTC (GMT)
    utc_datetime = local_datetime.astimezone(tz)

    result = {
        'code':200,
        'timezone':tz.zone,
        'GMT':int(utc_datetime.strftime("%z")[0:3]),
    }
    # Cetak hasil dalam format GMT
    return json.dumps(result)

