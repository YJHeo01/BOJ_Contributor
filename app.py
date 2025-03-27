from flask import Flask, Response
import api.main
import badge

app = Flask(__name__)

@app.route('/')
def hello():
    ret_value = badge.create_svg(["sk14cj",1,2,3,4])
    return Response(ret_value,mimetype='image/svg+xml')

@app.route('/user/<username>')
def show_user_profile(username):
    user_data = api.main.main(username)
    user_profile = badge.create_svg(user_data)
    return Response(user_profile,mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(debug=True)
