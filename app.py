from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route("/")
def hello():
    return "Hello World!"  # Response to GET requests at '/'

# Entry point for running the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  # Host the app on all network interfaces
