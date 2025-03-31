from flask import Flask, Response
import api.main
import images.badge as badge

app = Flask(__name__)

@app.route('/<username>')
def hello(username):
    user_data = api.main.main(username)
    user_profile = badge.create_svg(user_data)
    return Response(user_profile,mimetype='image/svg+xml')

@app.route('/user/<username>')
def show_user_profile(username):
    user_data = api.main.main(username)
    user_profile = badge.create_svg(user_data)
    return Response(user_profile,mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(debug=True)
