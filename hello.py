from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ping', methods=['GET', 'POST']) # Define a route that responds to both GET and POST requests
def ping():
    return {"message": "why you pinging me?"}

if __name__ == '__main__':
    app.run(debug=True) # Run the Flask app in debug mode , auto-reloads on code changes