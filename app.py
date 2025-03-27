from flask import Flask, Response
import api.main
import badge

app = Flask(__name__)

@app.route('/')
def hello():
    ret_value = badge.create_svg()
    return Response(ret_value,mimetype='image/svg+xml')

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User: {api.main.main(username)}"

if __name__ == '__main__':
    app.run(debug=True)
