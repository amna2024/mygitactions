from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"

# app.py
print('It Works')
def test_pass():
    assert True == True

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
