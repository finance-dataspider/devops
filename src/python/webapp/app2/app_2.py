from flask import Flask,jsonify
import time
app = Flask(__name__)

@app.route("/2")
def hello():
    print('This should be in new image')
    return jsonify("app2!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5000)