from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('Ometeotl.pkl','rb') as file:
    model = pickle.load(file)

@app.route('/explore', method =['POST'])
def explore():
    data = request.get_json()
    search_query = data[''] #{needs that fucking dictioanary}