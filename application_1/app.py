from flask import Flask, request, jsonify
import os
from kubernetes import client, config

app = Flask(__name__)


@app.route("/")
def home():
    html = f"<h3>Application 1</h3>"
    return html.format(format)


@app.route("/myPodInfo", methods=['GET'])
def response():
    pod_name=os.getenv('MY_POD_NAME')
    pod_ip=os.getenv('MY_POD_IP')
    return {"pod_ip":pod_ip,'pod_name':pod_name}
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True) 
    
    
    
    #v3