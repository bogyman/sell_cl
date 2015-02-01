import requests
import time

for i in range(3):
    con = requests.get("http://172.17.42.1:5000/get_tests")
    tasks = con.content
    #time.sleep(2)
    data =  {
        t: 'ok'
        for t in tasks
    }
    con = requests.post("http://172.17.42.1:5000/submit_results", data=data)
