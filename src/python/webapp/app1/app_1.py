from flask import Flask,jsonify
import time
app = Flask(__name__)

@app.route("/1")
def hello():
    print('This should be in new image')
    return jsonify("app1! update!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5000)