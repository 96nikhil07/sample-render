from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])  # Define the route for the root URL ("/")
def hello_world():
    return "Welcome to Nikhil's World Hi hello"

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False in production