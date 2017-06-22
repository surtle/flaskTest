from flask import Flask
app = Flask("peacefulravine")

@app.route("/")
def hello():
	return "Hello World!"

def goodbye():
        print "Goodbye"

if __name__ == "__main__":

        try:
                goodbye()

        except KeyboardInterrupt:
                raise

        
                
