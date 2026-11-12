from flask import Flask, render_template, jsonify, request, Response, redirect
import random
import requests
import secrets


app = Flask(__name__)

rooms = {}



@app.route("/")
def index():
    if request.query_string:
        return render_template("chat.html")
    return render_template("index.html")

@app.route('/api/room/<id>', methods=['POST', 'GET'])
def api_rooms(id):
    if request.method=="GET":        

        return jsonify(rooms.get(id, []))

    msg = request.get_data(as_text=True)
    rooms.setdefault(id, []).append(msg)
    return jsonify(ok=True)   


session = requests.Session()


    
app.run(port=8080, debug=True)
