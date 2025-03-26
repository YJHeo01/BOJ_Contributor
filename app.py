from flask import Flask
import api.main

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User: {api.main.main(username)}"

if __name__ == '__main__':
    app.run(debug=True)
