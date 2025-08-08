#builtin imports
from typing import *
import datetime
from threading import Thread 

#third party imports
from flask import Flask, request, redirect, render_template
from flask import Response


#self-coded imports
import STANDARD_API_OUTPUT
from Server import Server
import is_server_last_contact_too_long_ago
import bot_thread_function

JSON = Dict[str,Any]
app = Flask("mason")



servers:Dict[str, Server] = {} #where key is the ip address and value is the Server Object

#for testing purpose =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


#server with lost connection
servers["A"] = Server("A", 100, 50, 50)
_15_seconds_ago = datetime.datetime.now() - datetime.timedelta(seconds=15)
servers["A"].last_contact = datetime.datetime.now()

#server with high cpu 
servers["B"] = Server("B", 100, 50, 90)

#server with high memory 
servers["C"] = Server("C", 100, 90, 50)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=


"""
for i in range(100):
    servers[i] = Server("dont_care_about_me", 100, 50, 50)
"""
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
    total_ram:float = request.json["total_ram"]
    used_ram:float = request.json["used_ram"]
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
    return render_template("main.html", servers=servers, is_server_last_contact_too_long_ago=is_server_last_contact_too_long_ago)




def main():
    bot_thread = Thread(daemon=True , target=bot_thread_function.func, args=[servers])
    bot_thread.start()
    app.run(debug=True, host="0.0.0.0", port=8698)
    bot_thread.join()

if __name__ == "__main__":
    main()