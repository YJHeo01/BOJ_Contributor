from flask import Flask, Response
import api.main
import images.badge as badge

app = Flask(__name__)

@app.route('/<username>')
def hello(username):
    user_data = api.main.main(username)
    image = badge.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/user/<username>')
def show_user_profile(username):
    user_data = api.main.main(username)
    image = badge.create_svg(user_data)
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

if __name__ == '__main__':
    app.run(debug=True)
