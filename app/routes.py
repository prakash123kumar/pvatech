from app import app
from flask import Flask, render_template#,request,redirtect
import pandas as pd
import io 
import  os
import numpy as np

@app.route('/')
def index():
    return render_template('index.html')