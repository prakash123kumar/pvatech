from flask import Flask

app =Flask(__name__,template_folder='template')
from app import routes

#host="0.0.0.0",port=5008,debug=False
#app.run(host="0.0.0.0",port=5001, debug=False)
app.run(debug=True)
