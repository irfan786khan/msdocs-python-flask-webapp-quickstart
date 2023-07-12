from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Azure! My Flask app is up and running.'

# Define other routes and functionality for your app

if __name__ == '__main__':
    app.run()
