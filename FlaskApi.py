from logging import error
from flask import Flask,jsonify,request
 
app = Flask(__name__)
tasks = [{"id":1,"title":u"Complete Homework","done":False},{"id":2,"title":u"Complete Project","done":False}]

@app.route("/add-contact",methods = ["POST"])
def add():
    if not request.json:
        return jsonify({
            "name":"error",
            "Contact":"provide the number"

        },400)
    p = {"id":tasks[-1]["id"]+1,"title":request.json["title"],"done":False}
    tasks.append(p)
    return jsonify({
        "status":"Sucsess",
        "message":"Task added"
        })
if __name__ == "__main__":
    app.run(debug=True)