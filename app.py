from flask import Flask, Response, request, redirect, url_for
import api.main
import images.badge as badge

app = Flask(__name__)

@app.route('/<username>')
def hello(username):
    user_data = api.main.main(username)
    image, hash = badge.create_svg(user_data)
    if request.args.get('v') != hash:
        return redirect(url_for('show_user_profile', username=username, v=hash))
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

@app.route('/user/<username>')
def show_user_profile(username):
    user_data = api.main.main(username)
    image, hash = badge.create_svg(user_data)
    if request.args.get('v') != hash:
        return redirect(url_for('show_user_profile', username=username, v=hash))
    response = Response(image,mimetype='image/svg+xml')
    response.headers['Cache-Control'] = 'public, max-age=3600'
    return response

if __name__ == '__main__':
    app.run(debug=True)
