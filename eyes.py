from http.client import responses
from .models import Logdb
import json

def watch(req, res):
    verb = req.method
    path = req.path
    status = res.status_code
    duration = "0.34"
    payload = req.body.decode("utf-8")
    header = req.headers
    resp = res.getvalue().decode("utf-8")
#    collect = Logdb.objects.create(verb=verb,path=path,status=status,duration=duration,payload=payload,header=header,responses=resp)
    print(verb)
    print(path)
    print(status)
    print(duration)
    print(payload)
    print(header)
    print(resp)
    return True
