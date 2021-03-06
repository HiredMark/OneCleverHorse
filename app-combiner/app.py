import random
import json
import requests
from flask import Flask, request, render_template, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/comb', methods=['GET', 'POST'])
def comb():
    adj1 = request.args.get('randj','http://appadjevtive:5001/adj')
    adj2 = request.args.get('randj','http://appadjective:5001/adj')
    noun1 = request.args.get('rnoun','http://appnoun:5002/noun')
    noun2 = request.args.get('rnoun','http://appnoun:5002/noun')
    rcomb = txt.title(str(adj1))+txt.title(str(noun1))+txt.title(str(adj2))+txt.title(str(noun2))
    return Responce( str(rcomb), mimetype='text/plain' )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
