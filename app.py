import pandas as pd
import numpy as np
import math
import itertools
import numpy
from flask import Flask, request, render_template, jsonify
from flask_ngrok import run_with_ngrok
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import requests
import ast
import json

app = Flask(__name__)
#run_with_ngrok(app) 

@app.route("/home", methods=['GET'])
def home2():
    f=open("temp.html","r")
    text=f.read()
    f.close()
    return text

@app.route("/", methods=['GET'])
def home():
    f=open("temp.html","r")
    text=f.read()
    f.close()
    return text
