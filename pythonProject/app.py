from flask import Flask,request,jsonify
from config.wmpncaircraft import getmap
app = Flask(__name__)

@app.route('/')
def hello_world():
   getmap()
   return "Hello World"

if __name__ == '__main__':
   app.run()