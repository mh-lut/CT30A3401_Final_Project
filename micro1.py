#help received: https://www.youtube.com/watch?v=5aYpkLfkgRE

from flask import Flask #for api
import psutil #for pc usage stats


app = Flask(__name__) # tell Flask that everything that it need is here

# routes...
@app.route("/cpu", methods=['GET'])
def cpu():
    return str(psutil.cpu_percent()) # return cpu percent

@app.route("/memory", methods=['GET'])
def memory():
    return str(psutil.virtual_memory().percent) # return memory percent


app.run(host="0.0.0.0", port=8000) # adress this pc and port 8000