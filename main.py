from flask import Flask
app = Flask("peacefulravine")

@app.route("/")
def hello():
	return "Hello World!"
