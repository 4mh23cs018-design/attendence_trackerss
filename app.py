from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if  _name_=='_main_':
    app.run(debug=true,host='0.0.0.0',port=5000)git