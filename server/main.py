#builtin imports
from typing import *

#third party imports
from flask import Flask, request, redirect, render_template
from flask import Response

#self-coded imports
import STANDARD_API_OUTPUT
from Server import Server

JSON = Dict[str,Any]
app = Flask("mason")



servers:Dict[str, Server] = {}
servers["dont_care_about_me"] = Server("dont_care_about_me", 100, 50, 50)


#API SECTION ==========================================
@app.post("/api/server/submit/0XSADADAWDADFGRsdfesesee")
def api_server_submit()->JSON:
    """
    given request must be in json format
    given request must have the following fields
        1.ip_addrs
        2.total_ram
        3.used_ram
        4.cpu_usage
    """
    ip_addrs:str = request.remote_addr
    total_ram:int = request.json["total_ram"]
    used_ram:int = request.json["used_ram"]
    cpu_usage:int = request.json["cpu_usage"]

    #will write checking later
    servers[ip_addrs] = Server(ip_addrs, total_ram, used_ram, cpu_usage)

    output = STANDARD_API_OUTPUT.new()
    output["was_ok"] = True
    output["exit_code"] = "OK"
    output["caption"] = "ok"
    output["data"] = None
    return output



#GUI SECTION ==========================================
@app.route("/")
def index()->Response:
    return redirect("/gui/main")


@app.route("/gui/main")
def gui_main()->str:
    return render_template("main.html", servers=servers)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8698)