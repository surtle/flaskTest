from flask import Flask
app = Flask("peacefulravine")


def hello():
	return "Hello World!"
@app.route("/")
def goodbye():
        return "Goodbye"

if __name__ == "__main__":

        try:
                goodbye()

        except KeyboardInterrupt:
                raise

        
                
