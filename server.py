from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")   

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)