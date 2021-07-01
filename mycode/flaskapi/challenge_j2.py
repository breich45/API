#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/change", methods = ["POST", "GET"])
def add_data():
    if request.method == "POST":
       new_dict = {}
       new_dect = {"hostname" : request.form.get("hostname"), "ip" : request.form.get("ip"), "fqdn" : request.form.get("fqdn")}
       groups.append(new_dict)
       return redirect(url_for("/"))

@app.route("/")
def displaystuff():
    return render_template("challenge.html", func_groups= groups)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
