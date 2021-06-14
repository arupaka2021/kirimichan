import requests, datetime, json, os, sys, psycopg2, traceback, configparser
from requests.packages.urllib3.exceptions import InsecureRequestWarning

PATHCODE_URL = 'http://www.jma.go.jp/bosai/common/const/area.json'

# InsecureRequestWarning対策
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getjson(request=PATHCODE_URL,dump=0):
    try:
        res = requests.get(request,verify=False)
        if dump == 0:
            return res.json()
        else:
            return json.dumps(rawdata, indent=4, ensure_ascii=False)

    except Exception:
        return None
